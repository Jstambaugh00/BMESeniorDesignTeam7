# Jacob Stambaugh
# 1/26/21
# Complementing DNA Strand Problem

'''In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.'''

def main():
    # read text file
    file=open('ComplementDNA.txt','r')
    dnastrand=file.readline()
    # loop through and change
    cstrand=''
    for letter in dnastrand:
        if letter == 'A':
             cstrand = cstrand + "T"
        elif letter == 'G':
            cstrand = cstrand + "C"
        elif letter == 'T':
            cstrand = cstrand + "A"
        else :
            cstrand = cstrand + "G"

    # Reverse
    cstrand=cstrand[::-1]
    # Save to file
    f = open("ans.txt", "w")
    f.write(cstrand)
    print(cstrand)
main()

'''Could also solve using recursion for same eff'''