# Euclidian application for greater common divisor
def gcd (x, y):
  while (y):
    x, y = y, x % y

  return x

print ("Greater common divisor for 60 and 48: ")
print (gcd (60, 48))