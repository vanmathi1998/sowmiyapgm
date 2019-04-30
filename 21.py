def sum2(b,c,a):
sum=0
i=0
while i<a:
sum=sum+b
b=b+c
i=i+1
return sum
a=int(input('enter n1:'))
b=int(input('enter n2:'))
c=int(input('enter n3:'))
print(sum2(b,c,a))
