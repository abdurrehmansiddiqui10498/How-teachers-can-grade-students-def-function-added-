# How can teachers grade students
def grading(Name, Class, grade, percentage):
    
    if percentage >= 90:
        grade = "A"
        print(f"{Name} of class {Class} has acheived {percentage}% percentage and grade {grade}")
        print("Congradulations")
    elif percentage >= 80 and percentage <= 89:
        grade = "B"
        print(f"{Name} of class {Class} has acheived {percentage}% percentage and grade {grade}")
        print("Good Job")
    elif percentage >= 70 and percentage <= 79:
        grade = "C"
        print(f"{Name} of class {Class} has acheived {percentage}% percentage and grade {grade}")
        print("Good")
    elif percentage >= 60 and percentage <= 69:
         grade = "D" 
         print(f"{Name} of class {Class} has acheived {percentage}% percentage and grade {grade}")
         print("Average Good")
    elif percentage >= 50 and percentage <= 59:
        grade = "E"
        print(f"{Name} of class {Class} has acheived {percentage}% percentage and grade {grade}")
        print("Average Good")  
    else:
        grade = "F"
        print(f"{Name} of class {Class} has acheived {percentage}% percentage and grade {grade}")
        print("Better luck next time")
Name = "Ahmed"
Class = "VII-A"
percentage = 86
grade = None
grading(Name, Class, grade, percentage )

Name = "Sam"
Class = "III-A"
percentage = 76
grade = None
grading(Name, Class, grade, percentage )

Name = "Pam"
Class = "IX-B"
percentage = 96
grade = None
grading(Name, Class, grade, percentage )

Name = "Penny"
Class = "I-A"
percentage = 59
grade = None
grading(Name, Class, grade, percentage )




