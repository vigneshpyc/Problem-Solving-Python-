def findDuplicates(arr):
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
        
    return sorted(duplicates)
arr = [2, 3, 1, 2, 3]
print(findDuplicates(arr))
