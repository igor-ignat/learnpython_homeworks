# Practice: Age

# 1) Ask the user to enter age using input and put 
# the result in a variable

# 2) Write a function that determines by age what 
# the user should do: study in kindergarten, school, 
# university or work

# 3) Call the function, passing it the user's age, and 
# put the result of the function into a variable

age = input("enter your age please : ")
age = int(age)

def users_age(age):
    if age >= 1 and age <= 2:
        message = ('oh baby , you have to stay with your parents !!!')
        return f'{message}'
    elif age >= 3 and age <= 6:
        message = ('you have to go to kindergarten !!!')
        return f'{message}'
    elif age >= 7 and age <= 18:
        message = ('you have to go to school !!!')
        return f'{message}'
    elif age >= 19 and age <= 23:
        message = ('you have to enter the university !!!')
        return f'{message}'
    else:
        message = ('wrong input , try again ,please !!!')
        return f'{message}'
    
    
ua = users_age(age)

print(ua)

print('\n')

# Practice: String Comparison

# 1) Write a function that takes two lines as input
# 2) Check if what is passed to the function is strings. 
# If not, return 0
# 3) If the strings are the same, return 1
# 4) If the lines are different and the first is longer, 
# return 2
# 5) If the lines are different and the second line is 
# 'learn', returns 3
# 6) Call the function multiple times, passing different 
# parameters to it and displaying the results

print('\n')

def strings_comparisson(line1, line2):

    line1 = input('enter first line : ')
    line2 = input('enter first line : ')

    line1 = str(line1)
    line2 = str(line2)

    if line1 == line2:
        return 1
    elif line2 == 'learn':
        return 3
    elif len(line1) > len(line2):
        return 2
    elif line1 or line2 == str:
        return 0
    else:
        return 'error'

sc = strings_comparisson('a', 'b')
print(sc)