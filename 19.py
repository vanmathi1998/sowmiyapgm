n=8
factorial=1
if n<0
print('not exist for a negative number')
elif n==0:
print('the factorial of o is 1')
else:
for i in range(1,n+1):
factorial=factorial*i
print('the factorial of',n,'is',factorial)
