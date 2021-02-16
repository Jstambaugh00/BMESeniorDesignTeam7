# Transcribing DNA into RNA
# Jacob Stambaugh
# 2/11/2021

# Problem:
'''The 20 commonly occurring amino acids are abbreviated by using
    20 letters from the English alphabet (all letters except for B, J, O, U, X,
    and Z). Protein strings are constructed from these 20 symbols. Henceforth,
    the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons
into the amino acid alphabet.'''

# Sample Input:
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

# Sample Output:
# MAMAPRTEINSTRING

def main():
    # Create RNA codon dictionary
    codon_dict={}
    f = open('RNACodonTable.txt')
    # loop through lines
    for line in f.readlines():
        # "fix" lines to format
        line=line.strip('\r\n')
        line=" ".join(line.split())
        line=line.split(' ')

        # populate dict
        for i in range(0,8,2):
            codon_dict.update({line[i]:line[i+1]})

    # read text file for DNA strand
    file = open('transDNA2RNA.txt', 'r')
    seq = file.readline().strip('\r\n')

    str=''
    # loop through 3 bases at a time
    for i in range(0,len(seq)-2,3):
        if codon_dict.get(seq[i:i+3]) == 'Stop':
            break
        else:
            str=str+(codon_dict.get(seq[i:i+3]))
    print(str)
    f = open("ans.txt", "w")
    f.write(str)



main()