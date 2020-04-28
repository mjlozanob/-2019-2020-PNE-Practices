from Client0 import Client
from Seq0 import *

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

# -- Import the sequence
FOLDER = "../Session-04/"
FILENAME = "../Session-04/FRAT1.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)

# -- Make the sequence into fragments and send it
new_seq = sequence[0:50]
string = ""
number = 1
c.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")
print("Gene FRAT1: "+sequence)
for element in new_seq:
    string = string + element
    if len(string) == 10:
        print("Fragment " + str(number)+ ":" + string)
        c.talk("Fragment " + str(number)+ ":" + string)
        number = number + 1
        string = ""







