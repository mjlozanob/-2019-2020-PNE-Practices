with open("dna.txt","r") as f:
    num_c = 0
    num_a = 0
    num_t = 0
    num_g = 0

    for element in f:
        if "C" == element:
            num_c += 1
        elif "A" == element:
            num_a += 1
        elif "T" == element:
            num_t += 1
        elif "G" == element:
            num_g += 1

    print("The total length is:", len(dna))
    print("A:", num_a)
    print("C:", num_c)
    print("G:", num_g)
    print("T:", num_t)
