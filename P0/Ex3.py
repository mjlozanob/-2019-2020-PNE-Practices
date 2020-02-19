from Seq0_def import *

Genes = ["ADA","FRAT1", "FXN", "U5", "RNU6_269P"]
Folder = "../Session-04/"
end = ".txt"

for element in Genes:
    filename = Folder + element + end
    seq_len(filename)