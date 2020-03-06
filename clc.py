import opr


data = input("I`m Command Line Calculator\nI`m calculate mines/sum/devide/multiple with this pattern:\nnumber1 <opr> number2\nLet`s GO:\n")

data = data.replace(" ","",data.count(" "))
oprIndex =0

if data.find("/") != -1:
    oprIndex = data.find("/")
elif data.find("+") != -1:
    oprIndex = data.find("+")
elif data.find("-") != -1:
    oprIndex = data.find("-")
elif data.find("*") != -1:
    oprIndex = data.find("*")
    
number1 =int(data[0:oprIndex])
number2 =int(data[oprIndex+1:])
result = opr.calculator(number1,number2,data[oprIndex])

print(result)








