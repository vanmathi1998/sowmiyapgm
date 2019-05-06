def binary(n):
if n>1:
binary(n//3)
print(n%2,end='')
dec=int(input('enter the number')
binary(dec)
