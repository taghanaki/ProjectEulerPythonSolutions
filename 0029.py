# https://taghanaki.ir
mySet = {4}
for a in range(2, 101):
    for b in range(2, 101):
        mySet.add(a**b)

print(len(mySet))
