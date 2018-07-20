import os

print("*** m3d, python, begin ********************************************************************")

CC = os.environ["CC"]
CXX = os.environ["CXX"]
FC = os.environ["FC"]

print("CC: ", CC)
print("CXX:", CXX)
print("FC: ", FC)

os.system("m3d.exe")
os.system("which -a mpicc")
os.system("which -a mpic++")
os.system("which -a mpif90")

print("*** m3d, python, end ********************************************************************")


