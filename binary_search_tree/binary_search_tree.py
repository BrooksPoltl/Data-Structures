class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = BinarySearchTree(value)
    if self.value == None:
      self.value = value
      return self
    else:
      current_node = self
      while 1 == 1:
        if node.value == current_node.value:
          return None
        if node.value < current_node.value:
          if current_node.left == None:
            current_node.left = node
            return self
          else: 
            current_node = current_node.left
        if node.value > current_node.value:
          if current_node.right == None:
            current_node.right = node
            return self
          else: 
            current_node = current_node.right

    

  def contains(self, target):
    current_node = self
    while 1 == 1:
      if current_node.value == target:
        return True
      elif target > current_node.value:
        current_node = current_node.right
      else: 
        current_node = current_node.left
      if current_node == None:
        return False
  def get_max(self):
    pass

  def for_each(self, cb):
    pass