class Queue:
  def __init__(self, size = 0, storage = []):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    self.size += 1

  
  def dequeue(self):
    if self.size == 0:
      return None
    popped_item = self.storage.pop(0)
    self.size -= 1
    return popped_item

  def len(self):
    return self.size
