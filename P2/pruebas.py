from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "../Session-04/FRAT1.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)

new_seq = sequence[0:50]
string = ""
for element in new_seq:
    string = string + element
    if len(string) == 10:
        print(string)
        string = ""

