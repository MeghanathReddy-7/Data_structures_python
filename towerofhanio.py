def tower(n,sor,help,dest):
    if n==0:
        return
    else:
        tower(n-1,sor,dest,help)
        print(f"{n} is moved from {sor} to {dest}")
        tower(n-1,help,sor,dest)
n=int(input("enter number of elements"))
print("A:SOURCE\nB:HELPER\nC:DESTINATION")
tower(n,'A','B','C')