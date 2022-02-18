import time

class Node():
    def __init__(self, data=None):
        self.data = data  
        self.parent = None
        self.left = None 
        self.right = None
        self.color = 1 # Red=1, Black=0

class RedBlackTree():
    def __init__(self):
        self.TNIL = Node()
        self.TNIL.color = 0
        self.TNIL.left = None
        self.TNIL.right = None
        self.root = self.TNIL

    def get_root(self):
        return self.root

    def _search_tree(self, node, key):
        if node == self.TNIL or key == node.data:
            return node
        if key < node.data:
            return self._search_tree(node.left, key)
        return self._search_tree(node.right, key)
    
    def rbInsert(self, key):
        ### Z node initialization ###
        node = Node(key)
        node.parent = None
        node.left = self.TNIL
        node.right = self.TNIL
        node.color = 1 # Red

        ### Tail ###
        y = self.TNIL
        ## Head##
        x = self.root
        ### Binary search fot the position of key ###
        ### Iterate from root to tail ###
        while x != self.TNIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        # y is parent of x
        node.parent = y
        ### y == TNIL; means tree empty ###
        if y == self.TNIL:
            self.root = node
        ### Y != TNIL find position of Z (left child or right child) ###
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        ### Fix RBT voilations###
        self.rbInsertFixup(node)

    # Fix the red-black tree
    def  rbInsertFixup(self, z):
        while z.parent.color == 1: ##RED
            if z.parent == z.parent.parent.left:
                ### Check Z's Uncle ###
                y = z.parent.parent.right
                # case 1 Z.p == RED and Z's Uncle == RED; then just recolor ### 
                if y.color == 1: ##RED
                    y.color = 0 ##BLACK
                    z.parent.color = 0 ##BLACK
                    z.parent.parent.color = 1 ##RED
                    z = z.parent.parent
                # case 2 Z.p == RED and Z's Uncle == BLACK; Z== Right child of Z.P ### 
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    # case 3
                    z.parent.color = 0 ##BLACK
                    z.parent.parent.color = 1 ##RED
                    self.right_rotate(z.parent.parent)

            else:
                ### Check Z's Uncle ###
                y = z.parent.parent.left 
                if y.color == 1: ##RED
                    y.color = 0 ##BLACK
                    z.parent.color = 0 ##BLACK
                    z.parent.parent.color = 1 ##RED
                    z = z.parent.parent 
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    z.parent.color = 0 ##BLACK
                    z.parent.parent.color = 1 ##RED
                    self.left_rotate(z.parent.parent)
        self.root.color = 0

    # search the tree for the key k
    def searchTree(self, k):
        return self._search_tree(self.root, k)

    # minimum key
    def minimum(self, node):
        while node.left != self.TNIL:
            node = node.left
        return node

    # maximum key
    def maximum(self, node):
        while node.right != self.TNIL:
            node = node.right
        return node

    # successor of a given node
    def successor(self, x):
        if x.right != self.TNIL:
            return self.minimum(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    # predecessor of a given node
    def predecessor(self,  x):
        if (x.left != self.TNIL):
            return self.maximum(x.left)
        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y

    # rotate left at node x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.TNIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == self.TNIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Sort in ascending order
    def inOrderTreeWalk(self, x):
        if x != self.TNIL:
            self.inOrderTreeWalk(x.left)
            if x.color == 1:
                print(str(x.data) + ": RED")
            elif x.color ==0:
                print(str(x.data) + ": BLACK")
            self.inOrderTreeWalk(x.right)
    
    def height(self,x):
        if x is self.TNIL:
            return -1 
        else:
            leftHt = self.height(x.left)
            rightHt = self.height(x.right)
            return max(leftHt, rightHt) + 1
    
    def printTree(self, node, level=0):
        if node != self.TNIL:
            self.printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self.printTree(node.right, level + 1)

if __name__ == "__main__":
    rbt = RedBlackTree()
    with open("C:\\Users\\d.dasarathan\\OneDrive - Northeastern University\\Documents\\CS5800-Algo\\HW-8\\array_of_numbers.txt") as f:
        lines = f.readlines()
    print("Input Array: ",lines)
    for line in lines:
        for elements in line.split(","):
            rbt.rbInsert(int(elements))
            #print(elements)
    #rbt.rbInsert(17)
    #rbt.rbInsert(85)
    #rbt.rbInsert(40)
    #rbt.rbInsert(25)
    #rbt.rbInsert(18)
    #rbt.rbInsert(5)
    #rbt.rbInsert(8)
    #rbt.rbInsert(15)
    #print(rbt.searchTree(85).data)
    #print(rbt.searchTree(27).data)
    #print("T.root: ",rbt.get_root().data)
    #print("T.root parent: ",rbt.get_root().parent)
    #print("Minimum: ",rbt.minimum(rbt.get_root()).data)
    #print("Maximum: ",rbt.maximum(rbt.get_root()).data)
    #print("Successor(40): ",rbt.successor(rbt.searchTree(40)).data)
    #print("Predecessor(85): ",rbt.predecessor(rbt.searchTree(85)).data)
    #print("Sort / In-order Tree walk")
    #rbt.inOrderTreeWalk(rbt.get_root())
    #print("Predecessor(5): ",rbt.predecessor(rbt.searchTree(5)))
    #print("Successor(85): ",rbt.successor(rbt.searchTree(85)))
    #rbt.printTree(rbt.get_root())
    #print("Height of the RBT: ",rbt.height(rbt.get_root()))
    print("Reb-Black Tree created with input array.")
    print("Height of the RBT: ",rbt.height(rbt.get_root()))
    while True:
        print("Select the operation that you want to perform on Red-Black Tree")
        print("0. Height of the Tree")
        print("1. Insertion")
        print("2. Print root node key")
        print("3. Minimum key in Tree")
        print("4. Maximum key in Tree")
        print("5. Sort / In-order walk")
        print("6. Successor of a node (given key)")
        print("7. Predecessor of a node (given key)")
        print("8. Search for a node in Tree (given key)")
        print("9. Print Tree")
        print("10. Deletion(extra credit)")
        option = input ("Enter number corresponding to the operation :")
        time.sleep(2)
        #print(option)
        if option == "0":
            print("You have selected TREE-HEIGHT operation")
            print("Height of the RBT: ",rbt.height(rbt.get_root()))
            time.sleep(3)

        elif option == "1":
            print("You have selected INSERT operation")
            key = input ("Enter the value you want to INSERT :")
            rbt.rbInsert(int(key))
            print("Key (%d) INSERT success." %int(key))
            print("Height of the RBT: ",rbt.height(rbt.get_root()))
            time.sleep(3)

        elif option == "2":
            print("You have selected PRINT-ROOT operation")
            print("T.root: ",rbt.get_root().data)
            time.sleep(3)
            
        elif option == "3":
            print("You have selected TREE-MINIMUM operation")
            print("TREE-MINIMUM: ",rbt.minimum(rbt.get_root()).data)
            time.sleep(3)
            
        elif option == "4":
            print("You have selected TREE-MAXIMUM operation")
            print("TREE-MAXIMUM: ",rbt.maximum(rbt.get_root()).data)
            time.sleep(3)
            
        elif option == "5":
            print("You have selected SORT/IN-ORDER WALK operation")
            rbt.inOrderTreeWalk(rbt.get_root())
            time.sleep(3)
            
        elif option == "6":
            print("You have selected TREE-SUCCESSOR operation")
            key = input ("Enter the value you want to find SUCCESSOR :")
            print("SUCCESSOR(%d): " %int(key),rbt.successor(rbt.searchTree(int(key))).data)
            time.sleep(3)
            
        elif option == "7":
            print("You have selected TREE-PREDECESSOR operation")
            key = input ("Enter the value you want to find PREDECESSOR :")
            print("PREDECESSOR(%d): " %int(key),rbt.predecessor(rbt.searchTree(int(key))).data)
            time.sleep(3)
            
            
        elif option == "8":
            print("You have selected SEARCH operation")
            key = input ("Enter the value you want to SEARCH in tree :")
            print("SEARCH(%d): "%int(key),rbt.searchTree(int(key)).data)
            time.sleep(3)
            
        elif option == "9":
            print("You have selected PRINT-TREE operation")
            rbt.printTree(rbt.get_root())
            time.sleep(3)
        
        elif option == "10":
            print("You have selected DELETE operation")
            print("Opeartion not yet implemented")
            time.sleep(3)