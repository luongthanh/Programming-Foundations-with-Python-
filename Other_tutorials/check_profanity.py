#--- In order to check curse words in a file, I prepare a badword.txt file which includes the list of curse words. 

#import urllib
import os 

def check_profanity():
	bad_word= open("/Users/thanh/Movies/Other_tutorials/bad_word.txt")
	word = bad_word.read()
	#for word in bad_word():
	bad_word.close()
	return word

word = check_profanity()
def read_text():
	# You can paste local address of a random file in your computer. 
	quotes = open("/Users/thanh/Movies/Other_tutorials/file_to_compare.rtf")
	file_content= quotes.read()
	quotes.close()
	#each_word= file_content.split()
	#print(file_content)
	for each_word in file_content:
		if each_word in word:
			print (each_word)
			return
	print("Not anyword")

read_text()
