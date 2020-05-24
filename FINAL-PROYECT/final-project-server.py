import http.server
import socketserver
from pathlib import Path
import http.client
import json
import termcolor

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
        count = 0

        if resource == "/":
            contents = Path('index.html').read_text()

        elif resource == '/listSpecies':
            ENDPOINT = '/info/species/'
            # -- Get info from server
            conn = http.client.HTTPConnection(SERVER)
            try:
                conn.request("GET", ENDPOINT + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
            r1 = conn.getresponse()
            data1 = r1.read().decode("utf-8")
            response = json.loads(data1)
            # -- Elaborate response
            info = response['species']
            species = []
            string = ''
            for element in info:
                species.append(element['common_name'])
            for i in species:
                string = string + '\n' + i
                count = count + 1
            contents = f"""<!DOCTYPE html>
                       <html lang="en">
                       <head>
                           <meta charset="UTF-8">
                           <title>Species</title>
                       </head>
                       <body style="background-color: springgreen;">
                           <p1>The total number of species in ensemble is: 286</p1> <br>
                           <p1>The names of the species are</p1> <br> <br>
                           <textarea style="border: none; overflow: hidden; resize:none; background-color: springgreen" rows={count}>{string}    
                       </textarea>
                       </body>
                       </html>"""
        elif 'limit' in resource:
            ENDPOINT = '/info/species/'
            LIMIT = resource.split('=')
            LIMIT = LIMIT[1]
            # -- Get info from server
            conn = http.client.HTTPConnection(SERVER)
            try:
                conn.request("GET", ENDPOINT + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
            r1 = conn.getresponse()
            data1 = r1.read().decode("utf-8")
            response = json.loads(data1)
            # -- Elaborate response
            info = response['species']
            species = []
            string = ''
            for element in info:
                species.append(element['common_name'])
            try:
                if LIMIT == '':
                    for i in species:
                        string = string + '\n' + i
                        count = count + 1
                else:
                    LIMIT = int(LIMIT)
                    for i in species[:LIMIT]:
                        string = string + '\n' + i
                        count = count + 1
                contents = f"""<!DOCTYPE html>
                           <html lang="en">
                           <head>
                               <meta charset="UTF-8">
                               <title>Species</title>
                           </head>
                           <body style="background-color: springgreen;">
                               <p1>The total number of species in ensemble are: 286</p1> <br>
                               <p1>The limit you have selected is: {LIMIT}</p1> <br>
                               <p1>The names of the species are: </p1> <br> <br>
                               <textarea style="border: none; overflow: hidden; resize:none; background-color: springgreen" rows={count}>{string}    
                               </textarea>
                               </body>
                               </html>"""

            except ValueError:
                contents = Path('error.html').read_text()

        elif '/karyotype' in resource:
            try:
                ENDPOINT = '/info/assembly/'
                SPECIE = resource.split('=')
                SPECIE = SPECIE[1]

                conn = http.client.HTTPConnection(SERVER)

                try:
                    conn.request("GET", ENDPOINT + SPECIE + PARAMS)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()

                data1 = r1.read().decode("utf-8")
                response = json.loads(data1)

                karyotype = response['karyotype']
                string = ''
                for element in karyotype:
                    string = string + '\n' + element
                    count = count + 1

                contents = f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Species</title>
            </head>
            <body style="background-color: springgreen;">
                <h1>The names of the chromosomes are: </h1>
                <textarea style="border: none; overflow: hidden; background-color: springgreen" rows={count}>{string}    
            </textarea>
            </body>
            </html>"""
            except KeyError:
                contents = Path('error.html').read_text()


        elif '/chromosomeLength' in resource:
            try:
                ENDPOINT = '/info/assembly/'
                INFO = resource.split('&')
                specie = INFO[0].split('=')
                specie = specie[1]
                number = INFO[1].split('=')
                number = int(number[1])
                # Connect with the server
                conn = http.client.HTTPConnection(SERVER)

                # -- Send the request message, using the GET method. We are
                # -- requesting the main page (/)
                try:
                    conn.request("GET", ENDPOINT + specie + PARAMS)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()

                data1 = r1.read().decode("utf-8")
                response = json.loads(data1)

                data2 = response['top_level_region']
                list = []
                for i in data2:
                    list.append(i['length'])
                ans = list[number - 1]
                contents = f"""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>Chromosome length</title>
                            </head>
                            <body style="background-color: springgreen;">
                                <h1>Chromosome length</h1>
                                <p1> The length of the chromosome is: {ans}<p1>

                            </body>
                            </html>"""
            except IndexError:
                contents = Path('error.html').read_text()
            except KeyError:
                contents = Path('error.html').read_text()
            except ValueError:
                contents = Path('error.html').read_text()
        else:
            contents = Path('error.html').read_text()

        print(contents)
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