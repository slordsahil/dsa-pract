arr=[1,2,3,-1,4,2,4,5,3,2,10,-10,11,-12,12,12,-1]
def find_cont_largest_sum(arr):
    max_sum =sum(arr)
    actual_sum=0
    for i in arr:
        actual_sum+=i
        if actual_sum<0:
            actual_sum = 0
        elif actual_sum>max_sum:
            max_sum = actual_sum
            
    return max_sum

sum=find_cont_largest_sum(arr)
print(sum)
