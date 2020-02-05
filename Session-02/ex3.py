def fibon(n):
    numbers = [1]
    index = n
    f = 0  # first element of series
    s = 1  # second element of series
    if n <= 0:
        print("The requested series is", f)
    else:
        for x in range(1, n):
            next = f + s
            numbers.append(next)
            f = s
            s = next
        return (numbers)

def sum_fibo():
    n5 = fibon(5)
    n10 = fibon(10)
    sum5 = 0
    sum10 = 0
    for element in n5:
        sum5 = sum5 + element
    for element in n10:
        sum10 = sum10 + element
    print(sum5, sum10)
sum_fibo()