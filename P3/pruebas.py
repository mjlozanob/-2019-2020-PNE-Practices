"""user = input("Enter a command")


s1 = "Raymond"
s2 = "Flick"
s3 = "Audie"

villagers = [s1, s2, s3]

if "GET" in user:
    number = user.replace("GET", '')
    index = int(number)

print(villagers[index-1])"""

from Seq1 import *
bases_list = ["A", "T", "G", "C"]
s1= input("Enter a sequence")
s1 = s1.split()
sequence = Seq(s1[1])
A=sequence.len()
print(A)
if "INFO" in s1:
    print("fine")
"""for e in bases_list:
    result = s1.count_base(e)
    percentage = result * 100/divisor
    print(e, ":", round(percentage,2),"%")
"""
