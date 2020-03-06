def calculator(number1, number2,opr):
    result = 0
    if opr == "+":
        result = sum(number1,number2)
    if opr == "-":
        result = mines(number1,number2)
    if opr == "*":
        result = multiple(number1,number2)
    if opr == "/":
        result = devide(number1,number2)
    return result

def sum(*args):
    sum =0
    for n in args:
        sum+=n
    return sum

def mines(number1, number2):
    return number1 - number2

def devide(number1, number2):
    return number1 / number2

def multiple(*args):
    mult = 0
    for n in args:
        mult *= n
