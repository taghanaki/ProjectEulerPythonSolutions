powerDigitSum = 0
powerDigit = 2

for i in range(1, 1000):
    powerDigit *= 2

for digit in str(powerDigit):
    powerDigitSum += int(digit)

print(powerDigitSum)
