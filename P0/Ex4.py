from Seq0 import *

Genes = ["ADA", "FRAT1", "FXN", "U5", "RNU6_269P"]
Folder = "../Session-04/"
end = ".txt"
Bases = ["A", "C", "G", "T"]

for gene in Genes:
    for element in Bases:
        filename = Folder + element + end
        sequence = seq_read_fasta(filename)
        data = seq_count_base(sequence, element)
    print(data)