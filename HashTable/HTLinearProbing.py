class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def set(self, key, val):
        h = self.get_hash(key)
        #if hash idex occupies space
        if self.arr[h] is not None:
            
        #if hash idx does not occupy space
        else:
            self.arr[h] = val    
    
    def delete(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

    def print_hash(self):
        for i in self.arr:
            print(i)

if __name__ == '__main__':
    t = HashTable()
    t.print_hash()