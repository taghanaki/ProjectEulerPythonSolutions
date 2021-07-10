sumOfSquares = 0
squaresOfSum = 0

for i in range(1, 101):
    sumOfSquares += (i**2)
    squaresOfSum += i

difference = (squaresOfSum**2)-sumOfSquares
print(difference)
