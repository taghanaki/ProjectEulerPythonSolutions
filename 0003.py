def euler3(num):
     while num % 2 == 0:
         num = num // 2
     import math
     sq = int(math.sqrt(num)+1)
     ans = -1
     for i in range(3,sq,2):
         while num % i == 0:
             ans = max(ans,i)
             num = num // i
     ans = max(ans,num)
     return ans

print(euler3(600851475143 ))
