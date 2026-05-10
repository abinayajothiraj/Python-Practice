"""
Algorithm:

Go through the array to find the lowest value.
Move the lowest value to the front of the unsorted part of the array.
Go through the array again as many times as there are values in the array.

"""


def selection_sort(arr):
    n = len(arr)                          #n=8
    for i in range(n - 1):                #8-1 = 7 [0,1,2,3,4,5,6]
        min_index = i                     #i=0,                                           ,i=1
        for j in range(i + 1, n):         #j=(1,7)=[1,2,3,4,5,6]                          ,j=(2,7)=2,3,4,5,6
            if arr[j] < arr[min_index]:   #1- 34 < 64 ,2- 25 < 34, 3- 5< 25,4- 22 < 5     ,2-> 34<64, 3->25<34,4->22<25,5->11<22,6-> 90<11
                min_index = j             #j=1,          j=2,       j=,3                  ,j=2      ,j=3      ,j=4     ,j=5
        min_value = arr.pop(min_index)    #j=4,in.v=3 -> m.v= pop.3[64,34,25,22,11,90,94]  ,j=5 , m.v=pop(5)  [5,64,34,25,22,90,94]
        arr.insert(i, min_value)          #i=(0,3)-> [5,64,34,25,22,11,90,94]              ,insert(1,5)   [5,11,64,34,25,22,90,94]
    return arr
# usage
mylist = [64, 34, 25, 5, 22, 11, 90,94]
sorted_list = selection_sort(mylist)
print(sorted_list)