import os
import subprocess as sp
from pathlib import Path
import re
import sys
file_paths = []  # List which will store all of the full filepaths.
filepath ='GitPasswordChecker/Keywords.txt'
WordList = Path(filepath).read_text().splitlines()
msgList=[]
wordRe = re.compile("|".join(WordList))
skppiedList=[]
# Walk the tree.
for root, directories, files in os.walk('.'):
    try:
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            
            if wordRe.search(Path(filepath).read_text()):
                msgList.append(f' Found Keyword in the following file {filepath}')
    except Exception:
        print(filename)
print(msgList)
        
        
            
            