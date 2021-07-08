myNumber = 20
myList = list(i for i in range(2, 21))
divided = list(1 for i in range(19))
zeroList = list(0 for i in range(19))
print(myList)
print(divided)
print(zeroList)
while myNumber < 999999999:
    for i in range(19):
        divided[i] = myNumber % myList[i]
    if divided == zeroList:
        print(myNumber)
        break
    else:
        myNumber += 20
