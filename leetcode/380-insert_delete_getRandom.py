import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        # update list and dict with the new value
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        
        val_index = self.dict[val]        # get index of value to be removed
        last_element = self.list[-1]      # get last element
        
        self.list[val_index] = last_element # move last index to position where value needs to be removed
        self.dict[last_element] = val_index # update index of the last element to the position of the value to be removed
        
        # remove val from the list and dict
        self.list.pop()
        del self.dict[val]
        
        return True
            
    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()