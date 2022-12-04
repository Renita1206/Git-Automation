import os
from git import Repo 

path = input("Enter path of local repository: ")
print(path)
repo = Repo(path)
try:
    status = repo.git.status()
    print(status)
except:
    print("Oops...Something went wrong")