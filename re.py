import os
import subprocess as sp
from pathlib import Path
import re
import sys
import csv
file_paths = []  # List which will store all of the full filepaths.
filepath ='GitPasswordChecker/Keywords.txt'
WordList = Path(filepath).read_text().splitlines()
type(WordList)
print(WordList)
with open(filepath) as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
with open(filepath,"r") as f:
    rd = csv.reader(f)
    lst = list(rd)    # lst is a list of lists in expected format
print(lst[0])