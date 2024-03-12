from Graph import *
import re
class Main:
    def __init__(self,fileName):
        self.fileName = fileName
        self.data = []
        self.lineNumber =0
    #end def    
    def readFile(self, lineStart):
        f1 = open(self.fileName,'r');
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count== lineStart:
                lineNumber = int(line)                
                for i in range(lineNumber): 
                    line = f1.readline()                    
                    listValue = re.sub("\s+"," ",line.strip()).split(" ")                
                    row =[]
                    for j in range(len(listValue)):                        
                        row.append(int(listValue[j]))
                    self.data.append(row)
        f1.close()
    def display(self):
        for line in self.data:
            print(line, end ="\n")        
                # listName = line.strip().split(", ")
    def clear(self):
        self.data =[]
        self.lineNumber = 0
#####################            
m = Main("input.txt")
print("1. Test f1 (1 mark)")
print("2. Test f2 (1 mark)")
choice = int(input("Your selection (1->2)"))
print("OUTPUT")
if choice ==1:    
    m.readFile(2)
    g = Graph(m.data)
    # g.display()
    g.f1(1)
elif choice ==2:
    m.clear()
    m.readFile(13)
    g = Graph(m.data)
    # g.display()
    g.f2(1)
else:
    print("Wrong select")
print("FINISH")    