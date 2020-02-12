def seq_ping(): #done
    print("ok")


def seq_complement(seq): #done
    for i in seq:
        if i == "A":
            print("T", end="")
        elif i == "T":
            print("A", end="")
        elif i == "G":
            print("C", end="")
        elif i == "C":
            print("G", end="")

def seq_len(seq): #done
    print(len(seq))

def seq_count_base (seq, base): #done
    count = 0
    for i in seq:
        if base == i:
            count += 1
    print(count)

def seq_count(seq): #done
    count_a = 0
    count_t = 0
    count_g = 0
    count_c = 0
    for i in seq:
        if i == "A":
            count_a += 1
        elif i == "T":
            count_t += 1
        elif i == "G":
            count_g += 1
        elif i == "C":
            count_c += 1
    data = {'A': count_a, 'T': count_t, 'C': count_c, 'G': count_g}
    print(data)


seq_count("ATGGGGAGCCCACAATAAAGAAGGGCTGA")