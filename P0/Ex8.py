from Seq0 import *

Genes = ["ADA", "FRAT1", "FXN", "U5", "RNU6_269P"]
Folder = "../Session-04/"
end = ".txt"
Bases = ["A", "C", "G", "T"]
base_list = []

for gene in Genes:
    for element in Bases:
        filename = Folder + gene + end
        sequence = seq_read_fasta(filename)
        data = seq_count(sequence)
    print("Gene", gene, ": Most frequent Base: ", max(data, key=data.get))
