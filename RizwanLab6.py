#This program is for Muhammad Rizwan's Lab 7 Assignment for Computing I
#This program will be a Student Information Management System (SIMS) where a user can input a list of students and their scores and the program will output the letter grade
#from the listed scores.

print('  '); # blank space
print('This is a Student Information Management System (SIMS). Input the names of students and their scores in COMPUTING I, and the letter grade will be outputted.'); # descripton of program
print('   '); # blank space
print('STUDENT INFORMATION MANAGEMENT SYSTEM (SIMS)'); # program heading
print('\n'); # blank space

# Import all functions from the utility file
from RizwanLab7UtilityFile import *;

def main():
    # Get student data using the utility functions
    numstudents = print_function(); #numstudents equals to print function (being called here)
    input_values(int(numstudents)); #student_data is equal to inputvalues with the number of students as an integer
    # Process student data and calculate grades

# This block ensures that main() is called when the script is run
if __name__ == "__main__":
    main();
