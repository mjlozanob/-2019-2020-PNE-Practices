from pathlib import Path
FOLDER = "../Session-04/"
FILENAME = "U5.txt"

def seq_ping():
    print("ok")

def seq_read_fasta(filename):
    # Returns a string with all the bases

    string = ''
    file = Path(filename).read_text().splitlines()
    file = file[1:]
    for element in file:
        string = string + element

    return string

def seq_len(seq):
    # Returns the length of the sequence

    return len(seq)

def seq_count_base(seq, base):
    # Given a base, it returns the number of times it appears in the sequence

    count = 0
    for element in seq:
        if element == base:
            count += 1

    return count

def seq_count(seq):
    # Returns a dict with the number of times each base appears in the sequence

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

    return data

def seq_reverse(seq):
    # Returns the reversed sequence

    reverse_seq = []
    index = len(seq)
    while index > 0:
        reverse_seq += seq[index - 1]
        index = index - 1
    print(reverse_seq)

def seq_complement(seq):
    # Returns the complementary sequence

    complement = ""
    for i in seq:
        if i == "A":
            complement = complement + "T"
        elif i == "T":
            complement = complement + "A"
        elif i == "G":
            complement = complement + "C"
        elif i == "C":
            complement = complement + "G"

    return complement






