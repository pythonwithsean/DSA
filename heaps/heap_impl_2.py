# Min heap Implementation
class Heap:

  def __init__(self):
    self._heap = []

  # Left Child 2 * i + 1
  # Return the index of the left child
  def left_child(self,index):
    return 2 * index + 1

  def inBounds(self,index):
    return index >= 0 and index < len(self._heap)

  # Right Child 2 * i + 2
  # Return the index of the right child
  def right_child(self,index):
    return 2 * index + 2

  # Parent Child (i - 1) // 2
  # Return Index of parent
  def parent(self, index):
    if index < 0 or index >= len(self._heap):
      raise Exception("Illegal Exception")
    return (index - 1) // 2

  def insert(self, item):
    self._heap.append(item)
    self.heapify_up(len(self._heap) - 1)

  # Ensures Min heap invariant by ensuring the any node K is >= its children
  def heapify_up(self,index):
    # while we are not at the top and we are smaller than our parent then we bubble up
    while index != 0 and self._heap[self.parent(index)] > self._heap[index]:
      self._heap[self.parent(index)], self._heap[index] = self._heap[index],self._heap[self.parent(index)]
      index = self.parent(index)

  def peek(self):
    if self.is_empty(): return None
    return self._heap[0]
  def is_empty(self):
    return len(self._heap) == 0

  def poll(self):
    if self.is_empty():
      return None
    smallest = self._heap[0]
    last = self._heap.pop()
    # if it is empty after pop then there is only 1 node just return the tmp
    if self.is_empty():
      return smallest
    # there is more than 1 node so heapify down
    self._heap[0] = last
    self.heapify_down()
    return smallest

  def heapify_down(self,index=0):
    while self.inBounds(2 * index + 1) or self.inBounds(2 * index + 2):
       left_value = self._heap[self.left_child(index)] if self.inBounds(2 * index + 1) else float("inf")
       right_value = self._heap[self.right_child(index)] if self.inBounds(2 * index + 2) else float("inf")
       smallest = min(left_value, right_value)
       if(self._heap[index] > smallest):
        if left_value <= right_value:
          self._heap[index],self._heap[self.left_child(index)] = self._heap[self.left_child(index)],self._heap[index]
          index = self.left_child(index)
        else:
          self._heap[index], self._heap[self.right_child(index)] = self._heap[self.right_child(index)],self._heap[index]
          index = self.right_child(index)
       else:
         break

heap = Heap()
heap.insert(50)
heap.insert(2)
print(heap.peek())
