#https://www.hackerrank.com/challenges/re-group-groups/problem
#Group(), Groups() & Groupdict()
import re
m = re.search(r"([A-Za-z0-9])\1+", input())

if m:
   print(m.group(1))
else:
   print("-1")