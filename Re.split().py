"""
import re

ans = re.split(r",|\.", input())

for n in ans:
   print(n)
"""

regex_pattern = r",|\."

import re
print("\n".join(re.split(regex_pattern, input())))