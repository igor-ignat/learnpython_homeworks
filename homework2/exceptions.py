def cut_cake(people):
    parts = 1 / people
    print(f'each person will receive {parts} of the cake')

cut_cake(5)

print('\n')

# cut_cake(0) 

# Traceback (most recent call last):
#  File "exceptions.py", line 9, in <module>
#    cut_cake(0)
#  File "exceptions.py", line 2, in cut_cake
#    parts = 1 / people
# ZeroDivisionError: division by zero

def cut_cake(people):
    try:
        parts = 1 / people
        print(f'each person will receive {parts} of the cake')
    except ZeroDivisionError:
        print("you cannot divide by 0 !!!")
    except TypeError:
        print("unsupported operand type(s) for /: 'int' and 'str'")
    
cut_cake('5')

print('\n')

def cut_cake(people):
    try:
        parts = 1 / people
        print(f'each person will receive {parts} of the cake')
    except (ZeroDivisionError, TypeError, KeyboardInterrupt):
        print("division is impossible !!!")
    
cut_cake('5')

print('\n')

def cut_cake(people):
    try:
        parts = 1 / people
        print(f'each person will receive {parts} of the cake')
    except KeyboardInterrupt:
        print("division is impossible !!!")

while True:
    p = cut_cake(5)
    print(p)

# Exercise 1

# Rewrite the hello_user() function from the while task 
# so that it intercepts KeyboardInterrupt and writes "Bye!" 
# and exited with the break statement

