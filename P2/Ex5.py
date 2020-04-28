from Client0 import Client
from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "../Session-04/U5.txt"
string = seq_read_fasta(FOLDER + FILENAME)

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

c.debug_talk("Sending the U5 Gene to the server...")
c.debug_talk(string)