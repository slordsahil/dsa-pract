class node():
    def __init__(self,value):
        self.value = value
        self.next = None
    def next(self):
        return self.next
        
class check_cycle(node):
    
    def check(sol):
        node_list=[]
        while node.next(sol)!=None:
            if sol not in node_list:
                node_list.append(sol)
                sol = node.next(sol)
            else:
                return str(True )+str("its cycle")
        return str(False )+str("its not cycle")
     

a=node(input)  
b=node(2) 
c=node(3) 
d=node(4)
a.next=b
b.next=c
c.next=d
test=check_cycle.check(a)
print(test)          
