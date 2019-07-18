
operation = input('What operation would you like to use?') 
first_number = input('First number?')
second_number = input('Second number?')


def operation_question(operation):
    if operation == 'addition':
        return(int(first_number)+int(second_number))
    elif operation == 'Addition':
        return (int(first_number)+int(second_number))
    elif operation == 'add':
        return (int(first_number)+int(second_number))
    elif operation == 'Add':
        return (int(first_number)+int(second_number))
    elif operation == '+':
        return(int(first_number)+int(second_number))



print(operation_question(operation))
    