limit = 28124


def isAabundant(num):
    divisorsOfNum = []
    for i in range(1, num//2+1):
        if num % i == 0:
            divisorsOfNum.append(i)
    if sum(divisorsOfNum) > num:
        return True
    else:
        return False


def isSumAbundant(num):
    for item1 in abundantNums:
        if item1 < num:
            for item2 in abundantNums:
                if item2 < num:
                    if item1+item2 == num:
                        return True
                    elif item1+item2 > num:
                        break
    return False


abundantNums = []
for i in range(1, limit):
    if isAabundant(i):
        abundantNums.append(i)

sumAbundantNum = []
for i in range(1, limit):
    if isSumAbundant(i):
        sumAbundantNum.append(i)

notSumAbundantNum = list(range(1, limit))
for item in sumAbundantNum:
    notSumAbundantNum.remove(item)


print(sum(notSumAbundantNum))
