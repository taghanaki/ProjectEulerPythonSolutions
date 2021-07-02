sumOf3, sumOf5 = 0, 0
for num in range(1000):
    if num % 3 == 0:
        sumOf3 += num
    elif num % 5 == 0:
        sumOf5 += num

print(f"sum3= {sumOf3} & sum5= {sumOf5}")
print(sumOf3+sumOf5)
