import http.client
import json
import termcolor
from Seq1 import *

GENES = {'FRAT1':'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN':'ENSG00000165060',
        'RNU6_269P': 'ENSG00000212379', 'MIR633': 'ENSG00000207552','TTTY4C': 'ENSG00000228296',
         'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078', 'KDR': 'ENSG00000128052',
         'ANK2':'ENSG00000145362'}

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'

for e in GENES:
    ID = GENES[e]
    URL = SERVER + ENDPOINT + ID + PARAMS

    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", ENDPOINT + ID + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)

    # -- tools
    bases = ['A', 'C', 'G', 'T']
    seq = Seq(response['seq'])
    max_count = 0
    # -- Print data
    termcolor.cprint('GENE: ', 'green', end='')
    print(e)
    termcolor.cprint('Description: ', 'green', end='')
    print(response['desc'])
    termcolor.cprint('Total lengh: ', 'green', end='')
    print(seq.len())
    for i in bases:
        count = seq.count_base(i)
        if count > max_count:
            max_count = count
            max_base = i
        result = round(count * 100 / seq.len(), 1)
        termcolor.cprint(i + ': ', 'blue', end='')
        print(count, end=' ')
        print('({}%)'.format(result))
    termcolor.cprint('Most frequent base: ', 'green', end='')
    print(max_base)
