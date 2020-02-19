from pathlib import Path

def seq_read_fasta(filename):
    string = ''
    file = Path(filename).read_text().splitlines()
    file = file[1:]
    for element in file:
        string = string + element

    return string

