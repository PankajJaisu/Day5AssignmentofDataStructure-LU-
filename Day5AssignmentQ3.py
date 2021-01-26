def push(data):
    global size,s,top
    if top==size-1:
        print("Overflow")
        return
    top+=1
    s.insert(top,data)
def display():
    global size,s,top
    for i in range(top,-1,-1):
        print(s[i])
def  pop():
    global size,s,top
    if top==-1:
        print("UnderFlow")
        return
    top-=1
  
  
  
size=int(input("Enter Size of Stack:"))
s=list()
top=-1
push(84)
push(844)
push(854)
push(384)
pop()
display()