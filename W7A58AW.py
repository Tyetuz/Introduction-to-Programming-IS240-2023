#Problem 58: Vowel Words
#Program to check if a word is a vowel word

def is_vowel_word(word):
    vowels = "aeiou" #Check if each vowel is present in the word
    for vowel in vowels:
        if vowel not in word:
            return False
        return True

def main():
    word = input("Enter a word: ").lower() #Ask the user to enter a word
    if is_vowel_word(word): #Check if the word is a vowel word
        print(f"{word} is a vowel word:")
    else:
        print(f"{word} is not a vowel word.")
        
if __name__=="__main__":
    main()