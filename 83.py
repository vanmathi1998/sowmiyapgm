class solution(object):
def reverse(self,x):
type x:int
negative=false
if(x<0):
x=x*-1
negative=true
x=x
sum=0
dig=1
strX=str(x)
lst=list(strx)
for i in lst:
sum+=ont(i)*dig
dig*=10
if(abs(sum)>2**32):
return0
elif(negative==true):
return sum*-1
else:
return sum
