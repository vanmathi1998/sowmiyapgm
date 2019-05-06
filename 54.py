def prime(n)
if(n(<1))
return false
for i in range(2,n):
if n%i==0:
return false
return true
def printprime(n):
for i in range(2,n+1):
if printprime(i):
print(i,end='')
if__name__''__main__':
n+6
