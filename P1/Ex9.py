from Seq1 import*

FOLDER = "../Session-04./"
gene = 'U5.txt'


s1 = Seq("")
s1.read_fasta(FOLDER + gene)
print("Sequence 1", ": (Lenght: ", s1.len(), ")", s1)
print("Bases: ", s1.count())
print("Reverse: ", s1.reverse())
print("Complement:", s1.complement())