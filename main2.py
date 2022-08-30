import subprocess as sp
from pathlib import Path
import re
import sys
import os
import csv
msgList=[]

# Reads the Keyword list$
filepath ='GitPasswordChecker/Keywords.txt'
WordList = Path(filepath).read_text().splitlines()
with open(filepath,"r") as f:
    rd = csv.reader(f)
    lst = list(rd)    # lst is a list of lists in expected format
WordList = lst[0]
#with open(filepath,'w') as file:
#    pass
# If the wordlist is empty
if len(WordList) == 0:
    sys.exit(f"The Keyword list is empty. Enter keywords in the file seperated by a comma.")
wordRe = re.compile('|'.join(WordList))
# Create a list of commits
args = ['git', 'log', '--pretty=format:%h%x09%an%x09%ad%x09%s']
commits = [ln.split('\t') for ln in sp.check_output(args, text=True).splitlines()]

# Loops over commits
try:
    for commit in commits:
        sp.run(['git','checkout',commit[0]])
        for root, directories, files in os.walk('.'):
            try:
                for filename in files:
                    # Join the two strings in order to form the full filepath.
                    filepath = os.path.join(root, filename)

                    if wordRe.search(Path(filepath).read_text()):
                        msgList.append(f'Commit ID: {commit[0]} Commit Name: "{commit[3]}" Found Keyword in the following file {filepath}')
            except Exception:
                pass
    sp.run(['git','checkout','Test2'])
except Exception as e:
    pass

print('\n'.join(msgList))