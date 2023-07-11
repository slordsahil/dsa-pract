class node():
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        
        
    def reverse(N):
        total=[N]
        while N.nextnode!=None:
            N=N.nextnode
            total.append(N)
            print("hi")
        for i in range(len(total)//2): 
            total[i].value,total[-(i+1)].value=total[-(i+1)].value,total[i].value

        
            