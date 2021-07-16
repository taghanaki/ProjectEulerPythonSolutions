def triangleNumber(num):
    ans= int(num * (num+1) / 2)
    factors=1
    for i in range(1, int(ans/2+1)):
        if ans % i==0:
            factors += 1
    if factors>=500:
        print (num,ans,factors)

for i in range (12_300,12_400):
    triangleNumber (i)
