
a = ('l','w','z')
def get_solwst_child():
    """
    l1(9) l2 l3 = w1(8) w2 w3 = z1 z2 z3
    """
    
    b=["l","w"]

    surplus(b)
    

def surplus (current):
    current=current.copy()
    if len(current)==9:
        print(current)
    else:
        c=current[-1]#最后一个孩纸的姓氏

        for i in a:
            current_num=get_count(i,current)
            if i!=c and current_num<3:
                current.append(i)
                current=current.copy()
                surplus(current)

                
        
            


def  get_count(item,lis):
    """
    得到list--lis中元素item的个数
    """
    num =0;
    for i in lis:
        if i ==item:
            num +=1
    return num

b=["l","w"]

surplus(b)


