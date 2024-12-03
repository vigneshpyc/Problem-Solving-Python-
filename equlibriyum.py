'''
Given an array arr of non-negative numbers. The task is to find the first equilibrium point in an array. The equilibrium point in an array is an index (or position) such that the sum of all elements before that index is the same as the sum of elements after it.

Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

Examples:

Input: arr[] = [1, 3, 5, 2, 2]
Output: 3 
Explanation: The equilibrium point is at position 3 as the sum of elements before it (1+3) = sum of elements after it (2+2).

Input: arr[] = [0, 1, 0]
Output: 2
Explanation: Since sum all the elements before 1 and after 1 are same, so index 2 is equillibrium.

Input: arr[] = [1, 2, 3]
Output: -1
Explanation: There is no equilibrium point in the given array.
'''
#ssolution

def equilibriumPoint(arr):
        add1,add2,result,c=0,0,'',0
        for i in range(len(arr)-1):
            add1 = add1 + int(sum(arr[:i]))
            add2 = add2 + int(sum(arr[i+1:]))
            if(add1==add2):
                c+=i+1
                result+='True'
            add1,add2=0,0
        if(result == 'True'):
            return c
        else:
            return -1
print(equilibriumPoint(arr = [1, 3, 5, 2, 2]))
