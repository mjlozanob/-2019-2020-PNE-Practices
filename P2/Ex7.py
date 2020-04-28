from Client0 import Client
from Seq0 import *

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081

# -- Create a client object
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
print(c1)
print(c2)

# -- Import the sequence
FOLDER = "../Session-04/"
FILENAME = "../Session-04/FRAT1.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)

# -- Make the sequence into fragments and send it
new_seq = sequence[0:50]
string = ""
number = 1
c1.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")
c2.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")
print("Gene FRAT1: "+sequence)

# -- Make a list for the fragments
frag_list = []

new_seq = sequence[0:100]
string = ""
for element in new_seq:
    string = string + element
    if len(string) == 10:
        frag_list.append(string)
        print(string)
        string = ""

even_list = frag_list[::2]
odd_list = frag_list[1::2]

for e in even_list:
    c1.talk(e)
for i in odd_list:
    c2.talk(i)

