from Car import *
from Node import *
class NodeQ:
    def __init__(self,data):
        self.data = data
        self.next = None
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def EnQueue(self, data):
        node = NodeQ(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    #end def
    def DeQueue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data
#end class    
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    #end def
    def insert(self,name, price):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if name[0] == 'B' or price > 100:
            return
        new_car = Node(Car(name, price))
        self.root = BSTree.insertNode(self.root, new_car)  
    
    def insertNode(node, new_car):
        if node is None:
            return new_car
        if new_car.data.Price < node.data.Price:
            node.left = BSTree.insertNode(node.left, new_car)
        elif new_car.data.Price > node.data.Price:
            node.right = BSTree.insertNode(node.right, new_car)
        return node
        
    
        #end def
    def visit(self,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    #end def
    def preOrder(self,p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    #end def
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    #end def
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    #end def
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    #end def
    def inOrder(self,p):
        if p==None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)        
    #end def
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    #end def
    def breadth_first(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")        
    #end def
    def f2(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        self.pre_f2(self.root)
        print("")
    def pre_f2(self,p):
        if p==None:
            return
        if p.data.Price in [3,4,5]:
            self.visit(p)
        self.pre_f2(p.left)
        self.pre_f2(p.right)
 
    #end def
        ####################

    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        flag = True

        def check(x):
            return x < 7
        count = 0
        deleteNode = None
        
        def breadth_first2(tree):
            nonlocal deleteNode, flag, count
            if tree.isEmpty():
                return
            my = MyQueue()
            my.EnQueue(tree.root)
            while not my.isEmpty():
                p = my.DeQueue()
                if (p.left != None and p.right != None and check(p.data.Price) and flag):
                    deleteNode = p
                    count += 1
                    if count == 1:
                        flag = False
                        break
                if p.left != None:
                    my.EnQueue(p.left)
                if p.right != None:
                    my.EnQueue(p.right)

        def deleteByCopyingLeft(p):
            if p == None or p.left == None:
                return
            if p.left.right == None:
                p.data = p.left.data
                p.left = p.left.left
                return
            cur = p.left.right
            father = p.left
            while cur.right:
                father = cur
                cur = cur.right
            p.data = cur.data
            father.right = cur.left
        breadth_first2(self)
        deleteByCopyingLeft(deleteNode)
        

        #################################
        pass

                
 
        
        ############################
    def findFather(self, root, data):
        if root.data.Price == data:
            return None
        fa = None
        cur = root
        while cur:
            if cur.data.Price  == data:
                return fa
            fa = cur
            if cur.data.Price < data:
                cur = cur.right
            else:
                cur = cur.left
        return None
    
    def rightRotate(self,p):
        if not p or not p.left:
            return
        c = p .left
        p.left = c.right
        c.right = p
        return c
    def rightRotation(self, root, data):
        f = self.findFather(root, data.Price)
        p =None
        if f == None:
            if(root.data != data):
                return
            else:
                p =root
        else:
            if (f.data.Price > data.Price):
                p = f.left
            else:
                p = f.right
        newNode = self.rightRotate(p)
        if f == None:
            self.root = newNode
        else:
            if (f.data.Price < data.Price):
                f.right = newNode
            else:
                f.left = newNode
                
    def f4(self):
        #  ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
    #breadth_first(self):
        rotateNode = None
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left !=None and p.data.Price < 7:
                rotateNode = p
                break
            if p.left != None:
                my.EnQueue(p.left)
            if p.right != None:
                my.EnQueue(p.right)
        if rotateNode == None:
            return
        self.rightRotation(self.root, rotateNode.data)
        


# end class
