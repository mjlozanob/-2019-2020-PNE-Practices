from pathlib import Path

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases="NULL"):
        if strbases == "":
            self.strbases = "NULL"
            print("Null sequence created")
            return
        bases = ["A", 'C', 'G', 'T']
        for i in strbases:
            if i not in bases:
                self.strbases = "ERROR"
                print("INVALID Seq!")
                self.length = 0

                return
        self.strbases = strbases
        print("New sequence created.")
        self.length = strbases

    def __str__(self):
        """Method called when the object is being printed"""
        # We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        bases = ["A", 'C', 'G', 'T']
        for e in self.strbases:
            if e not in bases:
                return 0
        return len(self.strbases)

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        result = {"A": self.count_base("A"), "C": self.count_base("C"), "G": self.count_base("G"),
                  "T": self.count_base("T")}
        return result

    def reverse(self):
        base = ["A", 'C', 'G', 'T']
        for element in self.strbases:
            if element not in base:
                return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        comp = {"A": 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        result = ''
        base = ["A", 'C', 'G', 'T']
        for element in self.strbases:
            if element not in base:
                return self.strbases
            else:
                for c in self.strbases:
                    result = result + comp[c]
                return result

    def read_fasta(self, filename):
        lines = Path(filename).read_text()
        body = lines.split("\n")[1:]
        self.strbases = "".join(body)
        return self

def print_seqs(seqs_list):
        bases = ["A", "C", "G", "T"]
        for element in seqs_list:
            print("Sequence ", seqs_list.index(element), ":", "Length: ", element.len(), element)
            for base in bases:
                print(base, ":", element.count_base(base))

def generate_seqs(pattern, number):
    sequence = []
    for element in range(1, number+1):
        sequence.append(Seq(pattern * element))
    return sequence

