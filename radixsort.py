def countsort(l,n,pos):
    count=[0]*10
    b=[0]*n
    for i in range(n):
        count[(l[i]//pos)%10]+=1
    for i in range(1,10):
        count[i]=count[i]+count[i-1]
    for i in range(n-1,-1,-1):
        count[(l[i] // pos) % 10] -= 1
        b[count[(l[i]//pos)%10]]=l[i]
    for i in range(n):
        l[i]=b[i]
a=[int(x) for x in input("Enter list elements").split()]
k=max(a)
n=len(a)
pos=1
while k//pos>1:
    countsort(l,n,pos)
    pos=pos*10
print(a)