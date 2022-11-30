n=[]
a=int(input("enter a limit of numbers: "))
print("enter values: ")
for i in range(0,a):
    n.append(int(input()))
print("\n the list after asssigning: ")
for i in range(0,len(n)):
          if(n[i]>=100):
            print("over")
else:
            print(n[i])