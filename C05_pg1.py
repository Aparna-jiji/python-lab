fn1=open("C05_pg1.txt",'r')
lines=fn1.readlines()
l1=[line.strip() for line in lines]
print(l1)