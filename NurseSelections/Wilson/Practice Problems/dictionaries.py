# Transcribing DNA into RNA
# Jacob Stambaugh
# 2/11/2021

# Problem:
'''Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by spaces.
 Words are case-sensitive, and the lines in the output can be in any order.'''

# Sample Input:
# We tried list and we tried dicts also we tried Zen

# Sample Output:
'''and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1'''

def word_counter(name):
    # empty dict
    word_dict={};
    # read text file
    file = open(name, 'r')
    sentance = file.readline().strip('\r\n')

    sentance=sentance.split(' ') # split by spaces

    # loop through and count
    for word in sentance:
        if word_dict.get(word,-1)==-1:
            word_dict.update({word:1})

        else: #update count
            word_dict.update({word: 1+ word_dict.get(word)})

    return word_dict

# run code
ans=word_counter('dict.txt')

for i in ans:
    print(i,ans.get(i))