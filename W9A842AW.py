#W9A842AW.py
#Program to remove state names from SomeStates.txt that do not begin with a vowel

def main():
    filename = 'SomeStates.txt' #Text file containing 50 U.S. states
    states = read_file(filename) 
    filtered_states = filter_states(states)
    write_file(filename, filtered_states)
    
def read_file(filename):
    #Function to read the contents of the file
    with open(filename, 'r') as file:
        return file.readlines()

def filter_states(states):
    #Function to filter out states that do not begin with a vowel
    vowels = ('A', 'E', 'I', 'O', 'U')
    filtered_states = [state for state in states if state[0].upper() in vowels] #List comprehension taking the letter of each state name, converting it to uppercase, and checking if it is in the vowels tuple.
    return filtered_states

def write_file(filename, states):
    #Function to write the updated list back to the file
    with open(filename, 'w') as file:
        file.writelines(states)
        
main() #Resulting list will contain only 12 states with vowels