# Counting DNA Nucleotides
# Jacob Stambaugh
# 1/21/2020

# Problem:
''' A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length
of a string is the number of symbols that it contains. An example of a length 21 DNA string (whose alphabet contains the symbols
 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG." Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. '''

# Example string:
#AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# ans:
#20 12 17 21

def main():
    # get user input
    s=input('Enter DNA strand: ')
    total=[0,0,0,0] # pre-alocate space to count
    # Loop through and count
    for i in s:
        if i=='A':
            total[0]=total[0]+1
        elif i=='C':
            total[1]=total[1]+1
        elif i=='G':
            total[2]=total[2]+1
        else:
            total[3]=total[3]+1
    print('There are',total, 'A C G T base pairs respectively')


main()

# ALt approach:
'''AN alternative apporach would be to use recursion but does not provide any addtional benefits'''

# Has runtime complexity of O(N)