# first practise a HashMap

class HashMap:
    def __init__(self):
        self.size= 6
        self.map= [None] * self.size

    def get_hash_index(self, key):
        unicode_sum =0
        for ch in str(key):
            unicode_sum = unicode_sum + ord(ch)
        
        index = unicode_sum % self.size
        print(f"UniCodeSum: {unicode_sum} || index : {index}")
        return index
    
    def add(self, key, value):
        key_value_pair = [key,value]  
        
        list_index = self.get_hash_index(key)
        
        if self.map[list_index] is None:
            self.map[list_index] = list([key_value_pair])       # list() is used for making nested list
        else:
            for pair in self.map[list_index]:
                if pair[0]==key and pair[1]== value:
                    return True
            self.map[list_index].append(key_value_pair)
            
    def print_list(self):
        for pair in self.map:
            if pair is not None:
                # print(str(pair))
                print(pair)
                        
        

# h= HashMap()
# print(h.map)
# h.add("bob",1234)
# print(h.map)
# h.add("bob",200)
# print(h.map)
# h.print_list()

print(101/10000)