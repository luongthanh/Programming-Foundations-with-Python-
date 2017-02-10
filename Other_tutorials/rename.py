#This program is to do: rename the files in folder /Users/thanh/Pictures by excluding the number in file's name. 

import os 


def rename_file():
#get file name from a folder 
	file_list= os.listdir(r"/Users/thanh/Pictures")
	#print(file_list)
	saved_path= os.getcwd()
	#print("You are working directly in folder " +saved_path)
	os.chdir(r"/Users/thanh/Pictures")
#for each file, rename file name.
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)
rename_file()

