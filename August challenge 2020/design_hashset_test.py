class Bucket:
    def __init__(self):
        self.bucket=[]
      
    def update(self, key):
        found=False
        for i,k in enumerate(self.bucket):
            if key==k:
                self.bucket[i]=key
                found=True
                break
        if not found:
            self.bucket.append(key)
   
    def get(self, key):
        for k in self.bucket:
            if k==key:
                return True
        return False
   
    def remove(self, key):
        for i,k in enumerate(self.bucket):
            if key==k:
                del self.bucket[i]

################# Hash Set Class ################################    

class MyHashSet:
   def __init__(self):
        self.key_space = 2096
        self.hash_table=[Bucket() for i in range(self.key_space)]
      
   def add(self, key):
        hash_key=key%self.key_space
        self.hash_table[hash_key].update(key)
      
   def remove(self, key):
        hash_key=key%self.key_space
        self.hash_table[hash_key].remove(key)
      
   def contains(self, key):
        hash_key=key%self.key_space
        return self.hash_table[hash_key].get(key)
  
ob = MyHashSet()
ob.add(1)
ob.add(3)
print(ob.contains(1))
print(ob.contains(2))
ob.add(2)
print(ob.contains(2))
ob.remove(2)
print(ob.contains(2))