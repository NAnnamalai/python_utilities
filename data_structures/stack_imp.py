class StackImp:

	def __init__(self):
		print "-------------------------"
		print " Intiliazing ... "
		print "-------------------------"
		self.items = []

	def push(self, value):
		print "-------------------------"
		print " Pushing Value ", value
		print "-------------------------"
		self.items.append(value)

	def pop(self):
		print "-------------------------"
		print " Popping value "
		print  self.items.pop()
		print "-------------------------"

	def is_empty(self):
		print "-------------------------"
		print " Empty Check "
		print (self.items == [])
		print "-------------------------"

	def size(self):
		print "-------------------------"
		print " Stack Size "
		print len(self.items)
		print "-------------------------"
		

	def display(self):
		print "-------------------------"
		print " Stack Display "
		if len(self.items):
			for item in self.items[::-1]:
				print item
		print "-------------------------"


myStack = StackImp()

myStack.push("Hello")
myStack.push("and")
myStack.push("Welcome")
myStack.display()

myStack.pop()
myStack.display()

myStack.pop()
myStack.display()

myStack.size()