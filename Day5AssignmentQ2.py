def selection_sort(l):
    for i in range(0,len(l)):
        minpos=i
        for j in range(i,len(l)):
            if l[j]<l[minpos]:
                minpos=j
        l[i],l[minpos]=l[minpos],l[i]
      
l=[int(i) for i in  input("Enter Elements:").split()] 
selection_sort(l)
print("Sorted List")
for i in l:
    print(i)