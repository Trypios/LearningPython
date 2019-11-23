# SIMPLE FUNCTION EXAMPLE

def pig_latin(word='manolis'):
    '''
    THIS FUNCTION TAKES A SINGLE WORD.
    IF THE WORD STARTS WITH A VOWEL: ADDS 'ay' AT THE END OF THE WORD
    IF THE WORD STARTS WITH A CONSONANT: IT TAKES THE FIRST LETTER, PUTS IT AT THE END OF THE WORD ALONG WITH 'ay'
    '''
    first_letter = word[0]
    if first_letter.lower() in 'aeiou':
        return(word+'ay')
    else:
        return (word[1:]+first_letter+'ay')

print(pig_latin('kokos'))