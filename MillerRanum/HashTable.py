# a Map abstract data type


class HashTable:
  def __init__(self):
    self.size = 11
    self.slots = [None]*self.size  # keys, or the hashtable
    self.data = [None]*self.size   # values

  def put(self, key, data):
    hashvalue = self.hashfunction(key, len(self.slots))

    if self.slots[hashvalue] == None:    # slot is empty
      self.slots[hashvalue] = key  
      self.data[hashvalue] = data
    else:
      if self.slots[hashvalue] == key:
        self.data[hashvalue] = data   # replace value
      else:
        nextslot = self.rehash(hashvalue, len(self.slots))
        while self.slots[nextslot] != None and self.slots[nextslot] != key:
          nextslot = self.rehash(nextslot, len(self.slots))

        if self.slots[nextslot] == None:   
          self.slots[nextslot] = key
          self.data[nextslot] = data
        else:
          self.data[nextslot] = data       # replace

  def hashfunction(self, key, size):  # remainder method
    return key%size

  def rehash(self, oldhash, size):    # open addressing
    return (oldhash + 1)%size


  def get(self,key):  # using linear probing
    startslot = self.hashfunction(key,len(self.slots))

    data = None
    stop = False
    found = False
    position = startslot
    while self.slots[position] != None and not found and not stop:
      if self.slots[position] == key:
         found = True
         data = self.data[position]
      else:
         position=self.rehash(position,len(self.slots))
         if position == startslot:
            stop = True
    return data

  def __getitem__(self,key):  # to use [ ] 
      return self.get(key)

  def __setitem__(self,key,data):   # to use [ ]
    self.put(key,data)  


H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print H.slots

print H.data

print H[20]

print H[17]

H[20] = 'duck'
print H[20]

print H[99]

H.put(25, 'bear')
print H.data







