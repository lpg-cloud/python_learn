print(999-99)

count = 0
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if i != j and j != k and k != i:
                count +=1
                print(i,j,k,'\t')
print('共有',count,'个不重复的三位数')