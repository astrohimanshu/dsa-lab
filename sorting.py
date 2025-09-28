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
def merge(a, i, mid, j):
    c = []
    low = i 
    high = mid + 1
    while low <= mid and high <= j:
        if a[low]  <= a[high]:
            c.append(a[low])
            low += 1
        else:
            c.append(a[high])
            high += 1
        

    while low <= mid:
        c.append(a[low])
    while high <= j:
        c.append(a[high])

    for k in range(len(c)):
        a[low + k] = c[k] 

def mergesort(a, i, j):
    if i == j:return
    mid = (i + j) // 2
    mergesort(a, i, mid)
    mergesort(a, mid + 1, j)
    merge(a,i, mid, j)

a = [2,7,5]
mergesort(a,0,3)
print(a)
