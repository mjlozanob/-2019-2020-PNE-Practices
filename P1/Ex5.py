from Seq1 import *

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

seq_list = [s1, s2, s3]

base = ["A", "C", "T", "G"]

for element in seq_list:
    for item in base:
        result = []
        count = count_base(item, element)
        r2= result.append(base).append(":").append(count)
    print(r2)


