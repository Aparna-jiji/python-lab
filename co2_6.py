n=input("enter a string: ")
s={}
for i in n:
    if i in s:
        s[i]=s[i]+1
    else:
            s[i]=1
print("count: ",s)