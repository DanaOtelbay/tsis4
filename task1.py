def f(n):
   a, b= 0, 1
   for _ in range(n):
      yield a+b
      a, b = b, a+b

it = f(10)

print(next(it))