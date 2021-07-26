def divisors(num):
    divisorsOfNum = []
    for i in range(1, (num//2)+1):
        if num % i == 0:
            divisorsOfNum.append(i)
    return divisorsOfNum


def sumOfDivisors(num):
    return sum(divisors(num))


amicableNums = []
for i in range(1,10001):
    n = sumOfDivisors(i)
    if sumOfDivisors(n) == i and n != i:
        amicableNums.append(n)

print(sum(amicableNums))
