N=15
color=31,6,3,48,84,18,57,73,4,4,73,4,4,4,4
radius=53,23,44,61,96,1,97,15,83,97,97,97,83,97,97
class balls:
    def __init__(self,color,radius):
        self.color=color
        self.radius=radius

total=[]
for i in range(N):
    i=balls(color[i],radius[i])
    total.append(i)
    for  j in total:
        if i!=j:
            if i.color==j.color:
                if i.radius==j.radius:
                    total.remove(j)
                    total.pop()
                    break
                    
        
    
        
    

    

a=len(total)
print(a)