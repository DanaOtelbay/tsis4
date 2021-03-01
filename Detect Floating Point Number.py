'''
import re

n = int(input())

ans = []

for f in range(n):
   ans.append(bool(re.match(r"(\+|\-|\.)([0-9\. ]*)", input()  )))

for i in ans:
   print(i)
'''

import re

class Main():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.s = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))
                    
if __name__ == '__main__':
    obj = Main()