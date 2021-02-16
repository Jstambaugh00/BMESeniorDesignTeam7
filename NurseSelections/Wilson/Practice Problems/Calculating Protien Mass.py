# Transcribing DNA into RNA
# Jacob Stambaugh
# 2/12/2021 wooo birthday time!

# Problem:
'''In a weighted alphabet, every symbol is assigned a positive real number called a weight.
A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights
of its symbols. The standard weight assigned to each member of the 20-symbol amino acid alphabet is the
monoisotopic mass of the corresponding amino acid.

Given: A protein string P of length at most 1000 aa.
Return: The total weight of P. Consult the monoisotopic mass table.'''

# Sample Input:
# SKADYEK

# Sample Output:
# 821.392

def main():
    # create mass table dict
    mass_dict={}
    f = open('Mass.txt')
    # loop through lines
    for line in f.readlines():
        # "fix" lines to format
        line = line.strip('\r\n')
        line = " ".join(line.split())
        line = line.split(' ')
        # populate dict
        mass_dict.update({line[0]: float(line[1])})

    # Calculate mass
    # read text file for DNA strand
    file = open('input.txt', 'r')
    seq = file.readline().strip('\r\n')

    mass = 0
    # loop through
    for i in seq:
        mass+=mass_dict.get(i)
    print(round(mass,3))
main()