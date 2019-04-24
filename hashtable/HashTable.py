class HashTable(object):
    def __init__(self, size):

        # Set up sizes and slots and data
        self.size = size
        self.slots = [None]*size
        self.data = [None]*size

    def put(self, key, data):
        # Using only integer keys for ease of use

        # getting the hashvalue for hashfunction
        hashvalue = self.hashfunction(key, self.size)

        # if slot is empty
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        # if key already exist, replace old data
        elif self.slots[hashvalue] == key:
                self.data[hashvalue] = data
        # else find next available slot
        else:
            newhashvalue = self.rehash(hashvalue, self.size)
            while self.slots[newhashvalue]!=None:
                if self.slots[newhashvalue] == key:
                    break
                newhashvalue = self.rehash(newhashvalue, self.size)
                # if newhashvalue == hashvalue:
                #     raise Exception("Hash Table is Full")
            self.slots[newhashvalue] = key
            self.data[newhashvalue] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key):
        # Get item from a given key
        startslot = self.hashfunction(key, self.size)
        position = startslot

        while True:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position, self.size)

            if position == startslot:
                return None