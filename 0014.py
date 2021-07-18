def even_nums(num):
    return int(num/2)


def odd_nums(num):
    return (3*num+1)


chain_dict = {10: 13}
for my_n in range(14, 1000000):
    my_num = my_n
    chain = 1
    while my_num != 1:
        if my_num % 2 == 0:
            my_num = even_nums(my_num)
            chain += 1
        else:
            my_num = odd_nums(my_num)
            chain += 1
    chain_dict[chain] = my_n

print(max(chain_dict.items()))
