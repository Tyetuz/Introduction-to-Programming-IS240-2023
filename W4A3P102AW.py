#Promblem 102

def analyze_a_sentence(sentence):
    #Remove the period at the end if it exist
    if sentence.endswith('.'):
        sentence = sentence[:-1]
    #Split the sentence into words
    words = sentence.split()
    #Get the first and last words
    if words:
        first_word = words[0]
        last_word = words[-1]
        return first_word, last_word
    else:
        return None, None
    
    #User Input
sentence = input("Enter a sentence: ")
first, last = analyze_a_sentence(sentence)
    
    #Print statement
print(f"First word: {first}")
print(f"Last word: {last}")