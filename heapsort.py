def heapify(arr, n, i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[i]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest = r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def insert(array,newNum):
    size=len(array)
    if size==0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2)-1,-1,-1):
            heapify(array,size,i)
def heapsort(array,n):
    for i in range(n-1,0,-1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)
arr = []
insert(arr, 13)
insert(arr, 54)
insert(arr, 91)
insert(arr, 5)
insert(arr, 26)
n=len(arr)
print ("Max-Heap array: " + str(arr))
print("heap sort:")
heapsort(arr,n)
print(arr)