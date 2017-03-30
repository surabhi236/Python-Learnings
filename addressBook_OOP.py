class addressBook:
	def __init__(self,name):
		self.name = name
		self.address = raw_input("enter address: ")
		self.phone = input("enter phone number")

def main():
	name = raw_input("enter record name: ")
	addressBook(name)
	c = True
	while(c==True):
		name = raw_input("enter record name: ")
		addressBook(name)
		prom = raw_input("want to add another ?")
		if(prom=="Yes" or prom =="yes" or prom=="y"):
			c = True
		else:
			c = False

if __name__ == "__main__":
	main()
