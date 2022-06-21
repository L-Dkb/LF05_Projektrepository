z = 0
a = 0
b = 0
c = 0
d = 0
print("Welcome to the Employee Management Program (EMP)")
print("==================================================")
print("Please choose one of the following options:")
import os
while (z != 6):
    print("""
    1.create
    2.read
    3.update
    4.delete
    5.save / export
    6.end program
    """)
    z = int(input("Please enter a number between 1 and 6:"))
    if z == 1:
        print("==================================================")
        print("CREATE")
        print("==================================================")
        while (a !=4):
            print("""
            1.Create new database
            2.Create new entry
            3.add new column (for all datasets)
            4.back
            """)
            a = int(input("Please enter a number between 1 and 4:"))
            if a == 1:
                foldername = input("Enter new folder name:")
                folderpath = input("Enter path for new folder:")
                import.os
                os.mkdir(C:/pyproject/newfolder/)
                a = int(input("Please enter a number between 1 and 4:"))
            elif a == 2:
                filename1 = print(input("Enter file name:"))
                filetype1 = print(input("Enter file type:"))
                open(str(filename1) + "." + str(filetype1), "x")
                a = int(input("Please enter a number between 1 and 4:"))
            elif a == 3:
                print("3.add new column (for all datasets)")
                a = int(input("Please enter a number between 1 and 4:"))
            elif a == 4:
                print("Back to the menu")
    elif z == 2:
        print("==================================================")
        print("READ")
        print("==================================================")
        while (b !=5):
            print("""
            1. Open Database
            2. show single dataset
            3. filter ...
            4. show empty fields
            5. back
            """)
            b = int(input("Please enter a number between 1 and 5:"))
            if b == 1:
                print("1. show all datasets")
                b = int(input("Please enter a number between 1 and 5:"))
            elif b == 2:
                print("2. show single dataset")
                b = int(input("Please enter a number between 1 and 5:"))
            elif b == 3:
                print("3. filter ...")
                b = int(input("Please enter a number between 1 and 5:"))
            elif b == 4:
                print("4. show empty fields")
                b = int(input("Please enter a number between 1 and 5:"))
            elif b == 5:
                print("Back to the menu")
    elif z == 3:
        print("==================================================")
        print("UPDATE")
        print("==================================================")
        while (c !=3):
            print("""
            1. update all
            2. update single dataset
            3. back
            """)
            c = int(input("Please enter a number between 1 and 3:"))
            if c == 1:
                print("1. update all")
                c = int(input("Please enter a number between 1 and 3:"))
            elif c == 2:
                print("2. update single dataset")
                c = int(input("Please enter a number between 1 and 3:"))
            elif c == 3:
                print("Back to the menu")
    elif z == 4:
        print("==================================================")
        print("DELETE")
        print("==================================================")
        while (d !=4):
            print("""
            1. delete all
            2. delete single row
            3. delete single column
            4. back
            """)
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
        print("==================================================")
        print("SAVE/EXPORT")
        print("==================================================")
    elif z == 6:
        print("==================================================")
        print("Good Bye!")
        print("====================== END =======================")
