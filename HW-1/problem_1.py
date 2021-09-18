class Node:
    """
    A class for a node in a singly-linked list, storing
    a data payload and links to next node.
    """

    def __init__(self, data = None, next = None):
        """Initialize the node with data payload and link to next node."""
        self.data = data
        self.next = next

    def getdata(self):
        """Get the node's data payload."""
        return self.data

    def setdata(self, data = None):
        """Set the node's data payload."""
        self.data = data

    def getnext(self):
        """Get the next linked node."""
        return self.next

    def setnext(self, node = None):
        """Set the next linked node."""
        self.next = node

class LinkedList:
    """
    A singly linked list.
    """

    def __init__(self, data=None, head=None):
        self.data = data
        self.head = head
  
    def __iter__(self):
        """Returns a forward iterator over the list."""
        node = self.head
        while node is not None:
            yield node.getdata()
            node = node.getnext()

    def __str__(self):
        """Returns a string representation of the list."""
        return " -> ".join([str(x) for x in self])

    def __repr__(self):
        """Returns a printable representation of the list."""
        return str(self)

    def __len__(self):
        """Returns the length of the list."""
        size = 0
        for i in self:
            size += 1
        return size
    def push(self, data):
        """
        Adds a new item to the front of the list.
        param data: The new item to prepend to the list.
        returns: None
        """
        if self.head is None:
            node = Node()
            node.setdata(data)
            node.setnext(None)
            self.head = node

        else:
            node = Node()
            node.setdata(data)
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node

def mergeLists(baseList, tailList):
    itr = baseList.head
    while itr.next:
        itr = itr.next
    itr.next = tailList.head
    return baseList


def intersection(listA, listB):
    lenA = len(listA)
    lenB = len(listB)
    offset = abs(lenA-lenB)
    print("Offset: ",offset)
    currA = listA.head
    currB = listB.head
    ## length of listA greater then listB; then offset the listA
    if lenA > lenB:
        for i in range(offset):
            currA = currA.next
    ## length of listB greater then listA; then offset the listB
    elif lenB > lenA:
        for i in range(offset):
            currB = currB.next
    #print(currA.data)
    #print(currB.data)
    while currA.next:
        if currA == currB:
            return currA
        else:
            currA = currA.next
            currB = currB.next


if __name__ == "__main__":
    mergeList = LinkedList()
    mergeList.push(130)
    mergeList.push(180)
    mergeList.push(190)

    listA = LinkedList()
    listA.push(10)
    listA.push(11)
    listA.push(13)
    listA.push(12)
    listA.push(15)
    listA.push(16)
    listA.push(18)
    listA=mergeLists(listA,mergeList)

    listB = LinkedList()
    listB.push(14)
    listB.push(17)
    listB.push(19)
    listB.push(20)
    listB=mergeLists(listB,mergeList)
    

    ##two lists created listA and listB
    print("List A: ",listA)
    print("List A length",len(listA))
    print("List B: ",listB)
    print("List B length",len(listB))
    common = intersection(listA, listB)
    #print("First Common: ",intersection(listA, listB).data)
    #print("First Common: ",intersection(listA, listB))
    #rint("First Common: ",intersection(listA, listB).next.data)
    print("First Common element: ",common.data)