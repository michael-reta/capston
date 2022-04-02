

number_grade = input('Please enter your number grade: ')
number_grade = int(number_grade)

if number_grade <= 59:
    letter_grade = "F"
elif number_grade <= 69:
    letter_grade = "D"
elif number_grade <= 79:
    letter_grade = "C"
elif number_grade <= 89:
    letter_grade = "B"
else:
    letter_grade = "A"

print(letter_grade)
