def seq_ping():
    print("ok")

from pathlib import Path
FOLDER = "../Session-04/"
FILENAME = "U5.txt"
def seq_read_fasta(filename):
    # PRINTS THE FIRST 20 BASES OF THE FILE
    string = ''
    file = Path(filename).read_text().splitlines()
    file = file[1:]
    for element in file:
        string = string + element

    return string[:20]

def seq_len(seq):
    return len(seq)

def seq_complement(seq):
    for i in seq:
        if i == "A":
            print("T", end="")
        elif i == "T":
            print("A", end="")
        elif i == "G":
            print("C", end="")
        elif i == "C":
            print("G", end="")




def seq_count_base (seq, base):
    bases = ["A", "T", "G", "C"]
    for element in bases:


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


