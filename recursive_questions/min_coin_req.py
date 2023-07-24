def min_coin(N,coins,count=0):
    coins.sort()
    if N==0:
        return count
    
    else:
        lc=coins.pop()
        print(N)
        c=N//lc
        print(f'u required {lc} coin  {c} times')
        count+=c
        N=N%lc
        return  min_coin(N,coins,count)
        
min_coin_= min_coin(1099,[1,5,10,25])
print(min_coin_)