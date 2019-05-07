def iscomposite(n):
if (n<1):
return false
if(n<3):
return false
if(n%2==0orn%3==0):
return true
i=5
while(i*i<n):
if(n%I==0orn%(i+2)==0):
return true
i=i+6
return false
print(' ')
print('true')if(is composition(11))else print('false')
print('true')if(is composition(15))else print('false')
