from pathlib import Path
FOLDER = "../Session-04/"
FILENAME = "ADA.txt"
def seq_read_fasta(filename):
    string = ''
    file = Path(filename).read_text().splitlines()
    file = file[1:]
    for element in file:
        string = string + element

    return string

def seq_len(seq):
    print(len(seq))

seq_len(FOLDER + FILENAME)
