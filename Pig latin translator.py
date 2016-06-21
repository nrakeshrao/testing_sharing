"""Pig latin Translator"""
pyg = 'ay'

original = raw_input('Enter a word:') #taking input

if len(original) > 0 and original.isalpha(): #checking for a valid word
    word = original.lower() #Converting original to lowercase
    first = word[0] #Extracting the 1st letter
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u': #Check for 1st letter
        new_word = word + pyg #Concatenation
        print new_word
    else:
        new_word = word[1:] + first + pyg # slicing and concatenating
        print new_word
    print original
else:
    print 'empty'