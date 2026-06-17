import sys 

q = [None] * (20)
front = len(q) - 1
back = len(q) - 1

def enqueue(val): 
	global back
	back = (back + 1) % (len(q))
	q[back] = val
def dequeue(): 
	global front
	front = (front + 1) % (len(q))
	q[front] = None
def peek(): 
	global front
	global back
	if front == back: 
		return "Empty"
	return q[(front + 1) % len(q)] if q[(front + 1) % len(q)] != None else "Empty"

enqueue(100)
enqueue(99)
enqueue(150)
dequeue()
dequeue()
dequeue()
print(peek())
