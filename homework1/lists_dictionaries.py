# Task

# 1 Create a list of numbers 3, 5, 7, 9, and 10.5
numbers = [3, 5, 7, 9, 10.5]
# 2 Display the contents of the list on the screen
print(numbers)
# 3 Add the line "Python" to the end of the list
numbers.append("Python")
# 4 Display the length of the list on screen
print(len(numbers))
# 5 Display the starting list item
print(numbers[0])
# 6 Display the last element of the list
print(numbers[-1])
# 7 Print list items 2 through 4 inclusive
print(numbers[2:5])
# 8 Remove the string "Python" from the list
del numbers[-1]

print(numbers)