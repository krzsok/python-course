import random
 
class RandomQueue:

    def __init__(self):
      self.dict = {}

    def insert(self, item):
      self.dict.update{item:item}

    def remove(self):   # zwraca losowy element
      return self.dict.pop(random.choice(self.dict.keys())) #tylko python 2.7
      
    def is_empty(self):
      return len(self.dict) == 0
      
    def is_full(self):
      return False

