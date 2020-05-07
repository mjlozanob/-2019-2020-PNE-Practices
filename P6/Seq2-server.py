import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import *
from Seq0 import *
import re

# -- Tools
# -- List of sequences
seq_list = ["ATATATA", "CGCGCGC", "ACTGGCAT", "TAGCAGTAC","TTTGGGAA"]
# -- Tools to access genes
FOLDER = "../Session-04/"
end = ".txt"
# -- Bases
bases_list=["A","C","T","G"]
# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        req_line = self.requestline.split(' ')
        resource = req_line[1]
        print(resource)
        print(req_line)
        code = 200

        if resource == "/":
            contents = Path('form-1.html').read_text()
        elif '/ping' in resource:
            contents = Path('ping.html').read_text()
        elif '/get' in resource:
            msg = resource.split('=')
            index = int(msg[1])
            seq = seq_list[index]
            contents = Path('get.html').read_text().format(p1=seq,n1=index)
        elif '/gene' in resource:
            msg = resource.split('=')
            msg = msg[1]
            file = seq_read_fasta(FOLDER + msg + end)
            contents = Path('gene.html').read_text().format(gene=msg,seq=file)
        elif '/operation' in resource:
            msg = re.search('=(.+?)&', resource)
            msg = Seq(msg.group(1))
            divisor = msg.len()
            result_str =''
            if 'info' in resource:
                for e in bases_list:
                    count = msg.count_base(e)
                    result = round(count * 100 / divisor, 2)
                    result_str= result_str + e + ':'+ str(result)+'%\n'
                contents = Path('operation.html').read_text().format(ans=result_str,sequence=msg, op='info')
            elif 'comp' in resource:
                comp = msg.complement()
                contents = Path('operation.html').read_text().format(ans=comp, sequence=msg, op='comp')
            elif 'rev' in resource:
                rev = msg.reverse()
                contents = Path('operation.html').read_text().format(ans=rev, sequence=msg, op='rev')

        else:
            contents = Path('Error.html').read_text()

        # Generating the response message
        self.send_response(code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()