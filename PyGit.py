import os
from git import Repo 

pathOfFolder = input("Enter path of folder: ")
folders = os.listdir(pathOfFolder)
for i in folders:
    pathOfGit = pathOfFolder + '\\' + i + '\\.git'
    #print(i ,os.path.exists(pathOfGit))
    if(os.path.exists(pathOfGit)):
        path = pathOfFolder + '\\' + i
        print(path)
        repo = Repo(path)
        repo.git.add(all=True)
        message = input("Enter commit message for " + i + " repository: ")
        repo.index.commit(message)
        print("Changes have been committed")
        origin = repo.remote(name='origin')
        origin.push()
        print("Changes have been pushed")
