#DELETE THE FOLLOWING THREE LINES WHEN DONE
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

