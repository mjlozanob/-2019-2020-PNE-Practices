from Seq1 import *

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

bases = ["A", "C", "G", "T"]

print("Sequence 1", ": (Lenght: ", s1.len(), ")", s1)
print("Bases: ", s1.count())
print("Reverse: ", s1.reverse())
print("Sequence 2", ": (Lenght: ", s2.len(), ")", s2)
print("Bases: ", s2.count())
print("Reverse: ", s2.reverse())
print("Sequence 3", ": (Lenght: ", s3.len(), ")", s3)
print("Bases: ", s3.count())
print("Reverse: ", s3.reverse())