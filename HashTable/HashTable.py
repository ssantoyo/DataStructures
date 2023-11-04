class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        # self.arr = [None for i in range(self.MAX)] Does not avoid collisions
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def add(self, key, val): #__setitem__
        h = self.get_hash(key)
        found = False
        #checking if there is more then one element in hash idx
        for idx, element in enumerate(self.arr[h]):
            #element already exist; update it
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        
        #key does not exist in the linked list; add it
        if not found:
            self.arr[h].append((key,val))

    def get(self, key): #__getitem__
        h = self.get_hash(key)
        for element in self.arr[h]:
            #check the keys in the linked list
            if element[0] == key:
                return element[1]
    
    def delete(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
     
    def print_hash(self):
        for i in self.arr:
            print(i)


if __name__ == '__main__':
    t = HashTable()
    print(t.get_hash("march 6"))
    print(t.get_hash("march 17"))
    # t.add("march 6", 130)
    # t.add("march 22", 110)
    # t.add("march 1", 20)
    # t.add("march 5", 5)
    # t.get("march 6")
    # t.get("march 22")
    # t.get("march 1")
    # t.get("march 5")
    # t.print_hash()
    # print(" ")
    # t.delete("march 6")
    # t.print_hash()
    
