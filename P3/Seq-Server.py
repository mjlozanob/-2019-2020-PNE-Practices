import socket
import termcolor
from Seq1 import *
from Seq0 import *

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("SEQ Server configured")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")


    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Implement PING command

        if msg == "PING":
            response = "OK!"
            termcolor.cprint("PING command!", "green")
            print(response)

        # -- Split the message to identify the command

        msg = msg.split()

        # -- Implement GET command

        s1 = "AAC"
        s2 = "GTC"
        s3 = "TCT"
        s4 = "GTA"
        s5 = "TTG"
        seq_list = [s1, s2, s3, s4, s5]
        if "GET" in msg:
            termcolor.cprint("GET", "green")
            index = int(msg[1])
            response = seq_list[index]
            print(response)

        # -- Implement INFO command

        elif "INFO" in msg:
            termcolor.cprint("INFO", "green")
            bases_list = ["A", "T", "G", "C"]
            seq = Seq(msg[1])
            divisor = seq.len()
            print("Sequence: ", seq)
            print("Total length: ", seq.len())
            for e in bases_list:
                result = seq.count_base(e)
                percentage = result * 100 / divisor
                print(e, ":", round(percentage, 2), "%")

        # -- Implement COMP command

        elif "COMP" in msg:
            termcolor.cprint("COMP", "green")
            seq = Seq(msg[1])
            complement = seq.complement()
            print(complement)

        # -- Implement REV  and GENE command

        FOLDER = "../Session-04/"
        gene_list = ["U5", "FRAT1", "ADA", "FXN"]

        if "REV" in msg:
            if msg[1] in gene_list:
                termcolor.cprint("GENE", "green")
                seq = seq_read_fasta(FOLDER + "../Session-04/" + msg[1] + ".txt")
                print(seq)
            else:
                termcolor.cprint("REV", "green")
                seq = Seq(msg[1])
                reverse = seq.reverse()
                print(reverse)

        #-- Print the received message

            #print(f"Message received: {msg}")
            # -- Send a response message to the client
            #response = "ECHO: " + msg

        # -- The message has to be encoded into bytes
        #cs.send(response.encode())

        # -- Close the data socket
        cs.close()