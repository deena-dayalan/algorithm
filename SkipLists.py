import random

class Node():
	def __init__(self, key=None, level=0):
		self.key = key
		self.next = [None]*(level+1)

class SkipList():
	def __init__(self, max_lvl):
		self.max = max_lvl
		self.head = self.createNode(self.max, -1)
		self.level = 0
	
	def createNode(self, lvl, key):
		n = Node(key, lvl)
		return n
	
	def tossCoin(self):
		heads = 0
		while random.randint(0,1) and heads <= self.max:
			heads += 1
		return heads

	def insert(self, key):
		print("Inset start")
		update = [None]*(self.max+1)
		current = self.head

		for i in range(self.level, -1, -1):
			while current.next[i] and current.next[i].key < key:
				current = current.next[i]
			update[i] = current
		
		current = current.next[0]

		if current == None or current.key != key:
			rlevel = self.tossCoin()

			if rlevel > self.level:
				for i in range(self.level+1, rlevel+1):
					update[i] = self.head
				self.level = rlevel

			n = self.createNode(rlevel, key)

			for i in range(rlevel+1):
				n.next[i] = update[i].next[i]
				update[i].next[i] = n

			print("INSERT Success {}".format(key))
	
	def delete(self, search_key):
		update = [None]*(self.max+1)
		current = self.head
		for i in range(self.level, -1, -1):
			while(current.next[i] and current.next[i].key < search_key):
				current = current.next[i]
			update[i] = current
		current = current.next[0]
		if current != None and current.key == search_key:
			for i in range(self.level+1):
				if update[i].next[i] != current:
					break
				update[i].next[i] = current.next[i]
			while(self.level>0 and self.head.next[self.level] == None):
				self.level -= 1
			print("Delete Success {}".format(search_key))
  
	def search(self, key):
		current = self.head
		for i in range(self.level, -1, -1):
			while(current.next[i] and current.next[i].key < key):
				current = current.next[i]
		current = current.next[0]
		if current and current.key == key:
			print("Found key ", key)

	def printList(self):
		head = self.head
		for lvl in range(self.level+1):
			print("Level {}: ".format(lvl), end=" ")
			node = head.next[lvl]
			while(node != None):
				print(node.key, end=" ")
				node = node.next[lvl]
			print("")

if __name__ == "__main__":
	lst = SkipList(4)
	lst.insert(9)
	lst.insert(3)
	lst.insert(17)
	lst.insert(12)
	lst.insert(7)
	lst.insert(6)
	lst.insert(25)
	lst.insert(19)
	lst.insert(26)
	lst.insert(21)

	lst.printList()
	
	lst.search(19)
	lst.delete(21)

	lst.printList()

