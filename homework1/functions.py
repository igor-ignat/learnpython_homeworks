# Task 1

# 1) Create a function get_summ (one, two, delimiter = '&') 
# that takes two parameters, converts them to a string, 
# and returns them concatenated through delimiter
# 2) Call the function, passing two arguments "Learn" and 
# "python" to it, put the result in a variable and display 
# its value on the screen
# 3) Make the resulting string appear in title letters

def get_summ(one, two, delimeter = '&'):
    one = str(one)
    two = str(two)
    concatenated = one.title() + delimeter + two.title()
    return concatenated

g = get_summ('learn', 'python', '&')
print(g)

print('\n')

# Task 2

# 1) Create price.py file in the editor
# 2) Create a function format_price that 
# takes one argument, price
# 3) Cast price to integer (int type)
# 4) Return the line "Price: NUMBER rub."
# 5) Call the function with 56.24 on input 
# and put the result in a variable
# 6) Print the value of the variable with 
# the result to the screen

def format_price(price):
    price = int(price)
    message = (f'Price is : {price} rub.')
    return message

fp = format_price(56.24)
print(fp)