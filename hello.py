class Employee:
	def __init__(self,name,age,company):
		self.name = name
		self.age = age
		self.company = company
	def help(self):
		print(f"hello {self.name}. Your Current Employer is {self.company} ")
	def show_salary(self):
		if self.company == "Shell":
			return(12000)
		if self.company  == "Reliance":
			return(10000)
Employee1 = Employee("vyshnavps",21,"Shell")
Employee2 = Employee("Vishnu",21,"Reliance")
Employee1.help()
salary1 = Employee1.show_salary()
salary2 = Employee2.show_salary()
print(f"Hi {Employee1.name}, Your salary is {salary1}")
print(f"Hi {Employee2.name}, Your salary is {salary2}")
