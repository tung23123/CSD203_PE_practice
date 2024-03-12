import math
from Stack import *
class Graph:
    def __init__(self,data):
        self.a = data
    def display(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                print(self.a[i][j], end =" ")
            print("")
        print("")
    def depthFirst(self,start):
        b = [True]*len(self.a)
        b[start] = False    
        self.depth(start,b)
        for i in range(len(b)):
            if b[i]:
                b[i] = False
                self.depth(i,b)
    def depth(self,start,b):
        t = self.deg(start)
        print(f"{chr(start+65)}", end = " ")    
        for i in range(len(b)):
            if self.a[start][i]!=0 and b[i]:
                b[i] = False
                self.depth(i,b)
    def deg(self, x):
        count =0
        for i in range(len(self.a)):
            count += self.a[x][i]
        return count
    #----------------------------
    def depthFirst2(self,start):
        b = [True]*len(self.a)
        b[start] = False    
        self.depth2(start,b)
        for i in range(len(b)):
            if b[i]:
                b[i] = False
                self.depth2(i,b)
    def depth2(self,start,b):
        t = self.deg2(start)
        print(f"{chr(start+65)}({self.deg2(start)})", end = " ")    
        for i in range(len(b)):
            if self.a[start][i]!=0 and b[i]:
                b[i] = False
                self.depth2(i,b)
    def deg2(self, x):
        count =0
        for i in range(len(self.a)):
            count += self.a[x][i]
        return count
    def f1(self,start):
        self.depthFirst(start)
        print("")
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1========
        self.depthFirst2(start)


        #---------------------------
        print("")
    
    #----------------------------    
    '''Algorithm for finding an Euler cycle from the vertex X using stack 
//Input: Connected graph G with all vertices having even degrees
//Output: Euler cycle
declare a stack S of characters
declare empty array E (which will contain Euler cycle)
push the vertex X to S
while(S is not empty)
 {r = top element of the stack S 
  if r is isolated then remove it from the stack and put it to E
   else
   select the first vertex Y (by alphabet order), which is adjacent
   to r, push  Y  to  S and remove the edge (r,Y) from the graph   
 }
 the last array E obtained is an Euler cycle of the graph'''
    #-------------------------------------
    def f2(self,start):
        #===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        for i in range(len(self.a)):
            if self.deg(i) % 2 != 0:
                return "Graph doesn't have an Euler Cycle"

        # Initialize stack and path
        stack = [start]
        path = []
        original_degrees = [self.deg(i) for i in range(len(self.a))]

        # Main algorithm to find Euler's cycle
        while stack:
            v = stack[-1]
            if self.deg(v) == 0:
                path.append(stack.pop())
            else:
                for u in sorted(range(len(self.a)), key=lambda x: chr(x+65)):
                    if self.a[v][u] > 0:
                        stack.append(u)
                        # Remove the edge from the graph
                        self.a[v][u] -= 1
                        self.a[u][v] -= 1
                        break

        # Print Euler's cycle
        euler_cycle = ' '.join([chr(65 + v) for v in path])
        print(euler_cycle)

        # Print Euler's cycle with degrees

        #------------------------------        