'''
Given an array arr[], return the second largest element from an array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the first largest.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

Input: arr[] = [10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist..
'''

class second:
    def largest(self,arr):
        if(arr==[]):
            return -1
        else:
            arr = list(set(arr))
            arr.remove(max(arr))
            if(arr==[]):
                return -1
            else:
                return max(arr)
vetri = second()
print(vetri.largest(arr = [12, 35, 1, 10, 34, 1]))

