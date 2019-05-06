def validatestring(s):
letter__flag=false
number_flag=false
for i in s:
if i.isalpha():
letter_flag=true
if i.isdigit():
number__flag=true
return letter_flag and number_flag
print validatesstring('hasalphanum23')
print validatestring('some string')
