class Student:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def help(self):
		print(f"hello {self.name} ")
student1 = Student("vyshnav",21)
student1.help()
