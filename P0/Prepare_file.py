#THIS IS A TEMPORARY FILE IN WHICH I WILL TEST FUNCTION 2, AFTER THE FUNCTION WORKS
#THE FUNCTION MUST BE ADDED TO THE FILE SEQ0 AND THIS FILE SHOULD BE DELETED
from pathlib import Path
FOLDER = "../Session-04/"
FILENAME = "U5.txt"
def seq_read_fasta(filename) :
    file_contents = Path(filename).read_text().splitlines()
    print(file_contents[1:])

seq_read_fasta(FOLDER + FILENAME)