from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "../Session-04/U5.txt"

string = seq_read_fasta(FOLDER + FILENAME)
string = string[:20]

print("DNA file: U5.txt")
print("The first 20 bases are: ")
print(string)



