import glob, os

def exitsfile_rename():
	file= os.listdir(r"/Users/thanh/Pictures")
	saved_path= os.getcwd()
	os.chdir(r"/Users/thanh/Pictures")
	for file_name in file:
		if file_name.startswith("q"):
			os.rename("q.jpg", "abc.jpg")
			print ("success")
	#os.chdir(saved_path)
	else:
		print("try again")

exitsfile_rename()
