import os
from git import Repo 

path = os.curdir
print(path)
repo = Repo(path)
files = os.listdir(path)                                         
print(files[1:])
try:
    repo.index.add(files[1:])
    message = input("Enter commit message for repository: ")
    repo.index.commit(message)
    print("Changes have been committed")
    origin = repo.remote(name='origin')
    print(origin.push())
    print("Changes have been pushed")
except:
    print("Oops...something went wrong")