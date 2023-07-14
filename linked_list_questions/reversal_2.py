class node():
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        
    def reversal(head): 
        current =head
        previous=None
        
        
        while current:
            temp=current
            current=current.nextnode
            temp.nextnode=previous
            previous=temp
        return previous.value


            
#entering nodes aand respective value   
# # %%
# a=node(1)
# b=node(2)
# c=node(3)
# d=node(4) 
# a.nextnode=b
# b.nextnode=c
# c.nextnode=d


# # %%
#calling reversal
# node.reversal(a)



#checking whether node is reversed
# # %%
# a.nextnode.value
# # %%
# b.nextnode.value
# # %%
# c.nextnode.value
# # %%
# d.nextnode.value
# # %%
# d.value
# # %%
