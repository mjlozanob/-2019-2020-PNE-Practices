#THIS IS A TEMPORARY FILE IN WHICH I WILL TEST FUNCTION 2, AFTER THE FUNCTION WORKS
#THE FUNCTION MUST BE ADDED TO THE FILE SEQ0 AND THIS FILE SHOULD BE DELETED

from pathlib import Path
FOLDER = "../Session-04/"
FILENAME = "U5.txt"


def seq_read_fasta(filename):
    string = ''
    file = Path(filename).read_text().splitlines()
    file = file[1:]
    for element in file:
        string = string + element

    return string


def seq_len(seq):
    print(len(seq))


"""for element in FILENAME:
    seq = seq_read_fasta(FOLDER + element)
    seq_len(seq)"""


base = ["A"]
seq = seq_read_fasta(FOLDER + FILENAME)
def seq_count_base(seq, base):
    count_A = 0
    for element in base:
        if element in seq:
            count_A += 1
    print(count_A)

seq_count_base(seq, base)




