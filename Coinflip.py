import random

class Node():
    def __init__(self, key, level):
        self.key = key
        self.forward = [None]*(level+1)

class SkipList(object):
    def __init__(self, max_lvl, P):
        self.max = max_lvl
        self.P = P
        self.head = self.createNode(self.max, -1)
        self.level = 0
    
    def createNode(self, lvl, key):
        n = Node(key, lvl)
        return n
    
    def randomLevel(self):
        lvl = 0
        while random.random()<self.P and lvl<self.max:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None]*(self.max+1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current == None or current.key != key:
            rlevel = self.randomLevel()

            if rlevel > self.level:
                for i in range(self.level+1, rlevel+1):
                    update[i] = self.head
                self.level = rlevel

            n = self.createNode(rlevel, key)

            for i in range(rlevel+1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

            print("INSERT Success {}".format(key))
    
    def delete(self, search_key):
        update = [None]*(self.max+1)
        current = self.head
        for i in range(self.level, -1, -1):
            while(current.forward[i] and current.forward[i].key < search_key):
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current != None and current.key == search_key:
            for i in range(self.level+1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            while(self.level>0 and self.head.forward[self.level] == None):
                self.level -= 1
            print("Successfully deleted {}".format(search_key))
  
    def search(self, key):
        current = self.head
        for i in range(self.level, -1, -1):
            while(current.forward[i] and current.forward[i].key < key):
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            print("Found key ", key)

    def printList(self):
        head = self.head
        for lvl in range(self.level+1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.forward[lvl]
            while(node != None):
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")

if __name__ == "__main__":
    lst = SkipList(3, 0.5)
    lst.insert(3)
    lst.insert(6)
    lst.insert(7)
    lst.insert(9)
    lst.insert(12)
    lst.insert(19)
    lst.insert(17)
    lst.insert(26)
    lst.insert(21)
    lst.insert(25)
    lst.printList()
    
    lst.search(19)
    lst.delete(21)

    lst.printList()

