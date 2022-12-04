import os
from git import Repo 

path = os.curdir
print(path)
repo = Repo(path)
try:
    repo.git.add(all=True)
    message = input("Enter commit message for repository: ")
    repo.index.commit(message)
    print("Changes have been committed")
    origin = repo.remote(name='origin')
    origin.push()
    print("Changes have been pushed")
except:
    print("Oops...something went wrong")