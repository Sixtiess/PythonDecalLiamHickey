# File: homework5.py

# --- Vocabulary Review ---

# 1. Git vs. GitHub
# Git is the version control tool that runs locally, GitHub is the website that hosts git repositories online.

# 2. Terminal vs. Command Line
# The terminal is the window that displays everything, the command line is where you type commands in.

# 3. Local vs. Remote Repository
# A local repository lives on your own computer, a remote repository lives on a server like GitHub.

# 4. Version Control
# A way of tracking changes to files over time so earlier versions can be recovered and people can work together.

# 5. Staging Area
# Where changes wait after git add and before git commit, it decides what goes into the next commit.

# 6. git add
# Moves changes from the working directory into the staging area.

# 7. git commit
# Saves everything in the staging area as a snapshot in the local repository, with a message.

# 8. git push
# Sends local commits to the remote repository.

# 9. git status
# Shows which files are modified, staged, or untracked.

# 10. git pull
# Fetches new commits from the remote repository and merges them into the local one.

# 11. pwd
# Prints the current working directory.

# 12. ls
# Lists the files and folders in the current directory.

# 13. cd
# Changes the current directory.

# 14. nano
# A text editor that runs inside the terminal.

# 15. touch
# Creates a new empty file.

# 16. mv
# Moves a file or folder to a new location, or renames it.

# 17. rm
# Removes a file. It is permanent, there is no trash.

# 18. cat
# Prints the contents of a file to the terminal.


# --- A Directory Tree ---

# 1. What command tells you your current working directory?
# pwd

# 2. What command lists all the files in your current working directory?
# ls

# 3. What commands move you to the brianna repo and pull the latest changes?
# cd ../brianna_repo
# git pull

# 4. How would you move the new homework.py to the homework/ folder in your personal repository?
# mv homework.py ../judy_decal/homework/

# 5. How would you move yourself to the same repository as homework.py?
# cd ../judy_decal/homework

# 6. How would you see the contents of homework.py in the terminal?
# cat homework.py

# 7. What commands save the changes and push them to the remote repository?
# git add .
# git commit -m "done with homework"
# git push origin main

# 8. What does the rejected push error mean, and how is it fixed?
# The remote has commits that Judy doesn't have locally, so git won't let her push over them.
# She should pull first to bring those commits in, then push again:
# git pull origin main
# git push origin main

# 9. What absolute path moves you to Recents/?
# Recent/ sits in the home directory, next to python_decal/
# cd ~/Recent




def checkDataType(value):
    return type(value).__name__



def evenOrOdd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total



def duplicateList(items):
    duplicated = []
    for item in items:
        duplicated.append(item)
        duplicated.append(item)
    return duplicated




# The original was missing the colon after the function header, and the body wasn't indented.
def square(num):
    return num * num




if __name__ == "__main__":
    print(duplicateList(["a", "b", "c"]))
