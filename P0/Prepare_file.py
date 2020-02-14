#THIS IS A TEMPORARY FILE IN WHICH I WILL TEST FUNCTION 2, AFTER THE FUNCTION WORKS
#THE FUNCTION MUST BE ADDED TO THE FILE SEQ0 AND THIS FILE SHOULD BE DELETED
from pathlib import Path
FOLDER = "../Session-04/"
FILENAME = "U5.txt"
def seq_read_fasta(filename) :
    string = ''
    file = Path(filename).read_text().splitlines()
    file = file[1:]
    for element in file:
        string = string + element
    print(string)

seq_read_fasta(FOLDER + FILENAME)