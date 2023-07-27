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
            
    
    def get_childleft(node):
        return node.childleft
        
    def get_childright(node):
        return node.childright
        
    def get_childvalue(node):
        return node.childvalue
# %%
store=binary_tree("restraurent")
store.insert_childleft("paneer")
store.insert_childright("egg")
store.insert_childleft("mushroom")
store.insert_childright("omlete")
store.insert_childleft("veg")
store.insert_childright("nonveg")
#%%
store.get_childleft().get_childvalue()

#%%
def pre_order(root,tree_nodes=[]):
    if root==None:
        return 
        
        
    tree_nodes.append(root.get_childvalue())
    pre_order(root.get_childleft())
    pre_order(root.get_childright())
    return tree_nodes
pre_order(store)
# %%

def post_order(root,tree_nodes=[]):
    if root==None:
        return 
        
        
    post_order(root.get_childleft())
    post_order(root.get_childright())
    tree_nodes.append(root.get_childvalue())
    return tree_nodes
pre_order(store)
# %%
