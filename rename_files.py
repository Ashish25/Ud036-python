import os

def rename_files():
    #1 get file names from a folder
    file_list = os.listdir(r"K:\Python\City-ud036-Python\ud036-L2-use functions\prank")     # r stands for raw path
    print(file_list)
    saved_path = os.getcwd()
    print("current Working Directory is "+saved_path)
    os.chdir(r"K:\Python\City-ud036-Python\ud036-L2-use functions\prank")
    #2 for each file, rename filename
    for file_name in file_list:
            print("old Name - "+file_name)
            print("New Name - "+file_name.translate(None, "0123456789"))
            os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
