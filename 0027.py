import math
 
 
def isPrime(num):
    prime = True
    if num < 2:
        return False
    if num == 2:
        return True
    for n in range(3, int(math.sqrt(num)), 2):
        if num % n == 0:
            prime = False
            break
    return prime
 
 
def testEquation(a, b):
    n = 0
    while True:
        test = n**2 + a*n + b
        if isPrime(test):
            n += 1
        else:
            break
    return n
 
 
best = 0
bestA = 0
bestB = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        c = testEquation(a, b)
        if c > best:
            best, bestA, bestB = c, a, b
 
print(bestA*bestB)
