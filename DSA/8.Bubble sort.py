"""
Algorithm Steps

 Start from the first element
 Compare two adjacent elements
 Swap them if the first is greater
 Continue till the end of the array
 Repeat the process until the array is sorted


"""



# bubble sort
mylist=[64,34,25,12,22,11,90,5]
n=len(mylist)
for i in range(n-1):
    for j in range(n-i-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
print(mylist)


"""
# improved bubble sort

a=[7,3,9,12,11]
b=len(a)
for i in range(b-1):
    swapped = False
    for j in range(b-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
    if not swapped:
        break
print(a)"""

#using function

def bubblesort(arr):
    n = len(arr)                                # n =5
    for i in range(n-1):                        # i=5-1= 4 [0,1,2,3]
        swapped = False
        for j in range(n-i-1):                  # j = 5-0-1=4 [0,1,2,3]
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr=[7,3,9,12,11]
print(bubblesort(arr))