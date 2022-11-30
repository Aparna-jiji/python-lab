list=[4,3,4,5,6,7,8]
list1=[65,22,33,22,44,55]
s=int(0)
c=int(0)
if len(list)==len(list1):
    print("same lenghth")
else:
        print("different length")
for i in range(0,len(list) and len(list1)):
    s=s+list[i]
    c=c+list1[i]
if (s==c):
         print("equal sum")
else:
         print("not equal sum")
print("elements is same")
l=[]
for i in range (0,len(list)):
   for j in range(0,len(list1)):
        if list[i]==list[j]:
            l.append(list[i] and list[j])
   else:
        continue
print(l)