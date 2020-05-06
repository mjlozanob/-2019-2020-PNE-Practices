import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        command = self.requestline.split(' ')
        command2 = command[1]
        command2 = command2[1:]
        output = ''
        print(command2)

        if command2 == "":
            command2 = 'index.html'
        try:
            output = Path(command2).read_text()
            code = 200
        except:
            print("ERROR")
            output = Path('Error.html').read_text()
            code = 404

        self.send_response(code)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(output.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(output.encode())

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