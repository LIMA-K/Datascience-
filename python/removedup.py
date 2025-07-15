l=[]
limit=int(input("enter limit:"))
for x in range(limit):
    val = int(input("Enter value:"))
    l.append(val)
a=set(l)
print(a)