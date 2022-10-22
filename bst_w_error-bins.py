BIN_RANGE = 16

class Node(object):
  def __init__(self):
    self.value = None
    self.left = None
    self.right = None
    self.bin = set()

  def insert(self, to_insert):
    if self.value is None:
      self.value = to_insert
      return
    elif self.value == to_insert:
      return
    if to_insert < self.value - BIN_RANGE:
      if self.left is None:
        self.left = Node()
      self.left.insert(to_insert)
    elif to_insert > self.value + BIN_RANGE:
      if self.right is None:
        self.right = Node()
      self.right.insert(to_insert)
    else:
      self.bin.add(to_insert)
      return

  def has(self, to_search):
    if self.value is None:
      return False
    if to_search == self.value:
      return True 
    if to_search < self.value - BIN_RANGE:
      return self.left.has(to_search)
    elif to_search > self.value + BIN_RANGE:
      return self.right.has(to_search)
    else:
        return to_search in self.bin

  def print_in_order(self):
    if self.value is None:
      return 
    if self.left:
      self.left.print_in_order()
    en_lst = []
    i = 0
    if len(self.bin) > 0: 
      en_lst = sorted(list(self.bin))
      while(i < len(en_lst) and en_lst[i] < self.value):
          print(en_lst[i])
          i += 1
    print(self.value)
    if(i < len(en_lst)):
        print(en_lst[i])
        i += 1
    if self.right:
      self.right.print_in_order()
      
      
  def is_valid(self):
    if self.value is None:
        return
    elif len(self.bin) != 0:
        for val in self.bin:
            if val > self.value + BIN_RANGE or val < self.value - BIN_RANGE:
                return False
    if self.left is not None:
        if self.left.value < self.value - BIN_RANGE:
            self.left.is_valid()
        else:
            return False
    if self.right is not None:
        if self.right.value > self.value + BIN_RANGE:
            self.right.is_valid()
        else:
            return False
    return True







  
