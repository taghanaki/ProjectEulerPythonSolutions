# https://taghanaki.com
n = 1001
totalSum = [1]
for i in range(3, n+1, 2):
    myPow = i**2
    mySum = myPow + (myPow-(i-1)) + (myPow-2*(i-1)) + (myPow-3*(i-1))
    totalSum.append(mySum)

print(sum(totalSum))
