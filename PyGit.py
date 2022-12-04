import os
from git import Repo 

folders = os.listdir('C:\\Users\\Renita Kurian\\Documents\\Academic')
for i in folders:
    pathOfGit = 'C:\\Users\\Renita Kurian\\Documents\\Academic\\' + i + '\\.git'
    #print(i ,os.path.exists(pathOfGit))
    if(os.path.exists(pathOfGit)):
        path = 'C:\\Users\\Renita Kurian\\Documents\\Academic\\' + i
        #print(path)
        repo = Repo(path)
        files = os.listdir(path)
        #print(files[1:])
        repo.index.add(files[1:])
        message = input("Enter commit message for" + i 
        + "repository: ")
        repo.index.commit(message)