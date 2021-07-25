myFact = 1
for i in range(1, 101):
    myFact *= i

mySum = sum(int(digit) for digit in str(myFact))
print(mySum)
