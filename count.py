'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    
    #for i in range(len(text)):
    #    k = text[i]
    #    amount = 0
    #    j = 0
    #    d = dict()
    #    for j in range(len(text)):
    #        if text[j] == k:
    #            amount = amount + 1
    #        j = j + 1
    #    dict['text[i]'] = amount
        #print(text[i], amount)
    #    i = i + 1
    #i = 0
    
    #for i in range(len(dict())):
    #    print(dict["text[i]"])
        #dict['text[i]'], )
    #    i += 1
    i = 0
    count = 0
    d = dict()
    
    for i in range(len(text)):
        if text[i] in d and text[i] != ' ':
            d[text[i]] += 1
        elif text[i] != ' ':
            d[text[i]] = 1
    for i in d:
        print (i, d[i])
    
def count_char_insensitive(text):
    string = text.lower()
    i = 0
    count = 0
    d = dict()
    for i in range(len(text)):
        if string[i] in d:
            d[string[i]] += 1
        else:
            d[string[i]] = 1
    for i in d:
        print (i, d[i])
# bonus task:
def count_char_ordered(text):
    pass
    # add your code here 

text1 = "I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn't really happy" # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
count_char_ordered(text2)

