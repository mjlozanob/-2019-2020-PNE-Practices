from Seq0 import *

Genes = ["ADA", "FRAT1", "FXN", "U5", "RNU6_269P"]
Folder = "../Session-04/"
end = ".txt"

for gene in Genes:
    filename = gene + Folder + end
    sequence = seq_read_fasta(filename)
    frag = sequence[:20]
    rev_seq = seq_reverse(frag)