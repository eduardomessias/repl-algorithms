# Calculate greater common divisor (GCD) by using
# Euclidian algorithm
def gcd (x, y):
  while (x):
    x, y = y, x % y

  return x

print ('Greater common divisor of 60 and 48: ')
print (gcd(60, 48))