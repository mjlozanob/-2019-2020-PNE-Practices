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
        print(numbers[4])
        print(numbers[9])
        print(numbers[14])
fibon(20)