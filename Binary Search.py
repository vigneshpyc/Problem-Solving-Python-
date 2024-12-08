
#Binary search

def binary_search(arr, key):
    low=0
    high = len(arr)-1
    mid=0
    while(high>=low):
        mid = int(low+((high-low)/2))

        if(arr[mid]==key):
            return mid

        if(arr[mid]>key):
            high = mid-1

        else:
            low = mid+1
    return -1
        
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
key = 10
result = binary_search(arr,key)
if(result==-1):
    print('element is not found in the given array')
else:
    print('element fount at index')
