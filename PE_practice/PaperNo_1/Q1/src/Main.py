from MyList import *
from Car import *
import re
class Main:
    def __init__(self,fileName):
        self.fileName = fileName
        self.data = None
    #end def    
    def readFile(self, lineStart, numberline):
        f1 = open(self.fileName,'r');
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count== lineStart+1:
                LineName = re.sub('\s+',' ',line.strip())
                listName = LineName.split(" ")
                self.data =[listName];
            if count>lineStart+1 and count<lineStart+1+numberline:                 
                b = []
                LineValue = re.sub('\s+',' ',line.strip())
                listValue = LineValue.split(" ")
                for i in range(len(listValue)):
                    b.append(int (listValue[i]))
                self.data.append(b)
        f1.close()
    def display(self):
        for line in self.data:
            print(line, end ="\n")        
                # listName = line.strip().split(", ")
    def f1(self, linkList):
        for i in range(len(self.data[0])):
            linkList.addLast(self.data[0][i],self.data[1][i])
    #end def       
    def creatList(self,linkList,begin=0, end=0):
        self.readFile(begin, end)
        for i in range(len(self.data[0])):
            linkList.addLast(self.data[0][i],self.data[1][i])
#####################            
m = Main("input.txt")
linkList = MyList()
print("1. Test f1 (1 mark)")
print("2. Test f2 (1 mark)")
print("3. Test f3 (1 mark)")
print("4. Test f4 (1 mark)")
choice = int(input("Your selection (1->4)"))
print("OUTPUT")
if choice ==1:    
    m.readFile(1,2)
    m.f1(linkList)
    linkList.traverse()
elif choice ==2:
    linkList.clear()
    m.creatList(linkList,4,2)
    linkList.traverse()
    linkList.addFirst("X", 1)
    linkList.traverse()
elif choice ==3:
    linkList.clear()
    m.creatList(linkList,7,2)   
    linkList.traverse() 
    linkList.delete(5)
    linkList.traverse()
elif choice==4:
    linkList.clear()
    m.creatList(linkList,10,2)
    linkList.traverse()
    linkList.sort()
    linkList.traverse()
else:
    print("Wrong select")
print("FINISH")    