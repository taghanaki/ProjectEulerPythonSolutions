for i in range(1, 336):
    for j in range(i+1, 670):
        for k in range(j+1, 1000):
            if i+j+k == 1000:
                if ((i*i)+(j*j) == k*k):
                    print(i*j*k)
