f1=open("f1.txt","r")
w=f1.readlines()
f1.close()
f2=open("f1.txt","w")
old=input("enter old word to replace:")
new=input("enter new word to replace with:")
found=0
for i in range(len(w)):
    w[i]=w[i].strip()
    finders=w[i].find(old)
    if (finders!=-1):
        found=1
        w[i]=w[i].replace(old,new)
        w[i]=w[i]+'\n'
if found:
        f2.writelines(w)
        f2.close()
        f3=open("f1.txt","r")
        print(f3.read())
else:
    print("word not found!!")