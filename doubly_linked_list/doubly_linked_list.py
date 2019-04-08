"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1
    return self
  
  def remove_from_head(self):
    if self.length == 0:
      return None
    head_node = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = head_node.next
      self.head.prev = None
    self.length -= 1
    return head_node.value

  def add_to_tail(self, value):
    new_node = ListNode(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return self

  def remove_from_tail(self):
    if self.head == None:
      return None
    pop_node = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = pop_node.prev
      self.tail.next = None 
    self.length -= 1
    return pop_node.value
  def move_to_front(self, node):
    if self.head == node:
      return node.value
    if self.tail == node:
      self.tail = node.prev
      node.next = self.head
      self.tail.next = None
      self.head = node
    else:
      node.prev.next = node.next
      node.next.prev = node.prev
      node.prev = None
      self.tail.prev = node
      node.next = self.head
      self.head = node
    return self.head.value

  def move_to_end(self, node):
    if self.tail == node:
      return node.value
    if self.head == node:
      self.head = node.next
      node.prev = self.tail
      self.tail.next = node
      self.tail = node
    else:
      node.prev.next = node.next
      node.next.prev = node.prev
      node.next = None
      self.tail.next == node
      node.prev = self.tail
      self.tail = node
    return self.tail.value
  def delete(self, node):
    if self.length == 0:
      return None
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      if self.head == node:
        self.head = node.next
      elif self.tail == node:
        self.tail = node.prev 
      else:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    self.length -= 1
    return 1
  def get_max(self):
    max_value = self.head.value
    current_node = self.head
    if self.length == 1:
      return max_value
    while current_node.next != None:
      if current_node.value > max_value:
        max_value = current_node.value
      current_node = current_node.next 
    if current_node.value > max_value:
      return current_node.value
    return max_value

