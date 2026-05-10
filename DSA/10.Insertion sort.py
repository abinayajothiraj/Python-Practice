def insertion_sort(l):
    """
    Considering our 0th element is already sorted meaning "Single element array is sorted".

    Pick the element from the unsorted array i.e 1 to n and insert in its place. The 1st element is compared with the
    0th,and it is inserted at its place. Now sorted part is increased to 0,1.

    The 2nd element is compared with the 0th & 1st
    elements and inserted at its place.Now sorted part is increased to 0,1,2.

    The nth element is compared with the
    previous elements and inserted at its place

    Complexity : Best case : O(N) Worst case O(N**2)
    """
    n = len(l)

    for i in range(1, n):
        while i > 0:
            if l[i] < l[i - 1]:
                l[i - 1], l[i] = l[i], l[i - 1] # a,b = b
            else:
                break
            i -= 1
    return l