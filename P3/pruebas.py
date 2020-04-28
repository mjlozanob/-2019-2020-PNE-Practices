import termcolor
"""from Seq0 import *

FOLDER = "../Session-04/"
#FILENAME = "../Session-04/U5.txt"
gene_list = ["U5", "FRAT1", "ADA", "FXN"]

msg = input("Enter a command: ")
msg = msg.split()
gene = msg[1]
if gene in gene_list:
    sequence = seq_read_fasta(FOLDER + "../Session-04/" + gene + ".txt")
    print(sequence)"""

#CURRENT PROGRAM

elif "REV" in msg:
termcolor.cprint("REV", "green")
msg = msg.split()
seq = Seq(msg[1])
reverse = seq.reverse()
print(reverse)

# -- Implement GENE command
FOLDER = "../Session-04/"
gene_list = ["U5", "FRAT1", "ADA", "FXN"]
msg = msg.split()
gene = msg[1]
if gene in gene_list:
    sequence = seq_read_fasta(FOLDER + "../Session-04/" + gene + ".txt")
    print(sequence)

elif "REV" in msg:
    msg = msg.split
    new_msg = msg[1]
    if new_msg in gene_list:
        sequence = seq_read_fasta(FOLDER + "../Session-04/" + gene + ".txt")
        print(sequence)
    else:
        termcolor.cprint("REV", "green")
        seq = Seq(new_msg)
        reverse = seq.reverse()
        print(reverse)
