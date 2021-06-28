class Node:
  def __init__(self, data=None):
      self.data = data
      self.next = None
  
  def __str__(self):
      return f"{self.data}"
   
class Linked_list:
  def __init__(self):
    self.head = None
  def insert (self, data=None):
    new_node = Node(data)
    if self.head :
      new_node.next = self.head 
    self.head = new_node

  def includes(self,val):
    current = self.head 
    is_include = False
    while (current):
        if current.data == val :
            is_include = True
        current = current.next
    return is_include
      

  def __str__(self):
    output = ""

    current = self.head
    while current:
      output += "{%s} -> " %(current.data,)
      current = current.next
    output += " NULL"
    return output
  

if __name__ == "__main__":
  linked = Linked_list()
  linked.insert(1)
  linked.insert(2)
  linked.insert(3)
  print(linked)
  print(linked.includes(4),linked.includes(5),linked.includes(6))