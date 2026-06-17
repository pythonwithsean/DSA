class Heap:
	def __init__(self):
		self.size = 0
		self.items = []

	def peek(self):
		if self.size == 0:
			raise Exception("No Element in Heap")
		return self.items[0]

	def poll(self):
		if(len(self.items) == 0):
			raise Exception("No Element in Heap")
		item = self.items[0]
		self.items[0] = self.items[-1]
		self.size -= 1
		self.heapifyDown()
		self.items.pop()
		return item

	def add(self,item):
		self.items.append(item)
		self.size += 1
		self.heapifyUp()

	def heapifyDown(self):
		index = 0
		# while there is a left child
		while ((index * 2) + 1) < (len(self.items) - 1) and self.items[(index * 2) + 1]:
			# smaller child will be the left child
			smallerChildIndex = ((index * 2) + 1)
			# if there is a right child and the right child is smaller than the left child then the smallest should be the right
			if ((index * 2) + 2) < (len(self.items) - 1) and self.items[(index * 2) + 2] < self.items[(index * 2) + 1]:
				smallerChildIndex = (index * 2) + 2
			if self.items[index] < self.items[smallerChildIndex]:
				break
			else:
				self.items[index],self.items[smallerChildIndex] = self.items[smallerChildIndex], self.items[index]
			index = smallerChildIndex

	def heapifyUp(self):
		lastElementIndex = len(self.items)
		while self.items[(lastElementIndex - 2 // 2)] and self.items[(lastElementIndex -2) // 2] > self.items[lastElementIndex -1]:
			self.items[(lastElementIndex -2) // 2], self.items[lastElementIndex -1] = self.items[lastElementIndex - 1], self.items[(lastElementIndex -2) // 2]
			lastElementIndex = (lastElementIndex - 2) // 2


h = Heap()
h.add(2)
h.add(1)
print(h.items)
print(h.poll())
print(h.items)
print(h.poll())
print(h.items)
print(h.poll())
