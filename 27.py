def is_nbumber(s):
try:
float(s)
return true
except valueerror:
pass
try:
import unicodedata
unicodedata.numberic(s)
return true
except(typeerror,balueerror):
pass
return false
