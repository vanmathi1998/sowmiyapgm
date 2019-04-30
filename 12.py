c=int(input('enter number:'))
temp=c
rev=0
while(c>0):
dig=c%10
rev=rev*10+dig
c=c//10
if(temp==rev):
print('palindrome')
else:
print('no')
