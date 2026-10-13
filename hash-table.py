# Build a Hash Table
# build a hash table from scratch. A hash table is a data structure that stores key-value pairs. A hash table works by taking the key as an input and then hashing this key according to a specific hashing function.
# the hashing function will be simple: it will sum the Unicode values of each character in the key. The hash value will then be used as the actual key to store the associated value. The same hash value would also be used to retrieve and delete the value associated with the key.

class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string):
        return sum(ord(char) for char in string)
    
    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value

    
    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]
    
    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key)
        return None
        


