class robot:
	population = 0
	def __init__(self, name):
		self.name = name
		print("(Initializing {})".format(self.name))
		robot.population +=1

	def die(self):
		print("{} is being destroyed! ".format(self.name))
		robot.population -=1
		if(robot.population ==0):
			print("{} was the last one.".format(self.name))
		else:
			print("There are still {:d} robots working.".format(robot.population))

	def say_hi(self):
		print("greetngs, my master calls me {}.".format(self.name))

	@classmethod

	def how_many(cls):
		print("we have {:d} robots.".format(cls.population))


droid1 = robot("R2-D2")
droid1.say_hi()
robot.how_many()

droid2 = robot("C-3PO")
droid2.say_hi()
robot.how_many()

print("robots can do some work here. \n")

print("robots have finished their work, so let's destroy them")

droid1.die()
droid2.die()

robot.how_many()
