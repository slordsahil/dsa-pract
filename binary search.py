#%%
def bs(k,arr):
    mid=len(arr)//2
    if arr[mid]==k:
        return arr[mid]
    elif k>arr[mid]:
        arr1=arr[mid:]
        return bs(k,arr1)
    else:
        arr1=arr[:mid+1]
        print(arr,mid+1)
        return bs(k,arr1)
        
        
bs(4,[1,2,3,4,5])
# %%
