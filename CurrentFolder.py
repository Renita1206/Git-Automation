import os
from git import Repo 

path = os.curdir
print(path)
repo = Repo(path)
try:
    repo.git.add(all=True)
    
    status = repo.git.status()
    print(status)

    message = input("Enter commit message for repository: ")
    repo.index.commit(message)
    print("Changes have been committed")

    status = repo.git.status()
    print(status)

    origin = repo.remote(name='origin')
    origin.push()
    print("Changes have been pushed")

    status = repo.git.status()
    print(status)
except:
    print("Oops...something went wrong")