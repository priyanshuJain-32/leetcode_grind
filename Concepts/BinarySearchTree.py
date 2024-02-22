class Tree:
	
	# Constructor
	def __init__(self, initval=None):
		self.value = initval
		if self.value:
			self.left = Tree()
			self.right = Tree()
		else:
			self.left = None()
			self.right = None()
		return
	
	# Check empty
	def isempty(self):
		return self.value == None
	
	# Check leaf
	def isleaf(self):
		return self.value != None and self.left.isempty() and self.right.isempty()
	
	# Inorder
	def inorder(self):
		if self.isempty():
			return []
		return self.left.inorder() + [self.value] + self.right.inorder()
	
	# Preorder
	def preorder(self):
		if self.isempty():
			return []
		return [self.value] + self.left.preorder() + self.right.preorder()
	
	# Postorder
	def postorder(self):
		if self.isempty():
			return []
		return self.left.postorder() + self.right.postorder() + [self.value]
	
	# Min Depth
	def mindepth(self):
		if self.isempty():
			return 0
		left = self.left.mindepth()
		right = self.right.mindepth()
		if self.left.isempty() and self.right.isempty():
			return 1
		if self.left.isempty():
			return 1 + right
		if self.right.isempty():
			return 1 + left
		return min(left, right) + 1
	
	# Max Depth
	def maxdepth(self):
		if self.isempty():
			return 0
		left = self.left.maxdepth() + 1
		right = self.right.maxdepth() + 1
		return max(left, right)
	# Print
	def __str__(self):
		return str(self.inorder())
	
	# Find
	def find(self, v):
		if self.isempty():
			return False
		if self.value == v:
			return True
		if self.value>v:
			return self.left.find(v)
		if self.value<v:
			return self.right.find(v)
	
	# Minimum
	def minimum(self):
		if self.left.isempty():
			return self.value
		return self.left.minimum()
	
	# Maximum
	def maximum(self):
		if self.right.isempty():
			return self.value
		return self.right.maximum()
	
	# Insert
	def insert(self, v):
		if self.isempty():
			self.value = v
			self.left = Tree()
			self.right = Tree()
		if self.value == v:
			return
		if self.value > v:
			self.left.insert()
			return
		if self.value < v:
			self.right.insert()
			return
	
	# Make empty
	def makeempty(self):
		self.value = None
		self.left = None
		self.right = None
		return

	# Copy left
	def copyleft(self):
		self.value = self.left.value
		self.left = self.left.left
		self.right = self.left.right
	
	# Copy right
	def copyright(self):
		self.value = self.right.value
		self.left = self.right.left
		self.right = self.right.right
	
	# Delete
	def delete(self,v):
		if self.isempty():
			return
		if self.value > v:
			self.right.delete(v)
			return
		if self.value < v:
			self.left.delete(v)
			return
		if self.value == v:
			if self.isleaf():
				self.makeempty()
			elif self.left.isempty():
				self.copyright()
			elif self.right.isempty():
				self.copyleft()
			else:
				self.value = self.left.maximum()
				self.left.delete(self.left.maximum())
			return