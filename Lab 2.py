#Welcome to the Lab grade calculator!
print('Welcome to the LAB grade calculator!')
#This line asks the user for their name
name = input('What are we calculating grade for?')
print()
#This line asks the user for their lab grade
user_lab = int(input('Enter the Labs grade?'))
#This itteration checks if the input the user gave for lab grade is < or > 100
if user_lab < 0:
      print('The lab value should have been zero or greater. It has been changed to zero')
      print()
elif user_lab > 100:
      print('The lab value should have been 100 or less. It has been changed to 100')
      print()
else:
      print()
#This line asks the user for their EXAMS grade
user_exam = int(input('Enter the EXAMS grade?'))
#This if-else statements checks if the input the user gave for exams grade is < or > 100
if user_exam < 0:
      print('The EXAMS value should have been zero or greater. It has been changed to zero')
      print()
elif user_exam > 100:
      print('The EXAMS value should have been 100 or less. It has been changed to 100')
      print()
else:
      print()
#This line asks the user for their attendance grade
user_attendance = int(input('Enter the Attendance grade?'))
#This if-else statements checks if the input the user gave for attendance grade is < or > 100
if user_attendance < 0:
      print('The Attendance value should have been zero or greater. It has been changed to zero')
      print()
elif user_attendance > 100:
      print('The Attendance value should have been 100 or less. It has been changed to 100')
      print()
else:
      print()
#This line calculates the weighted grade of the user by multiplying each grade by their percentage out 100 and then summing it all together
Weighted_grade = round((user_lab*0.7)+(user_exam*0.2)+(user_attendance*0.1), 1)
print('The weighted grade for', name, 'is', Weighted_grade)
#This if-else statements assigns a letter grade for the weighted grade of the user
if Weighted_grade >= 90:
      print(name, 'has a letter grade of A')
elif Weighted_grade >= 80:
      print(name, 'has a letter grade of B')
elif Weighted_grade >= 70:
      print(name, 'has a letter grade of C')
elif Weighted_grade >= 60:
      print(name, 'has a letter grade of D')
else:
      print(name, 'has a letter grade of F')
print('Thanks for using the Lab grade calculator')
#Thanks for using the lab grade calculator
