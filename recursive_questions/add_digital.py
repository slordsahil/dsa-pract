#%%
def  add_digits(N):
    if N<10:
        return N
    else:
        return  N %10 +(add_digits(N//10))
    

a=add_digits(8654)
print(a)
# %%
