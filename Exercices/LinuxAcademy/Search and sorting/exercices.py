# 1. Write a Python program for binary search.
def binary_search(l,num):
    first = 0; last = len(l)-1; found = False
    while(first<=last and not found):
        mid = (first + last)//2
        if l[mid] == num:
            found = True
        else:
            if num < l[mid]:
                last = mid-1
            else:
                first = mid+1
    return found
print('1. Binary search:', binary_search([1,2,3,5,8], 0), binary_search([1,2,3,5,8], 5))

# Write a Python program for sequential search.
def Sequential_Search(l,num):
    pos = 0; found = False
    while (pos <= len(l) and found == False):
        if l[pos] == num:
            found = True
        else:
            pos +=1
    return (found, pos)
print('2. Sequentila search:', Sequential_Search([11,23,58,31,56,77,43,12,65,19],31))

# 3. Write a Python program for binary search for an ordered list.
def Ordered_binary_Search(liste, num):
    if len(liste) == 0:
        return False
    else:
        mid_point = len(liste)//2
        if mid_point == num:
            return True
        else:
            if num < mid_point:
                return binary_search(liste[:mid_point], num)
            else:
                return binary_search(liste[mid_point+1:], num)

print('3. Ordered Binary search:', Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3), 
Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))

# 4. Write a Python program to sort a list of elements using the bubble sort algorithm.
def bubble_algorithm(l):
    for n in range(len(l)-1,0,-1):
        for i in range(n):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
    return l
print('4. Bubble algo:', bubble_algorithm([14,46,43,27,57,41,45,21,70]))

# 5. Write a Python program to sort a list of elements using the selection sort algorithm.
def selection_sort(l):
    for n in range(len(l)):
        l_search = l[n:]
        if l[n] > l[l.index(min(l_search))]:
            l.insert(n, l.pop(l.index(min(l_search))))
    return l
print('5. Selection sort algo:', selection_sort([14,46,43,27,57,41,45,21,70]))

# 6. Write a Python program to sort a list of elements using the insertion sort algorithm.
def insertion_sort(nlist):
    for index in range(1,len(nlist)):
        for n in nlist[:index]:
            if n > nlist[index]:
                nlist.insert(nlist[nlist.index(n)-1], nlist.pop(index))
    return nlist
print('6. Insertion sort algo:', insertion_sort([14,46,43,27,57,41,45,21,70]))

# 7. Write a Python program to sort a list of elements using shell sort algorithm.
# def shell_sort(l):



# print('7. Shell sort:', shell_sort([14,46,43,27,57,41,45,21,70]))
 

# 8. Write a Python program to sort a list of elements using the merge sort algorithm.
def merge_sort(l):
    pair = sorted(l, key=lambda n: (n,n+1))
    # db_pair = sorted(pair, key=lambda m:  ) #[(a,b) if a<b else (b,a) for a, b in pair]
    # for n in range(0,len(db_pair),2):
    #     new_l = [(a,b) if a<b else (b,a) for a, b in db_pair]
    return pair
print('8. Merge sort:', merge_sort([14,46,43,27,57,41,45,21,70]))