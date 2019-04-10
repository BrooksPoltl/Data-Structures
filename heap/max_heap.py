class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    max_value = self.storage[0]
    self.storage[0] = self.storage[len(self.storage)-1]
    self.storage.pop()
    self._sift_down(0)
    return max_value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[(index - 1) // 2], self.storage[index] = self.storage[index], self.storage[(index -1) // 2]
      index = (index - 1) // 2

  def _sift_down(self, index):
    length = len(self.storage)
    while 1 == 1:
      left_child_index = 2 * index + 1
      right_child_index = 2 * index + 2
      swap = None
      if left_child_index < length:
        left_child = self.storage[left_child_index]
        if left_child > self.storage[index]:
          swap = left_child_index
      if right_child_index < length:
        right_child = self.storage[right_child_index]
        if (swap == None and right_child > self.storage[index]) or (swap != None and right_child > left_child):
          swap = right_child_index
      if swap == None:
        break
      self.storage[swap], self.storage[index] = self.storage[index], self.storage[swap]
      index = swap