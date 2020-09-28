# Practice: Numbers

# ~ Create a types.py file and do the following task in it:
# ~ set the value to b so the result is 2.5

a = 2
b = 0.5

print(a + b)

print('\n')

# Practice: Strings

# ~ Solve the following problem:
# ~ make the program greet you using the name variable and 
# string formatting such as "Hello Misha!"

name = 'kaliyuga'
print(f'Hello {name.title()} !!!')

print('\n')

# Practice: Numbers

# ~ Correct the code to display a number 10 more than 
# the one entered, for example, the user entered 10, the 
# program displayed 20

v = input('print the number from 1 up to 10 : ')
v_int = int(v)

print(v_int + 10)

print('\n')

# Practice: Strings

# ~ correct the code to display the line 
# Hello, NAME! How are you?

name = input('type your name : ')

print(f'Hello, {name.upper()}! How are you???')

print('\n')

print(float('1'))    # 1.0
# print(int('2.5'))    # invalid literal for int() 
print(bool(1))       # True
print(bool(''))      # False
print(bool(0))       # False