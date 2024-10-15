import os, sys

root_path = os.path.dirname(__file__)
print(root_path)

myclass_path = os.path.join(root_path, "my_class")

sys.path.append(myclass_path)

import my_class
a = my_class.MyClass()
