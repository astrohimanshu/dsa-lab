#%%
def selectionsort(a: list):

    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

a = [2,3,1,4,6]
selectionsort(a)
print(a)
#%%
def merge(a, low, mid, high):
    i = low
    j = mid  + 1
    temp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1
    while i <= mid:
        temp.append(a[i])
        i += 1
    while j <= mid:
        temp.append(a[j])
        j += 1

    for k in range(len(temp)):
        a[low + k] = temp[k]

def merge_sort(a, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(a, low, mid)
    merge_sort(a, mid + 1, high)
    merge(a, low, mid, high)

a = [2,7,5,0,9,-1,-3,100]
merge_sort(a,0,len(a) - 1)
print(a)
#%%
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]

a = [100, 1, 3, 2, 10 , -1, -1]
bubble_sort(a)
print(a)

#%%
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while( j >= 0 and a[j] > key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

a= [100, 1, 3, 2, 10 , -1, -1]
insertion_sort(a)
print(a)      
def rec_insert(a, size = None):
    if n == None:
        n = len(a)
    if len(a) <= 1:
        return 
    rec_insert(a, n - 1)
    # else place last element in correct place
    last = a[n - 1]
    j = n - 2
    while j >= 0 and a[j] > last:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = last
a= [100, 1, 3, 2, 10 , -1, -1]
insertion_sort(a)
print(a) 

#%%
a = [3,1,10,1,6,7,8]
def partition(a, low = None, high = None):
    if low == None or high == None: low, high = 0, len(a) - 1

    i = low + 1
    pivot = a[low]
    j = high
    while(i <= j):
        while(i <= j and a[i] <= pivot): i += 1
        while(i <= j and a[j] > pivot): j -= 1
        if(i<=j):
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    
    a[low], a[j] = a[j], a[low]
    return j

print(partition(a))
print(a)

def quicksort(a, low = None, high = None):
    if low == None or high == None:
        low = 0
        high = len(a) - 1
    if low >= high: return
    p = partition(a, low, high)
    quicksort(a, low, p - 1)
    quicksort(a, p + 1, high)

b = [5,4,3,2,1, -1,-1,-2]
quicksort(b)
print(b)
# %%
# binary search
def binary_search(a, key, low = None, high = None):
    if low == None or high == None:
        low = 0 
        high = len(a) - 1  

    if low  > high:
        return -1
    mid = (low + high) // 2

    if key == a[mid]:
        return mid
    
    elif key < a[mid]: return binary_search(a, key, low, mid)
    elif key > a[mid]: return binary_search(a, key, mid + 1, high)

a = [-1,-1,1,2,3,4,5]

binary_search(a, 4)

#%%
