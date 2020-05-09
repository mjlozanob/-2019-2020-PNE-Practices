import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-EX01.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print("Total people in the database:", len(person))
for e in person:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(e['Firstname'], e['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(e['age'])

# Get the phoneNumber list
    phoneNumbers = e['phoneNumber']

# Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

# Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

    # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])