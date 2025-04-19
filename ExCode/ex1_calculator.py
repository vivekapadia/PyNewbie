#Problem statement : Implement Calculator using python


hint = '''
We support below mentioned operations:
1 > Addition [+]
2 > Subtraction [-]
3 > Multiplication [*] 
4 > Exponential [**]
5 > Division [/]
6 > Floor Division aka Divisor [//]
7 > Modulus aka remainder [%]

Type 'exit' to terminate the program!
'''

math_operand = {'1':'+','2':'-','3':'*','4':'**','5':'/','6':'//','7':'%'}

def math_operation(x, operator, y):

    result = ''
    x = float(x)
    y = float(x)
    operator = operator.lower()
    match operator:
        case '+' | '1':
            result = x + y
        case '-' | '2':
            result = x - y
        case '*' | '3':
            result = x * y
        case '**' | '4':
            result = x ** y
        case '/' | '5':
            result = x / y
        case '//' | '6':
            result = x // y
        case '%' | '7':
            result = x % y
        case _:
            result = '-1'

    return str(result)



print('Welcome to Calculator!')
print(hint,'\n')

while True:

    num_input1 = input('Enter first number!\n>')
    if num_input1.lower() == 'exit':
        break

    while not num_input1.replace('.','',1).isdigit():
        print('Invalid!\nPlease enter number only!')
        num_input1 = input('>')

        if num_input1.lower() == 'exit':
            break


    num_input2 = input('Enter second number!\n>')
    if num_input2.lower() == 'exit':
        break

    while not num_input1.replace('.','',1).isdigit():
        print('Invalid!\nPlease enter number only!')
        num_input2 = input('>')

        if num_input2.lower() == 'exit':
            break


    num_operand = input('Enter the number or the operand which you wish to use.\n>')
    if num_operand.lower() == 'exit':
        break

    result = math_operation(num_input1,num_operand,num_input2)
    if result == '-1':
        print('Invalid!\nPlease enter only the operand to be used.')
        num_operand = input('>')
        if num_operand.lower() == 'exit':
            break

        result = math_operation(num_input1, num_operand, num_input2)

    if num_operand.replace('.','',1).isdigit():
        num_operand = math_operand.get(num_operand)

    print(f'''Final Result!\n{num_input1} {num_operand} {num_input2} = {result}''')

    loop_again = input('Do you wish to use the program again! (Y/N)\n>')
    if loop_again.lower() != 'y' or loop_again.lower() != 'yes':
        break

print('Program Terminating!\nThanks for using caculator program!')







