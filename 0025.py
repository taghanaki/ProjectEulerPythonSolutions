fib = [1, 1]
i = 1
while len(str(fib[i])) < 1000:
    fib.append(fib[i]+fib[i-1])
    i += 1

print(i+1)
