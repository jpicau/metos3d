import os

print("*** m3d, python, begin ********************************************************************")

CC = os.environ["CC"]
FC = os.environ["FC"]

print("CC:", CC)
print("FC:", FC)

os.system("./m3d.exe")
os.system("which -a mpicc")

print("*** m3d, python, end ********************************************************************")


