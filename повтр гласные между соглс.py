#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
#Re.findall() & Re.finditer()

import re
a=re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', input().strip())
if a:
    for e in a: print(e)
else:
    print(-1)