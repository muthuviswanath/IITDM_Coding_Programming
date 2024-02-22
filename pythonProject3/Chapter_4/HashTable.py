class Hashtable:

    def __init__(self,size):
        self.size = size
        self.hashtable = {}
        for i in range (size):
            self.hashtable[i] = []

    def hash_function(self,key):
        return key % self.size

    def store_data(self,key,value):
        cell = self.hashtable[self.hash_function(key)]
        if value not in cell:
            cell.append(value)
    def get_data(self,key):
        return self.hashtable[self.hash_function(key)]

    def remove_data(self,key,value):
        cell = self.hashtable[self.hash_function(key)]
        if value in cell:
            cell.remove(value)
        else:
            print("Value not found")

My_HashTable = Hashtable(16)
names = ["MESSI","ABD","KALAM","SHREYA","ROHIT","LOKI","VIRAT","RONALDO"]
for values in names:
    key = sum(map(ord,values))
    My_HashTable.store_data(key,values)
    print(My_HashTable.get_data(key),key%My_HashTable.size)

My_HashTable.remove_data(303,"LOKI")
for value in names:
    key= sum(map(ord,value))
    print(My_HashTable.get_data(key))

