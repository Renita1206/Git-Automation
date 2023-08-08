import os
from git import Repo 

path = path = os.curdir
#print(path)
repo = Repo()
try:
    g = repo.git
    logs = g.log(author="Renita Kurian")
    #print(logs)
    for i in logs.split("\n"):
        #print(i.split())
        if(i == ""):
            continue
        words = i.split()
        if words[0] == 'commit':
            #print("commit ID", i)
            continue
        elif words[0] == 'Date:':
            #print("Date", i)
            continue
        elif words[0] == 'Author:':
            #print("Author ", i)
            continue
        else:
            print("Msg", i)

except:
    print("Oops...Something went wrong")