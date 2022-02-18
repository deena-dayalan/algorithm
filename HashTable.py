class HashTable():
    def __init__(self,m):
        self.m = m
        self.array = [None] * self.m
        self.n = 0

    def gethash (self,key):
        ###Multiplication method of hashing###
        asciis = [ord(key[i]) * (31 ** i ) for i in range(len(key))]
        hashValue=sum(asciis) % self.m
        return hashValue

    ### simple hash fucntion### for testing
    #def gethash (self,key):
    #    asciis = [ord(key[i]) for i in range(len(key))]
    #    hashValue=sum(asciis) % self.m
    #    return hashValue
    
    def getsize(self, number, cap):
        max = num =number
        n = cap + 1
        while number and n >= num:
            if all(n % d for d in range(2, int(n ** 0.5 + 1))):
                if (max < n):
                    max=n
                number -= 1
            n -= 1
        return max
    
    def  rehash(self):
        print("Rehasing to size %d started" % self.m)
        ### taking copy of original array###
        temp = self.array
        ### initailizing the array and size ###
        self.array = [None] * self.m
        self.n = 0
        for i in range(len(temp)):
            node = temp[i]
            while node != None:
                k = node.getkey()
                v = node.getvalue()
                self.insert(k,v)
                node = node.next
        print("Rehasing completed")

    def insert(self,key,value=1):
        #print("Inserting key:value ",key+":"+str(value))
        index = self.gethash(key)
        #print("INDEX: ",index)
        if self.array[index] == None:
            #print("SLOT empty")
            node=Node()
            node.setkey(key)
            node.setvalue(value)
            self.array[index] = node
            self.n = self.n + 1
        else:
            #print("SLOT non-empty")
            node = self.array[index]
            while node is not None:
                if key == node.getkey():
                    node.setvalue(node.getvalue()+1)
                    #self.n = self.n + 1
                    return
                node=node.getnext()
            node=Node()
            node.setvalue(value)
            node.setkey(key)
            node.setnext(self.array[index])
            self.array[index] = node
            self.n = self.n + 1
        loadfactor = self.n / self.m
        #print("loadfactor: ",loadfactor)
        if loadfactor >= 0.8:
            ###Table doubling###
            self.m=self.getsize(self.m, 2*self.m)
            self.rehash()

    def delete(self,key):
        print("Deleting key: [%s] in HashTable" % key)
        #self.n = self.n -1
        idx = self.gethash(key)
        #print("index: ",idx)
        if self.array[idx] == None:
            #print("Key not found in HT")
            return
        node = self.array[idx]
        if node.getkey() == key:
            #print("Key found at location HT[%s]" % str(idx))
            #print(node.getkey()+":"+str(node.getvalue()))
            self.array[idx] = node.getnext()
            self.n = self.n -1
            return
        prevnode = None
        while node != None:
            if node.getkey() == key:
                #print("Key found at location HT[%s]" % str(idx))
                #print(node.getkey()+":"+str(node.getvalue()))
                prevnode.setnext(node.getnext())
                self.n = self.n -1
                return
            prevnode = node
            node = node.getnext()
        print("Key not found in HT")
    
    def increase(self,key):
        print("Increasing key: [%s] in HashTable" % key)
        idx = self.gethash(key)
        node = self.array[idx]
        while node != None:
            if node.getkey() == key:
                print("Key found at location HT[%s]" % str(idx))
                print(node.getkey()+":"+str(node.getvalue()))
                node.setvalue(node.getvalue()+1)
                print(node.getkey()+":"+str(node.getvalue()))
                return
            node = node.getnext()
        print("Key not found in HT")

   
    def find(self,key):
        print("Finding key: [%s] in HashTable" % key)
        idx = self.gethash(key)
        print("Hash [%s] : "% key,idx)
        node = self.array[idx]
        while node != None:
            if node.getkey() == key:
                print("Key found at location HT[%s]" % str(idx))
                print(node.getkey()+":"+str(node.getvalue()))
                return
            node = node.getnext()
        print("Key not found in HT")

    def listAllKeys(self):
        print("Listing all the keys in HashTable")
        for i in range(self.m):
            node = self.array[i]
            while node != None:
                print(node.getkey())
                #print(node.getkey()+":"+str(node.getvalue()))
                node = node.getnext()
    def writeKeyValue(self):
        print("Printing all the keys and values in HashTable to file")
        f = open("problem1_result.txt", "w")
        for i in range(self.m):
            node = self.array[i]
            while node != None:
                #print(node.getkey())
                #print(node.getkey()+":"+str(node.getvalue()))
                f.write(node.getkey() + ":" + str(node.getvalue()) + "\n")
                node = node.getnext()
        f.close()

            

class Node:
    def __init__(self, value = None, key=None, next = None):
        self.value = value
        self.key = key
        self.next = next

    def getvalue(self):
        return self.value

    def setvalue(self, value = None):
        self.value = value

    def getkey(self):
        return self.key

    def setkey(self, key = None):
        self.key = key

    def getnext(self):
        return self.next

    def setnext(self, node = None):
        self.next = node

if __name__ == "__main__":
    ht = HashTable(13)
    with open("C:\\Users\\d.dasarathan\\OneDrive - Northeastern University\\Documents\\CS5800-Algo\\HW-8\\alice_in_wonderland.txt") as f:
        #lines = f.readlines()
        lines = list(line for line in (l.strip() for l in f) if line)
    #punctuation= '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    punctuation= '''!()[]{};:'"\, <>./?#$%^&*_~'''
    emptystring=""
    for line in lines:
        for word in line.split():
            for x in punctuation:
                word = word.replace(x,emptystring)
            #print(word)
            ht.insert(word.lower())
    ht.writeKeyValue()
    ht.delete("Deena")
    ht.listAllKeys()
    ht.delete("that")
    ht.listAllKeys()
    ht.increase("that")
    ht.find("that")
    ht.increase("thought")
    ht.find("thought")
        