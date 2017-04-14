import os

def rename_files():
	#1 get file names from a folder
	file_list = os.listdir(r"K:\Python\City-ud036-Python\ud036-L2-use functions\prank")		# r stands for raw path
	print(file_list)

	#2 for each file, rename filename

rename_files()