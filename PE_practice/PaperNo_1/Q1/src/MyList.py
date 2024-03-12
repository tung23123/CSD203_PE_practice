from Car import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")        
    def clear(self):
        self.head = None
#Q1-1
    def addLast(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if name[0] == 'B' or price > 100:
            return
        new_car = Node(Car(name,price))
        if not self.head:
            self.head = new_car
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_car
            new_car.next = None

    # end def
#Q1-2    
    def addFirst(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        new_node = Node(Car(name,price))
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    # end def
#Q1-3
    def delete(self, price =0):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        prev = self.head
        if prev.data.Price == price:
            self.head = prev.next
            prev = None
            return 
        while prev.next:
            if prev.next.next:
                if prev.next.data.Price == price:
                    prev.next = prev.next.next
                    return 
            elif not prev.next.next:
                if prev.next.data.Price == price:
                    return 
            prev = prev.next
        
    #end def
# Q1-4
    def sort(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        check = True
        while check:
            check = False
            current = self.head
            while current.next:
                if current.data.Price > current.next.data.Price:
                    self.swap(current, current.next)
                    check = True
                current = current.next
        
    #end def
    def swap(self, el1, el2):
        tmp = el1.data
        el1.data = el2.data
        el2.data = tmp