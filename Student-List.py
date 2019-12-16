# Author: William E McLean
# Intent: Accept a First Name, Last Name, and Student ID number from a user, and add them to list in a file
#         called students.txt which is automatically generated if needed. Then, output the list contents on screen.

# Declaring list to hold info from students.txt when it is read later
students = []

# Function for creating or adding to students.txt
def save_file(FName, LName, Studentid):
    # try block for exception handling, just in case something goes wrong.
    try:
        f = open("students.txt", "a") # opens/creates the file
        f.write(FName + " " + LName + " " + Studentid + "\n") # adds the name and ID, separated by spaces, and adds a line
        f.close() # closes the file
    except Exception:
        print("Could not save file")

# Function for reading the contents of students.txt
def read_file():
    # try block with exception handling, just in case
    try:
        f = open("students.txt", "r") # Open the file
        for student in read_students(f): #Loop whch pulls the data of each line, and adds it to student list
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")

# Function which helps to format the list in the .txt file for more easily read output, line by line
def read_students(f):
    for line in f:
        yield line

# Input validation - makes sure the name users enter is actually a name
def check_let(name):
    Good = True # Boolean value initialization
    if name.isalpha()==True:
        Good = True
    else: # Last names may contain spaces, apostrophes, or hyphens, which are not alpha, but are accaptable
        for letter in name: # Check each character for legitimate, non-alpha characters
            if letter != " " and letter != "'" and letter != "-" and letter.isalpha()!= True:
                Good = False # If any character is not acceptable, boolean becomes False
    return Good

# Input validation - makes sure the StudentID entered is a number
def check_numb(ID):
    Good = ID.isdigit()
    return Good

# Function to collect user input and save it to .txt file
def collect_input():
    # Initialize boolean variable used for data validation
    Good = False
    # Loop which will iterate until valid input is entered
    while Good == False:
        InFname = input("Enter student's first name: ")
        # Remove blank spaces before or after input
        InFname.strip()
        # Call function for data validation and sets boolean to result
        Good = check_let(InFname)
        if Good == False:
            # Error message for if invalid data is entered
            print("Invalid Entry.")
    # Set data validation boolean back to False
    Good = False
    # Loop which will iterate until valid input is entered
    while Good == False:
        InLname=input("Enter student's last name: ")
        # Remove blank spaces before or after input
        InLname.strip()
        # Call function for data validation and sets boolean to result
        Good = check_let(InLname)
        if Good == False:
            # Error message for if invalid data is entered
            print("Invalid Entry")

    # Set data validation boolean back to False
    Good = False
    # Loop which will iterate until valid input is entered
    while Good == False:
        InStudentid=input("Enter student's ID number: ")
        # Remove blank spaces before or after input
        InStudentid.strip()
        # Call function for data validation and sets boolean to result
        Good = check_numb(InStudentid)
        if Good == False:
            # Error message for if invalid data is entered
            print("Invalid Entry")

    # Call function to save user input to .txt file, and ensure first name and last name start with capitals
    save_file(InFname.capitalize(), InLname.capitalize(), InStudentid)

# Calling function for collecting and saving user input
collect_input()


# Call function to read contents of .txt file and place in students list
read_file()
print("Current list of students: ")
# Print students list one line at a time
for line in students:
    print(line)

# initialize finish variable which is used to determine whether there is more data to add
finish = input("Add another student? Y/N :")

# Loop will iterate as long as user enters Y or y, as a response, repeating entire program
while finish == "Y" or finish == "y":
    # Clear contents of students list so that when file is read from again, nothing is listed multiple times
    students.clear()
    collect_input()

    read_file()
    print("Current list of students: ")
    for line in students:
        print(line)

    finish = input("Add another student? Y/N :")

# Message for program end, when user stops entering Y or y for "Add another student?"
print("Exiting Program. Thank you.")

