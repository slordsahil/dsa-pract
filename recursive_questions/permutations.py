#%%
def permutation(n):
    out=[]
    if len(n)==1:
        out =[n]
    else:
        for i,let in enumerate(n):
            for perm in permutation(n[:i] + n[i+1:]):
                out+=[let+perm]
    return out

permutation_string=permutation('abc')
print(permutation_string)
# %%
