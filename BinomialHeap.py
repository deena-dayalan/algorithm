import math
class Node():
    def __init__(self, key=None, degree=None, parent=None, child=None, sibling=None):
        self.key = key  
        self.degree = degree
        self.parent = parent
        self.child = child
        self.sibling = sibling

class BinomialHeap():
    def __init__(self):
        self.head = None
        
    def BinomialHeapInsert(self, h, x):
        h_new = self.MakeBinomialHeap()
        x.parent = None
        x.child = None
        x.sibling = None
        x.degree = 0
        h_new.head = x
        h = self.BinomialHeapUnion(h, h_new)
        return h

    def BinomialHeapMinimum(self, h):
        y= None
        x = h.head
        min = math.inf
        while x != None:
            if x.key < min:
                min = x.key
                y = x
            x = x.sibling
        return y

    def BinomialLink(self,y,z):
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree = z.degree + 1

    def MakeBinomialHeap(self):
        h = BinomialHeap()
        return h
    
    def BinomialHeapMerge(self, h1, h2):
        h = self.MakeBinomialHeap()
        y = h1.head
        z = h2.head
        if y is not None:
            if z is not None:
                if (y.degree <= z.degree):
                    h = y
                elif (y.degree > z.degree):
                    h = z
            else:
                h = y
        else:
            h = z
        while (y is not None and z is not None):
            if (y.degree < z.degree):
                y = y.sibling
            elif (y.degree == z.degree):
                temp = y.sibling
                y.sibling = z
                y = temp
            else:
                temp = z.sibling
                z.sibling = y
                z = temp
        return h

    def BinomialHeapUnion(self, h1, h2):
        h = self.MakeBinomialHeap()
        h.head = self.BinomialHeapMerge(h1, h2)
        if h.head is None:
            return h
        prev_x = None
        x = h.head
        next_x = x.sibling
        while next_x is not None:
            if ((x.degree != next_x.degree) or (next_x.sibling != None and (next_x.sibling).degree == x.degree)):
                prev_x = x
                x = next_x
            else:
                if x.key <= next_x.key:
                    x.sibling = next_x.sibling
                    self.BinomialLink(next_x, x)
                else:
                    if prev_x == None:
                        h.head = next_x
                    else:
                        prev_x.sibling = next_x
                    self.BinomialLink(x, next_x)
                    x = next_x
            next_x = x.sibling
        return h

    def BinomialHeapDelete(self, h, x):
        if h.head is None:
            print("Heap empty")
            return
        self.BinomialHeapDecreaseKey(h,x,-math.inf)
        #self.BinomialHeapDecreaseKey(h,x,0)
        min, h_new = self.BiniomialHeapExtractMin(h)
        if min is not None:
            print("Node deleted successfully")
            return h_new

    def BinomialHeapDecreaseKey(self, h, x, key):
        if key > x.key:
            print("new key is greater than current key")
            return
        x.key = key
        y = x
        z = y.parent
        while z != None and y.key < z.key:
            temp = y.key
            y.key = z.key
            z.key = temp
            y = z
            z = y.parent
        print("Key reduced successfully")

    def BinomialHeapRevert(self,x):
        prev = None
        curr = x
        while curr is not None:
            sibling = curr.sibling
            curr.sibling = prev
            prev = curr
            curr = sibling
        x = prev
        return x

    def BiniomialHeapExtractMin(self, h):
        x = h
        if x is None:
            return None
        min = self.BinomialHeapMinimum(x)
        head = x.head 
        if head is min:
            x.head = None
        else:
            while (head.sibling != min):
                head = head.sibling
            x.head.sibling = x.head.sibling.sibling
        
        h_new = self.MakeBinomialHeap()
        if (min.child is not None):
            h_new.head = self.BinomialHeapRevert(min.child)
       
        h = self.BinomialHeapUnion(x,h_new)
        return min, h

    def BinomialHeapDisplayRoots(self,x):
        if x is None:
            print("Heap empty")
            return 0
        print("Root Nodes are: ", end =" ")
        while x is not None:
            print(x.key, end =" ")
            if x.sibling is not None:
                print("--->",end =" ")
            x = x.sibling
        print()

    def Display(self, x):
        if x is None:
            return
        print(x.key)
        self.Display(x.child)
        self.Display(x.sibling)
    
if __name__ == '__main__':
    bh = BinomialHeap()
    heap = bh.MakeBinomialHeap()
    for i in range(1,10):
        heap = bh.BinomialHeapInsert(heap, Node(i))
    print("Binomial heap after inserinting elements")
    bh.BinomialHeapDisplayRoots(heap.head)
    print("### List of elements in Heap ###")
    bh.Display(heap.head)

    ### MINIMUM ###
    node = bh.BinomialHeapMinimum(heap)
    print("Binomial Heap Minimum: ", node.key)

    ### EXTRACT MINIMUM ###
    min, heap = bh.BiniomialHeapExtractMin(heap)
    print("Binomial Heap Extract Minimum: ",min.key)
    print("Binomial heap after ExtractMin")
    bh.BinomialHeapDisplayRoots(heap.head)
    print("### List of elements in Heap ###")
    bh.Display(heap.head)
    
    ### INSERT ###
    heap = bh.BinomialHeapInsert(heap, Node(12))
    print("Binomial heap after inserting key 12")
    bh.BinomialHeapDisplayRoots(heap.head)
    print("### List of elements in Heap ###")
    bh.Display(heap.head)

    ### EXTRACT MINIMUM ###
    min, heap = bh.BiniomialHeapExtractMin(heap)
    print("Binomial Heap Extract Minimum: ",min.key)
    print("Binomial heap after ExtractMin")
    bh.BinomialHeapDisplayRoots(heap.head)
    print("### List of elements in Heap ###")
    bh.Display(heap.head)

    ### MINIMUM ###
    node = bh.BinomialHeapMinimum(heap)
    print("Binomial Heap Minimum: ",node.key)

    ### FIND ELEMENT for DECREASE KEY###
    node = bh.BinomialHeapMinimum(heap).child.child
    print(node)
    print("Node for Decrease Key: ", node.key)
    print(node.key)
    
    ### DECREASE KEY ###
    bh.BinomialHeapDecreaseKey(heap, node, 4)
    bh.BinomialHeapDisplayRoots(heap.head)
    print("### List of elements in Heap ###")
    bh.Display(heap.head)

    ### FIND ELEMENT for DELETE KEY###
    node = bh.BinomialHeapMinimum(heap).child.sibling
    print(node)
    print("Node for Delete Key: ", node.key)
    #print(node.key)

    ### DELETE ###
    heap = bh.BinomialHeapDelete(heap, node)
    bh.BinomialHeapDisplayRoots(heap.head)
    print("### List of elements in Heap ###")
    bh.Display(heap.head)