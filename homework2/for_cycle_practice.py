# Cycle

# 1) Create a list of ten integers.
# 2) Display each number increased by 1.

digits = [10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20]
for digit in digits:
    print(digit + 1)
print('done')

print('\n')

# Cycle

# 1) Enter a string from the keyboard.
# 2) Print the same line vertically: 
#one character per console line.

word = input('enter a string please : ')
for letter in word:
    print(letter.title())

print('\n')

# Marks

# 1) Create a list from dictionaries with grades 
# of students of different classes of the school like 
# [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]

marks = [
    {'school_class': '1a', 'scores': [4.5, 4.5, 4.5, 4.6, 4.6, 4.6, 4.7, 4.7, 4.8, 4.8]} ,
    {'school_class': '1b', 'scores': [4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.8, 4.8]} ,
    {'school_class': '1c', 'scores': [4.8, 4.6, 4.4, 4.4, 4.9, 4.7, 4.5, 4.3, 4.1, 4.1]} ,
]

total_marks = marks[0]["scores"] + marks[1]["scores"] + marks[2]["scores"]

print('\n')

total_school_points = 0
for mark in total_marks:
    total_school_points += mark
    print(total_school_points)

print('\n')

tsp = float(total_school_points)

average_school_mark = 0
av = float(average_school_mark)

av = tsp / len(total_marks)
# 2) Calculate and display the GPA for the entire 
# school.
print(f'average score for entire school is : {av} ')

print('\n')

total_class_points = 0

for mark in marks[0]["scores"]:
    total_class_points += mark
    print(total_class_points)

tcp = float(total_class_points)

average_class_mark = 0 

acm = float(average_class_mark)

acm = tcp / len(marks[0]["scores"])
# 3) Calculate and display the average score for 
# each grade.
print(f'average mark for {marks[0]["school_class"]} class is : {acm}')

print('\n')

total_class_points = 0

for mark in marks[1]["scores"]:
    total_class_points += mark
    print(total_class_points)

tcp = float(total_class_points)

average_class_mark = 0 

acm = float(average_class_mark)

acm = tcp / len(marks[1]["scores"])
# 3) Calculate and display the average score for 
# each grade.
print(f'average mark for {marks[1]["school_class"]} class is : {acm}')

print('\n')

total_class_points = 0

for mark in marks[2]["scores"]:
    total_class_points += mark
    print(total_class_points)

tcp = float(total_class_points)

average_class_mark = 0 

acm = float(average_class_mark)
# 3) Calculate and display the average score for 
# each grade.
acm = tcp / len(marks[2]["scores"])
print(f'average mark for {marks[2]["school_class"]} class is : {acm}')