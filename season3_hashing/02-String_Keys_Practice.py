"""There is a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        # Out hash table is a list which holds 10000 elements with "None" initial value  
        self.table = [None]*10000
        
    # This function stores a string in its correct place in our hash table
    def store(self, string):
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                self.table[hash_value].append(string)
            else:
                self.table[hash_value] = [string]

    # This function looks up for a key in hash table
    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                if string in self.table[hash_value]:
                    return hash_value
        return -1

    # This is our hash function which is the core of our Hashing
    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 6865 because 68 * 100 + 65 = 6800 + 65 = 6865
print(hash_table.calculate_hash_value('DATA_STRUCTURE'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('DATA_STRUCTURE'))

# Test store
hash_table.store('DATA_STRUCTURE')
# Should be 6865
print(hash_table.lookup('DATA_STRUCTURE'))

# Test store edge case
hash_table.store('DATA_STRUCTURE')
# Should be 6865
print(hash_table.lookup('DATA_STRUCTURE'))

# Look at the output printed on your screen you will see a pair ..., None, ['DATA_STRUCTURE', 'DATA_STRUCTURE'], None, ... 
print(hash_table.table)
# It shows that store function appends the repeated request to the same place because:
# It is possible to have several strings which start with "DA" and it is logical
# like following 

hash_table.store('DATA')
