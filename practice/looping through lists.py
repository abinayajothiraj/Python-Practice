# Looping through lists:

# i) using for loop

this_list = ["Apple","Banana","Cherry"]
for x in this_list:
    print(x)

#ii) how do you loop using index? / how can you access list elements using index while looping?
# ans: by using range() with len() to iterate over indices
this_list = ["Apple","Banana","Cherry"]
for i in range(len(this_list)):
    print(this_list[i])

#iii) list comprehension

this_list = ["Mango","Apple","Banana","Cherry","orange"]
[print(x) for x in this_list]

#iv) find output


thislist1=[1,2,3]
for i in range(len(thislist1)):
    thislist1[i] +=1
print(thislist1)    #[2,3,4]


#v) index based looping

"""mylist = [1,2,3,4]
for i in range(len(mylist)):
    if mylist[i]%2==0:
        mylist.pop(i)
print(mylist)    # index error: list index out of range"""

# so the alternative method for this is by using list comprehension

mylist = [1,2,3,4]
[print(x) for x in mylist if x%2 != 0]   # 1 3


#vi) wrote a program to print only even numbers from the list

arr=[1,2,3,4,5,6]
for x in arr:
    if x%2 ==0:
        print(x)   # 2  4  6