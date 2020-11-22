def cal(h,k):
    """
    有h个头，k只脚，返回有几只鸡几只兔
    """
    #设有i只鸡
    a = '没有找到结果！！！'
    for i in range(0,h+1):
        if i*2+4*(h-i)==k:
            a = f'共有{i} 只鸡，{h-i} 只兔子'
            print(a)
    if not a.startswith("共有"):
        print(a)

cal(5,10)