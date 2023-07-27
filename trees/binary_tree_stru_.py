#%%
class binary_tree():
    def __init__(self, value):
        self.childvalue = value
        self.childleft = None
        self.childright = None
        
    
    def insert_childleft(self, newNode):
        if self.childleft==None:
            self.childleft = binary_tree(newNode)
        else:
            t=binary_tree(newNode)
            t.childleft = self.childleft
            self.childleft=t
        
    def insert_childright(self, newNode):
        if self.childright==None:
            self.childright = binary_tree(newNode)
        else:
            t=binary_tree(newNode)
            t.childright = self.childright
            self.childright=t
            
    
    def get_childleft(self):
        return self.childleft
        
    def get_childright(self):
        return self.childright
        
    def get_childvalue(self):
        return self.childvalue
# %%
store=binary_tree("restraurent")
store.insert_childleft("veg")
store.insert_childright("nonveg")

#%%
def pre_order(root):
    if root.get_childvalue!=None:
        print(root.get_childvalue)
        pre_order(root.get_childleft)
        pre_order(root.get_childright)
# %%
pre_order(store)
# %%
