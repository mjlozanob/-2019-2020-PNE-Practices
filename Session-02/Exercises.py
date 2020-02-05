
def fibon():
    n1 = 0
    n2 = 1
    for i in range(16):
        sum = n1 + n2
        if n1 % 5 == 0:
            print(sum)
        else:
            pass
        n1 = n2
        n2 = sum


fibon()