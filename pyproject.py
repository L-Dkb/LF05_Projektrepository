import os
import os.path
z = 0
a = 0
b = 0
c = 0
d = 0
#Menus
mainmenu = ("""
    1.create
    2.read
    3.update
    4.delete
    5.save / export
    6.end program
    """)
menu1 = ("""
            1.Create new folder
            2.Create new file
            3.Show file tree
            4.back
            """)
menu2 = ("""
            1. Read file
            2. Read specific line in file
            3. 
            4. show empty fields
            5. back
            """)
menu3 = ("""
            1. update all
            2. Change file name and type.
            3. Show directory tree.
            4. Back
            """)
menu4 = ("""
            1. delete all
            2. delete single row
            3. delete single column
            4. back
            """)
spaceholder1 = ("==================================================")

print("Welcome to the Employee Management Program (EMP)")
print(spaceholder1)
print("Please choose one of the following options:")

#MAIN MENU
while (z != 6):
    print(spaceholder1)
    print("MAIN MENU")
    print(spaceholder1)
    print(mainmenu)
    print(spaceholder1)
    z = int(input("Please enter a number between 1 and 6:"))

#CREATE MENU
    if z == 1:
        while (a !=4):
            print(spaceholder1)
            print("CREATE")
            print(spaceholder1)
            print(menu1)
            a = int(input("Please enter a number between 1 and 4:"))
#CREATE FOLDER FUNCTION
            if a == 1:
                foldername = input("Enter new folder name:")
                folderpath = input("Enter path for new folder:")
                os.mkdir(folderpath + foldername)
                print(foldername + " successfully created at " + folderpath)
#CREATE FILE FUNCTION
            elif a == 2:
                filename1 = input("Enter file name:")
                filetype1 = input("Enter file type:")
                filepath1 = input("Enter file path:")
                open(filepath1 + filename1 + filetype1, "x")
                print(filename1 + " successfully created at " + filepath1)
#SHOP DIRECTORY TREE
            elif a == 3:
                print("File tree for C:/pyproject/")
                def tree_printer(root):
                    for root, dirs, files in os.walk(root):
                        for d in dirs:
                            print(os.path.join(root, d))
                        for f in files:
                            print(os.path.join(root, f))
                tree_printer('C:/pyproject/')
#BACK TO MAIN MENU
            elif a == 4:
                print("Back to the menu")
#READ MENU
    elif z == 2:
        print(spaceholder1)
        print("READ")
        print(spaceholder1)
        while (b !=5):
            print(menu2)
            b = int(input("Please enter a number between 1 and 5:"))
#READ FILE FUNCTION
            if b == 1:
                spaceholder1 = ("==================================================")
                path = input("Enter file path and name:")
                path_check = os.path.exists(path)
                if path_check:
                    x = open(path, "r")
                    print("Showing " + path + " contents...")
                    print(x.read())
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
#READ FILE LINE FUNCTION
            elif b == 2:
                spaceholder1 = ("==================================================")
                path = input("Enter file path and name:")
                path_check = os.path.exists(path)
                if path_check:
                    line = int(input("Enter line number:"))
                    x = open(path, "r")
                    print("Showing " + line + " of file " + path)
                    print(x.readline(line))
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
                print("3. filter ...")
                b = int(input("Please enter a number between 1 and 5:"))
            elif b == 4:
                print("4. show empty fields")
                b = int(input("Please enter a number between 1 and 5:"))
            elif b == 5:
                print("Back to the menu")
#UPDATE MENU
    elif z == 3:
        print(spaceholder1)
        print("UPDATE")
        print(spaceholder1)
        while (c !=4):
            print(menu3)
            c = int(input("Please enter a number between 1 and 3:"))
            if c == 1:
                print("1. update all")
                c = int(input("Please enter a number between 1 and 3:"))
#RENAME FILE FUNCTION
            elif c == 2:
                print("2. update single dataset")
                directorypath = input("Set working directory path:")
                file1 = input("Old file name:")
                file2 = input("New file name:")
                os.chdir(directorypath)
                os.rename(file1, file2)
                print("File " + file1 + " was renamed to " + file2)
            elif c == 3:
                print("File tree for C:/pyproject/")
                def tree_printer(root):
                    for root, dirs, files in os.walk(root):
                        for d in dirs:
                            print(os.path.join(root, d))
                        for f in files:
                            print(os.path.join(root, f))
                tree_printer('C:/pyproject/')
#DELETE MENU
    elif z == 4:
        print(spaceholder1)
        print("DELETE")
        print(spaceholder1)
        while (d !=4):
            print(menu4)
            d = int(input("Please enter a number between 1 and 4:"))
            if d == 1:
                print("1. delete all")
                d = int(input("Please enter a number between 1 and 4:"))
            elif d == 2:
                print("2. delete single row")
                d = int(input("Please enter a number between 1 and 4:"))
            elif d == 3:
                print("3. delete single column")
                d = int(input("Please enter a number between 1 and 4:"))
            elif d == 4:
                print("Back to the menu")
    elif z == 5:
        print(spaceholder1)
        print("SAVE/EXPORT")
        print(spaceholder1)
    elif z == 6:
        print(spaceholder1)
        print("Good Bye!")
        print("====================== END =======================")
