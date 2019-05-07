def gcd(n,m):
id(m==0):
return n
else:
return gcd(m,n%m)
n=int(input('enter m:'))
m=int(input('enter m'))
print('the gcd is',end='')
print(gcd(n,m))
