def fib_gen(maxNum):
  a, b = 0, 1
  for _ in range(maxNum):
    yield a
    a, b = b, a+b

fs = fib_gen(3)
while True:
  try:
    print(next(fs))
  except StopIteration:
    break
# print(next(fs))

# print(list(fib_gen(10)))
