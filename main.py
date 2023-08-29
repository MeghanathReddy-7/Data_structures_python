Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
a=input("enter expression")
b=""
c=[]
for i in a:
    if i.isalnum():
           b+=i
    elif i=='(':
        c.append(i)
    elif i==')':
          while c and c[-1] != '(':
            b+=c.pop()
          c.pop()
    else:
        while c and c[-1]!='(' and Priority[i]<=Priority[c[-1]]:
         b+=c.pop()
        c.append(i)
while c:
        b+=c.pop()
print(b, end="")



