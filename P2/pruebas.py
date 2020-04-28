from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "../Session-04/FRAT1.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)
frag_list = []

new_seq = sequence[0:100]
string = ""
for element in new_seq:
    string = string + element
    if len(string) == 10:
        frag_list.append(string)
        print(string)
        string = ""

print(frag_list[::2])
print(frag_list[1::2])