# Grade Calculator

# Welcome Message
print ("Grade Calculator. Enter the Project Grade, then the Exam Grade below.")


# Project Grades
project_score = int(input("What is the project score?:"))
Project_Perc = (project_score/72)*100
print('Your Project %: ', Project_Perc)

# Exam Grades
exam_score = int(input("What is the exam score?:"))
Exam_Perc = (exam_score/112)*100
print('Your Exam %: ', Exam_Perc)

#Calculating Grade
final_grade = Exam_Perc*0.4 + Project_Perc*0.6
print('Final Grade %: ', final_grade)

# Final Grade
if final_grade >= 80:
    print ("A")

elif final_grade > 69:
    print ("B")

elif final_grade > 59:
    print ("C")

elif final_grade > 49:
    print ("D")

elif final_grade <= 49:
    print ("Fail")




input('Thank you for your grade')