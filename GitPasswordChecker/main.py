import subprocess as sp
from pathlib import Path
import re
import sys
import os
import csv

############################ Section 1: Keywords list ############################
# Reads the Keyword list$
filepath ='GitPasswordChecker/Keywords.txt'
with open(filepath,"r") as f:
    rd = csv.reader(f)
    lst = list(rd)
# If the wordlist is empty The program will Exit
if len(lst) == 0:
    sys.exit(f"The Keyword list is empty. Enter keywords in the Keywords.txt seperated by a comma.")
wordList = lst[0]
# Empty the list after reading
with open(filepath,'w') as file:
    pass
#combines the list of keywords
wordRe = re.compile("|".join(wordList))

############################ Section 2: Creates a new Git Branch and adds gitignore ############################
#Gets the current branch name
initialBranch =sp.check_output(['git','branch','--show-current'], text=True).strip()
# Creates a new branch called GitPasswordChecker
newBranch ='GitPasswordChecker' # branch Name
sp.run(['git','checkout','-b',newBranch])
writePath='.gitignore'
# If .gitignore does not exists
if not os.path.exists(writePath):
    #Creates file and inserts 'GitPasswordChecker'
    with open(".gitignore", "a") as file:
        file.write("\nGitPasswordChecker")
else:
    #If the file exits it will open the file and check if the GitPasswordChecker in the file it will be added
    with open('.gitignore','r') as file:
        gitignore=file.read().split('\n')
    if not 'GitPasswordChecker' in gitignore:
        with open(".gitignore", "a") as file:
            file.write("\nGitPasswordChecker")
# push initial commit for the branch
sp.run(['git','add','.'])
sp.run(['git','commit','-m','GitPasswordChecker inital commit'])

############################ Section 3: extracts the list of commits ############################

# extracts the list of commits
args = ['git', 'log', '--pretty=format:%h%x09%an%x09%ad%x09%s']
commits = [ln.split('\t') for ln in sp.check_output(args, text=True).splitlines()]

############################ Section 4: # Loops over commits and serch for keywords ############################
# Empty list that will be filled with messages
msgList=[]

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
            except UnicodeDecodeError:
                # Skips files that can't be open
                pass
except Exception as e:
    pass
finally:
############################ Section 5: # Clean up ############################
#Checkout to orginal branch 
    sp.run(['git','checkout',initialBranch])
    sp.run(['git', 'branch', '-D',newBranch])
    if len(msgList)!=0:
        print('\n\n Found keyword in the following commmits:\n')
        print('\n'.join(msgList))
    else:
        print('\n\n Didnt fint any commits with the keyword included\n')
