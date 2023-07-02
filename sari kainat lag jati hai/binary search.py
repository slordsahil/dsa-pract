def bs(k,arr):
    mid=len(arr)//2
    if arr[mid]==k:
        return mid
    elif k>arr[mid]:
        arr=arr[mid:]
        return bs(k,arr)
    else:
        arr=arr[:mid+1]
        print(arr,mid+1)
        return bs(k,arr)
        
        
bs(4,[1,2,3,4,5])