def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid       # target found
        elif arr[mid] < target:
            low = mid+1      # search right half
        else:
            high = mid-1     # search left half
    return -1                # target not found




arr=[2,4,6,8,10,12,14]
target=10
index=binary_search(arr,10)
print(index)

"""numbers=[2,4,6,8,10,12,14]
target=10
result=binary_search(numbers,target)
if result != -1:
    print("Element is present at index:  ",result)
else:
    print("Element is not present" )"""