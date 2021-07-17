file_path = 'ProjectEuler\\013.txt'
f = open(file_path, 'r')
sum = 0
for line in f.readlines():
    sum += int(line)
str_sum = str(sum)
print(str_sum[0:10])
f.close()
