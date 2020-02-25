from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "../Session-04/U5.txt"

sequence = seq_read_fasta(FOLDER + FILENAME)
frag = sequence[:20]
com_frag = seq_complement(frag)

print("Gene U5: ")
print("Frag: ", frag)
print("Comp: ", com_frag)
