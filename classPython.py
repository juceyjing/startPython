#-*- coding:UTF-8 -*-
class Employee(object):
	"""docstring for Employee"""
	'所有员工的基类'
	empCount =0
	def __init__(self, name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount +=1

		def displayCount(self):
			print "Total Employee %d" % Employee.empCount

		def displayEmployee(self):
			print "elf.name,",SName:",salary:",self.salary

		super(Employee, self).__init__()
		self.arg = arg
