
class node():
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        
    def reverse(head):
        total=[head] 
        while head.nextnode!=None:
            head=head.nextnode
            total.append(head)
        total[0].nextnode=None
        for i in range(0,len(total)-1):
            total[i+1].nextnode=total[i]
            

# # entering nodes value and nextnode
# a=node(1)
# b=node(2)
# c=node(3)
# d=node(4) 
# a.nextnode=b
# b.nextnode=c
# c.nextnode=d
## before value 
# print(a.nextnode.value)
# print(b.nextnode.value)

## reversal
# node.reverse(a)

## after value
# print(b.nextnode.value)
# print(c.nextnode.value)
# print(d.nextnode.value)

# we are not finding a.nextnode.value because a.nextnode is None and it will give an error message

