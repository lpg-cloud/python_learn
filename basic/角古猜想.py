import random
def sal(num):
    print(num)
    if num==1:
        return ""
    if num%2:
        return sal(num*3+1)
    else:
        return sal(num/2)

sal(random.randint(0,100))
# print(random.randint(0,100))