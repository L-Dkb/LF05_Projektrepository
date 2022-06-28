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
    6.help
    7.end program
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
            4. show empty filds
            5. back
            """)
menu3 = ("""
            1. update all
            2. Change file name and type.
            3. Show directory tree.
            4. Back
            """)
menu4 = ("""
            1. Delete File.
            2. delete single row
            3. delete single column
            4. back
            """)
spaceholder1 = ("==================================================")

print("Welcome to the Employee Management Program (EMP)")
print(spaceholder1)
print("Please choose one of the following options:")

#MAIN MENU
while (z != 7):
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
                folder = input("Enter new folder name:")
                path = input("Enter path for new folder:")
                os.mkdir(path + folder)
                print(folder + " successfully created at " + path)
#CREATE FILE FUNCTION
            elif a == 2:
                file = input("Enter file name:")
                filetype = input("Enter file type:")
                path = input("Enter file path:")
                open(path + file + filetype, "x")
                print(file + " successfully created at " + path1)
#SHOW DIRECTORY TREE
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
                
#WRITE 
            elif b == 3:
                spaceholder1 = ("==================================================")
                path = input("Enter file path and name:")
                path_check = os.path.exists(path)
                if path_check:
                    f = open(path, "a")
                    x = input("Enter the text you want to add: ")
                    f.write(x)
                    f.close()
                    print("Ihr Eintrag wurde übernommen.")
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
#SHOW FILE TREE
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
                path = input("Enter path and filename of the file that you want to delete:")
                if os.path.exists(path):
                    os.remove(path)
                else:
                    print("File doesnt exist")
                    print("Check path and try again!")
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
        print("Help")
        print("Press numbers to navigate through the help menus")
        print("1: Help Menu (CREATE)")
        print("2: Help Menu (READ)")
        print("3: Help Menu (UPDATE)")
        print("4: Help Menu (DELETE)")
        print("5: Help")
        helpinput = input("Please enter a number between 1 and 5:")
        while(helpinput !=5):
            if helpinput == 1 :
                print
            elif helpinput == 2:
                print
            elif helpinput == 3:
                print
            elif helpinput == 4:
                print
            elif helpinput == 5:
                print
        input("Press enter key to continue!")
        print(spaceholder1)
    elif z == 7:
        print(spaceholder1)
        print("Good Bye!")
        print("====================== END =======================")
