import sys

class HashMap:
    def __init__(self, size):
        self.maxSize = size
        self.arr = []
        self.size = 0

    def insert(self, key, value):
        if self.size == self.maxSize:
            print ("Max capacity reached for hashtable")
            return

        for i in range(0, self.size):
            pair = self.arr[i]
            if pair[0] == key:
                pair[1].append(value)
                return
        pair = [key, [value]]
        self.arr.append(pair)
        self.size += 1
        return

    def getKey(self, key):
        if self.size == 0:
            print ("No keys in the hashtable")
            return None

        for i in range(0, self.size):
            pair = self.arr[i]
            if pair[0] == key:
                return pair[1]

        return None

    def removeKey(self, key):
        if self.size == 0:
            print ("No keys in the hashtable")
            return None

        for i in range(0, self.size):
            pair = self.arr[i]
            if pair[0] == key:
                self.arr.pop(i)
                self.size -= 1
                return

    def display(self):
        if self.size == 0:
            print ("No keys in the hashtable")
            return None

        for i in range(0, self.size):
            pair = self.arr[i]
            print pair

    def getSize(self):
        return self.size

    def checkEmpty(self):
        if self.size == 0:
            return True
        return False

    def clear(self):
        for i in range(0, self.size):
            del self.arr[i]
        self.arr = []
        self.size = 0

h = HashMap(100)
h.insert(1,2)
h.insert(1,3)
h.insert(5,6)
h.insert(8,9)
h.display()
print "\n"
print h.getKey(1)
h.removeKey(1)
h.removeKey(8)
print "\n\n"
h.display()
