# Mini-project: Take A Break. 

#Plan the steps to execute "Take a break" program:
#Repeat N times 
# Sleep time= waiting for some hours to play video
#open browser


import time
import webbrowser
total_breaks= 3
count_break= 0

print("Hey, take a break " +time.ctime())
while (count_break < total_breaks):
	time.sleep(100)
	webbrowser.open("https://www.youtube.com/watch?v=0yW7w8F2TVA")
	count_break= count_break+1




