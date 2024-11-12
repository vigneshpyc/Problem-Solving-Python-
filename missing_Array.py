def missingNumber(arr):
        
    t_sum = 0
    r_sum = 0
    for i in range(1,max(arr)+1):
        t_sum += i
    
    for i in arr:
        r_sum+=i

    if(t_sum == r_sum):
        return max(arr)+1
    else:
        return(abs(r_sum - t_sum))
print(missingNumber(arr=[1, 2, 3, 5]))
