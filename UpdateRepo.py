import os
from git import Repo 

path = input("Enter path of local repository: ")
pathOfGit = path + '\\.git'
if(not os.path.exists(pathOfGit)):
    print("No such repository")
    exit(0)
print(path)
repo = Repo(path)
try:
    repo.git.add(all=True)
    
    status = repo.git.status()
    print(status)
    print()

    message = input("Enter commit message for repository: ")
    repo.index.commit(message)
    print("Changes have been committed")

    status = repo.git.status()
    print(status)
    print()

    origin = repo.remote(name='origin')
    origin.push()
    print("Changes have been pushed")

    status = repo.git.status()
    print(status)
except:
    print("Oops...something went wrong")