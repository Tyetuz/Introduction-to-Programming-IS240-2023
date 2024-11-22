#Problem 32: Pig Latin
#Program to translate a word into pig latin

def pig_latin(word):
    #Check if the first letter is a vowel or consonant
    if word[0] in "aeiou":
        #If it starts with a vowel, append "way"
        return word + "way"
    
    elif word[0] not in "aeiou":
        #If word starts with consonant, move the consonant to the end and append "ay"
        return word[1:] + word[0] + "ay"
    
    else:
        return word
    
#Input for the word to translate
word_to_translate = input("Enter word to translate:").strip().lower()

#Translate to pig latin
translate_word = pig_latin(word_to_translate)

#Print statement
print(f"The word in Pig Latin is{translate_word}.")
        