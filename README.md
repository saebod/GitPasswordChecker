# GitPasswordChecker
This project scans all previous commits to find passwords/keys/tokens that are entered in the keyword.txt file.
## Motivation
This project is motived by the fact that we are all humans and forget to remove passwords from previous commits when we start out projects.
## How To Use
Add the folder *GitPasswordChecker* to your project and add  *GitPasswordChecker*  to your .gitignore.
Enter the keywords that you want to look for in the txt file GitPasswordChecker/Keywords.txt (The scripts will empty the txt file when it is done.)
Run the script in main.py
## How does it work?
1. The script will start by looking at the GitPasswordChecker/Keywords.txt file and list the key words. If the list is empty then the script will exit.

2. The script will list all your previous commits
   
3. For each commit the script will open all files and try to see search for the keywords.

4. if it finds the keyword it will append the details to a list

5. When the script is done it will print the list and checkout to master.