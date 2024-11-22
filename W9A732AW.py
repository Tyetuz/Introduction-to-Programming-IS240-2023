#W9A732AW.py
#Write a program that displays the months containing the letter r

import os
print(os.getcwd())

#Define an empty list called months that contain only the months which contain an r
months = []

def main(): #Every program starts with def main():
    #Main entry point for the script calls functions fillList, deleteNoRs and displayMonths
    global months #Required by program
    fill_List() #Will add the contents of Months.txt to this list
    months = delete_No_Rs() #Will remove all months not containing letter r
    display_Months() #Will print the list of months containing the letter r
    
def fill_List():
    global months
    infile = open("Months.txt", 'r') #Open Months.txt and 'r' (read through the file)
    for line in infile: #Read file line by line
        months.append(line.rstrip()) #Append the month and strip white spaces from the right side
    infile.close() #Close the file Months.txt
    
def delete_No_Rs():
    reduced_list = [] #Append r months to the empty list
    for i in range(12): #Read range line by line
        if 'r' in months[i]: #If "r" found in month add to empty list
            reduced_list.append(months[i])
    return reduced_list #Return and replace the original list of months
    
def display_Months():
    #Print function to format the output
    print("The R months are:") #Header
    print(*months, sep = ", ") #Months containing the letter "r"

#Call the main function
main()

