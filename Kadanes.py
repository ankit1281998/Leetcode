arr= [1,-5,-8,4,6,7,-6,4,6,4,5,-5,-7,-8]

def kadanes(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(arr[i],current_sum+arr[i])
        max_sum = max(max_sum,current_sum)
    return max_sum


print(kadanes(arr))