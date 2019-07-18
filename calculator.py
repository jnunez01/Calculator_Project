
operation = input('What operation would you like to use?') 
first_number = input('First number?')
second_number = input('Second number?')


def operation_question(operation):
    addition_answer = (int(first_number)+int(second_number))
    subtraction_answer = (int(first_number)-int(second_number))
    multiplication_answer = (int(first_number)*int(second_number))
    division_answer = (int(first_number)/int(second_number))
    operation = operation.lower()
    if operation == 'addition':
        return(addition_answer)
    elif operation == 'Addition':
        return (addition_answer)
    elif operation == 'add':
        return (addition_answer) 
    elif operation == 'Add':
        return (addition_answer)
    elif operation == '+':
        return(addition_answer)
    elif operation == 'subtraction':
        return (subtraction_answer)
    elif operation == 'Subtraction':
        return(subtraction_answer)
    elif operation == 'minus':
        return(subtraction_answer)
    elif operation == 'Minus':
        return (subtraction_answer)
    elif operation == '-':
        return (subtraction_answer)
    elif operation == "multiplication" or operation == "Multiplication" or operation == '*' or operation == 'multiply' or operation == 'Multiply' or operation == 'x':
        return (multiplication_answer)
    elif operation == 'division' or operation == 'Division' or operation == 'divide' or operation == 'Divide' or operation == '/':
        return (division_answer)
    else:
        return('Try again')

print(operation_question(operation))




    