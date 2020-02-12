from Seq0 import *
from pathlib import Path

genes = ["FRAT1.txt", "U5.txt"]

for element in genes:
    with open(element, 'r') as f:
        read_file = f.read()
        seq_len(read_file)