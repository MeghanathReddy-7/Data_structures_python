priority={'+':1,'-':1,'*':2,'/':2,'^':3}
a=input("enter expression")
b=""
stack=[]
for i in a:
  if i.isalnum():
    b+=i
  elif i=='(':
   stack.append(i)
  elif i==')':
    while stack and stack[-1]!='(':
        b+=stack.pop()
    stack.pop()
  else:
    while stack and stack[-1]!='(' and  priority[i]<=priority[stack[-1]] :
        b+=stack.pop()
    stack.append[i]
while stack:
  b+=stack.pop()
print(b)
    