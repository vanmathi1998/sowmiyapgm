def min(list,n):
final_list=[];
for i in range(0,n):
min1=9999999;
for j in range(len(list)):
if list[j]<min1:
min1=list[j]
list1.remove(min1);
print(final_list);
list1=(4,5,6,7,8,33,321);
n=2;
min(list1,n)
