# write a recursive function to generate nth fibonacci
#number

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)
n=9
for i in range(0,10):
 result = (i,fibonacci(n))
print(result)
