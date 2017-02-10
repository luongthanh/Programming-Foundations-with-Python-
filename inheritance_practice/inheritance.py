class Parent():
	def __init__(self, lastname, bloodtype):
		print("Parent Constructor Called")
		self.lastname = lastname
		self.bloodtype= bloodtype 

	def show_info(self):
		print("The last name is " +self.lastname)
		print("The blood type is " +self.bloodtype) 
#billy_cyrus= Parent("Walker", "AB") 
#print(billy_cyrus.bloodtype) 

class Child(Parent):
	def __init__ (self, lastname, bloodtype, age):
		#print("Chidren Constructor Called")
		Parent.__init__(self, lastname, bloodtype) 
		#Parent.show_info(self) 
		self.age= age 
alan_walker= Child("Alan", "A", 12)

#print(alan_walker.age)
#print(alan_walker.bloodtype) 
alan_walker.show_info()  
	

		
	
	