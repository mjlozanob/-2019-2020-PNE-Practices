from Seq0_def import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"

string = seq_read_fasta(FOLDER + FILENAME)
string = string[:20]
print(string)



