from Seq0 import *

Genes = ["ADA", "FRAT1", "FXN", "U5", "RNU6_269P"]
Folder = "../Session-04/"
end = ".txt"

for element in Genes:
    filename = Folder + element + end
    sequence = seq_read_fasta(filename)
    length = seq_len(sequence)
    print("Gene ", element, "---> Length: ", length)