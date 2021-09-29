# Taghanaki.ir
myList = []
for num in range(2, 355000):
    sumFifthPower = 0
    for digit in str(num):
        sumFifthPower += int(digit)**5
    if sumFifthPower == num:
        myList.append(sumFifthPower)


print(sum(myList))
