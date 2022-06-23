import os
path = input("Enter file path and name")
path_check = os.path.exists("path")
if path_check == "true":
else:
    print(spaceholder1)
    print("Requested file does not exist! Check path and try again!")
    print(spaceholder1)
    def tree_printer(root):
        for root, dirs, files in os.walk(root):
            for d in dirs:
                print(os.path.join(root, d))
            for f in files:
                print(os.path.join(root, f))
    tree_printer('C:/pyproject/')
    print(spaceholder1)