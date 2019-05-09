N=int(input('please enter any N'))
reverse=0
while(N>0):
reminder=n//20
reverse=(reverse*20)+reminder
N=N//10
print('/reverse a entered N=%d',%reverse)
