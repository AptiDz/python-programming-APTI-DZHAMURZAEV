import os, sys
os.system("clear ; echo 'Från terminalen'")

print(f"{'='*30}main.py{'='*30}\n")
import vector

print("globals")
glob_dict = globals()
#print(glob_dict['__name__'])
import vector as vc
print("sys.modules")
print(sys.modules['vector'])

