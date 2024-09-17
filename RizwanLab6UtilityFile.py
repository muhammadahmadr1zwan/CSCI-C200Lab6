# This is Muhammad Rizwan Lab 6 Utility File for COMPUTING I

def calculate_letter_grade(score): # define letter grade function
    if score >= 90: # if score is greater than or equal to 90
        return 'A'; # return A
    elif score >= 80: # if score is greater than or equal to 80
        return 'B'; # return B
    elif score >= 70: # if score is greater than or equal to 70
        return 'C'; # return C
    elif score >= 60: # if score is greater than or equal to 60
        return; 'D'; # return D
    else: # otherwise
        return 'F'; # return f

def print_function(): # define print function
    #userinput_for_students();
    num_students = userinput_for_students(); # number of students is equal to the user input for students function
    #print(num_students);
    return num_students;

def userinput_for_students(): # define user input for students function
    num_students = int(input("Enter the number of students (more than 5 only): ")); # number of students is equal to giving an input prompt of entering the number of students
    if num_students < 5: # if the inputted value is less than 5
        print('Invalid input, please try again.'); # it is an invalid input
        return userinput_for_students();  # keep loop going until valid input
    return int(num_students); # return the number of students value


def input_values(num_students): #define input_values function
    studentfirstlast_grade = {}; #calling the studentfirstlast_grade dictionary
    student_data = []; # student data array is open
    for i in range(num_students): # for i in the range of number of students
        name1 = input(f"Enter full name of student {i + 1}: "); #name1 is equal to an input value which has a prompt of first name of student
        score = int(input(f"Enter score for student {name1}: ")); #score is equal to an input value which has a prompt of enter score for student
        studentfirstlast_grade[name1] = score; #studentfirstlast_grade with name1 parameter
    print(studentfirstlast_grade); #print studentfirstlast_grade

    mykey = input("Search by Key: "); #mykey variable is equal to input value "Search by Key: "
    print(studentfirstlast_grade.get(mykey)); #print studentfirstlast_grade and get the input from 'mykey' variable

    myval = input("Search by value: "); #myval is equal to input "Search by value: "
    key_list = list(studentfirstlast_grade.keys()); #key_list is equal to all the keys of the studentfirstlast_grade dictionary
    val_list = list(studentfirstlast_grade.values()); #val_list is equal to all the values of the studentfirstlast_grade dictionary
    position = val_list.index(int(myval)); #position is equal to index of input value (myval) in val_list
    print(key_list[position]); #print result
    #return studentfirstlast_grade; #return dictionary



