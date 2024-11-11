import os
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
else:
    print("file not found")


# create

    foldername=input("enter foldername:")
    filename=input("enter filename:")
    os.mkdir(foldername)
    f=open(foldername+"/"+filename,'x')

# delete
    os.rmdir("j")