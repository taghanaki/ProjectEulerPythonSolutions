maxRecurringCycle = 7
maxCount = 6
for i in range(8, 1000):
    remainder = 1 % i
    count = 0
    remaindersList = []
    while remainder not in remaindersList:
        remaindersList.append(remainder)
        remainder = (remainder * 10) % i
        count += 1

    if count > maxCount:
        maxCount = count
        maxRecurringCycle = i

print(maxRecurringCycle)
