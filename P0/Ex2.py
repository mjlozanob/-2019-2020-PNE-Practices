from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"

seq = seq_read_fasta(FOLDER + FILENAME)

lseq = seq_len(seq[:20])

print(lseq)