import termcolor

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        base = ["A", 'C', 'G', 'T']
        for i in strbases:
            if i not in base:
                self.strbases = "ERROR"
                print("ERROR!")

                return
        self.strbases = strbases
        print("New sequence created.")

    def __str__(self):
        """Method called when the object is being printed"""
        # We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

def print_seqs(seqs_list):
        for element in seqs_list:
            print("Sequence ", seqs_list.index(element), ":", "Length: ", element.len(), element)

def generate_seqs(pattern, number):
    sequence = []
    for element in range(1, number+1):
        sequence.append(Seq(pattern * element))
    return sequence

# Main program

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
termcolor.cprint(print_seqs(seq_list1), "blue")


termcolor.cprint("List 2:", "green")
termcolor.cprint((print_seqs(seq_list2)), "green")
