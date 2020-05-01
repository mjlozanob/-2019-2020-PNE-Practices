import termcolor
from Client0 import *
from Seq1 import *
from Seq0 import *
FOLDER = "../Session-04/"
gene_list = ["U5", "FRAT1", "ADA", "FXN"]
for element in gene_list:
    print("GENE "+element)
    msg = ("REV"+element)
    msg = msg.split()
if "REV" in msg:
    if msg[1] in gene_list:
        termcolor.cprint("GENE", "green")
        response = seq_read_fasta(FOLDER + "../Session-04/" + msg[1] + ".txt")
        print(response)
    else:
        termcolor.cprint("REV", "green")
        seq = Seq(msg[1])
        response = seq.reverse()
        print(response)