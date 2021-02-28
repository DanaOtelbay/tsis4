'''
def f(n):
   a,  b = 0, 1
   for _ in  range(0, 10):
      yield a+b
      a, b = b, a+b

it = f(10)

print(next(it))
print(next(it))
'''

def f():
   for i in range(0,10):
      yield i

it = f()

for i in it:
   print(i, end=' ')