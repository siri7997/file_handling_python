
from pathlib import Path
def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():

    try:
        readfileandfolder()

        name=input("set your file name:- ")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data=input("what do u want to write")
                fs.write(data) 

            print("FILE CREATED SUCCESSFULLY!")
        else:
            print("the file already exists")
    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try:
        readfileandfolder()
        name=input("Enter the file u want to read:- ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data=fs.read()
                print(data)
            print("FILE READ SUCCESSFULLY")
        else:
            print("file does not exist")
    except Exception as err:
        print(f"an error has occured {err}")

def updatefile():
    try:
        readfileandfolder()
        name=input("to which file u want to update:- ")
        p=Path(name)
        if p.exists() and p.is_file:
            print("enter 1 to update a file name")
            print("enter 2 to update while appending the data")
            print("enter 3 to completely overwrite the file")
            s=int(input("enter the number to proceed:- "))
            if s==1:
                name2=input("tell your new file name:-")
                p2=Path(name2)
                if not p2.exists():
                    p.rename(p2)
                    print("FILE RENAMED SUCCESSFULLY")
                else:
                    print("file name already exists" )
            if s==2:
                with open(p,"a") as fs:
                    data=input("Enter te data to be updated:- ")
                    fs.write(f"\n{data}")
                print("FILE UPDATED SUCCESSFULLY")
            if s==3:
                with open(p,"w") as fs:
                    data=input("Enter the data to be updated:- ")
                    fs.write(data)
                print("FILE OVERWRITTEN SUCCESSFULLY")

        elif p.is_dir:
            print("")
        else:
            print("file does not exist")
    except Exception as err:
        print(f"An error has coccured {err}")

def deletefile():
    try:
        readfileandfolder()
        name=input("which file u want to delete:- ")
        p=Path(name)
        if p.exists() and p.is_file:
            p.unlink()
            print("FILE DELETED SUCCESSFULLY")
        elif p.is_dir:
            print(f"{name} is a directory not a file and canot be deleted")

        else:
            print("file does not exist")
    except Exception as err:
        print("An error has occured as {err}")



print("press 1 for to create file")
print("press 2 for to read file")
print("press 3 for to upate file")
print("press 4 for to delete file")

a=int(input("enter number to process further:- "))
if a==1:
    createfile()
if a==2:
    readfile()
if a==3:
    updatefile()
if a==4:
    deletefile()
