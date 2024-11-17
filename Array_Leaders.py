arr = [16, 17, 4, 3, 5, 2]
new_arr = []
new_arr.append(max(arr))
index = arr.index(max(arr))
for i in range(index,-1,-1):
    arr.remove(arr[i])
print(arr)
