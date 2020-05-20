import http.server
import socketserver
from pathlib import Path
import http.client
import json
import termcolor
import re

# Data to connect to ensembl
SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'
# Define the server's port
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
            contents = Path('index.html').read_text()
        elif '/karyotype' in resource:
            ENDPOINT = '/info/assembly/'
            SPECIE = resource.split('=')
            SPECIE = SPECIE[1]

            # Connect with the server
            conn = http.client.HTTPConnection(SERVER)

            # -- Send the request message, using the GET method. We are
            # -- requesting the main page (/)
            try:
                conn.request("GET", ENDPOINT + SPECIE + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            # -- Read the response message from the server
            r1 = conn.getresponse()

            # -- Read the response's body
            data1 = r1.read().decode("utf-8")
            response = json.loads(data1)

            # -- Put data in html file

            karyotype = response['karyotype']
            string = ''
            for element in karyotype:
                string = string + element

            contents = f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
                <h1>Karyotype</h1>
                <p1>{string}</p1>

            </body>
            </html>"""

        else:
            contents = Path('error.html').read_text()



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