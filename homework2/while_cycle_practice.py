# Task 1
# Write a hello_user () function that asks the user 
# “How are you?” Using the input() function until they 
# say “Okay”

def hello_user(greeting):
    while True:
        hello_user = input('how are you ? : ')
        if hello_user == 'ok':
            return 'nice'
            break
        else:
            print(f'hello {hello_user} !!!')

hu = hello_user(input)
print(hu)

print('\n')

# Task 2
# ~ Create a dictionary like "question": "answer", for example: 
# {"How are you": "Ok!" "What are you doing?": "Programming"} 
# and so on.

# ~ Write a function ask_user () which, using the input() 
# function, asks the user to enter a question, and then, 
# if the question is in the dictionary, the program gives 
# it the appropriate answer. For example:
# User: What are you doing? Program: Programming

question_answer = {
    "question": ['do you have a brother ?','what are you doing ?', 'how old are you ?', 
                'what is your name ?', 'how are you ?', 'do you like learning ?'] , 
    "answer": "programming" ,
}

def ask_user(question):
    while True:
        users_question = input('user : ')
        if users_question in question_answer["question"]:
            return (f'programm : {question_answer["answer"]}')
            break
        else:
            print(f'programm : {users_question}')

q = ask_user(input)
print(q)