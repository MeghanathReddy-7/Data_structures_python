def partion(a,low,high):
    i=low-1
    pivot=a[high]
    for j in range(low,high):
        if a[j]<=pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1
def quicksort(a,low,high):
    if low<high:
        loc=partion(a,low,high)
        quicksort(a,low,loc-1)
        quicksort(a,loc+1,high)
a=[int(x) for x in input("Enter list elements").split()]
h=len(a)-1
quicksort(a,0,h)
print(a)