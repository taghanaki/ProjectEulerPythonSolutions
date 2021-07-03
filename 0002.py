fibonacciNumbers = [0, 1]
sumOfEvens = 0

for i in range(2, 70):
    fibonacciNumbers.append(fibonacciNumbers[i-1]+fibonacciNumbers[i-2])
    if fibonacciNumbers[i] < 4000000:
        if fibonacciNumbers[i] % 2 == 0:
            sumOfEvens = sumOfEvens + fibonacciNumbers[i]
    else:
        break

print(fibonacciNumbers)
print(sumOfEvens)
