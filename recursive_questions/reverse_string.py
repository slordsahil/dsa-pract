def reverse_string(N):
       
    if len(N) == 1:
        return N

    else:
        return N[-1] + reverse_string(N[0:-1])
        
        
a=reverse_string('sahil')
print(a)
# %%
