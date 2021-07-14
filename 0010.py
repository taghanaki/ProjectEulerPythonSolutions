def isPrime(x):
    for i in range(2, int((x/2)+1)):
        if x % i == 0:
            return False
    return True

sumOfPrimes = 0
for i in range(2, 2_000_000):
    if isPrime(i):
        sumOfPrimes += i

print(sumOfPrimes)
