def isPrime(num):    
    if num > 1:   
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            return num
    else:
        print(num,"is not a prime number")
primeNumbers=[1]
for i in range(2,111000):
    if (isPrime(i)):
        primeNumbers.append(i)

print(primeNumbers[10001])
