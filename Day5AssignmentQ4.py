def enqueue(data):
    global f,r,size,l
    if r==size-1:
        print("Queue is Full")
        return
    r+=1
    l.insert(r,data)
def dequeue():
    global f,r,size,l
    if r==-1:
        print("Queue is Empty")
        return
    elif r==f:
        r=-1
    else:
        f+=1
def display():
    global f,r,size,l
    if r==-1:
        print("Queue is Empty")
        return 
    for i in range(f,r+1):
        print(l[i])
r=-1
f=0
size=int(input("Enter Size of Queue:"))
l=list()
enqueue(844)
enqueue(843)
enqueue(84194)
enqueue(1814)
enqueue(484)
dequeue()
dequeue()
dequeue()
display()
