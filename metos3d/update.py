
import os

def update_metos3d():
    
    path = os.path.dirname(os.path.abspath(__file__))
    os.system("cd " + path + "; git pull")
#    print(path)
#    os.system("pwd")
#    os.system("cd /usr/; pwd")
#    os.system("pwd")


