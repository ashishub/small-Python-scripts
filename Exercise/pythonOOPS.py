def printStatement(num):
  print('hello : ',num)

printStatement(2)

def square(num):
  return num ** 2

print('Square of a num', square(10))
print(list(range(15, 0, -5)))

print(type({'ashish' : [0, 1, 2], 'india': 'hello'}))
print(len(list(range(15, 0, -5))))

# iterator
def squareOfArray():
  arr = list(range(10))
  it = iter(arr)
  while True:
    try:
      print('printing from iterator: ',next(it))
    except StopIteration:
      break
  print('Original Array:', arr)
  # for n in arr:
  #   print(n, end=', ')
  # List Comprehension expression
  squaredValues = [ no ** 2 for no in arr]
  print('Squared Array:', squaredValues)
  # while(next(i) > -1):
  

squareOfArray()

print([n**2 for n in list(range(10))])