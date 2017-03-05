import random

def main():
	n = random.randint(0,9999)
	y = input("enter your guess: ")
	while(y!=n):
		if(y<n):
			print("guesssed number too small, try another one !")
			y = input("new guess?")
		elif(y>n):
			print("guesssed number too large, try another one !")
			y = input("new guess?")
	if(y==n):
		print("boom! you guessed it right!")





if __name__ =='__main__':
	main()