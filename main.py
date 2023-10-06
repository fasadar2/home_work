def calculate(]num1,num2):
    if sign == "+":
    print(num1+num2)
    elif sign == "-":
    print(num1-num2)
    else:
        print("нет такой операции")
while True:
    string = input("введите 0 для выхода\nвведите строку с математическим выражением\nкалькулятор поддерживает только операции - и +\n>>>")
    if string.find("+"):
        sign = string[string.find("+")]
        num1 = string[:string.find("+")]
        num2 = string[string.find("+")+1:]
        calculate(sign,num1,num2)
    elif string.find("-"):
        sign = string[string.find("-")]
        num1 = string[:string.find("-")]
        num2 = string[string.find("-")+1:]
        calculate(sign,num1,num2)
    elif string.strip() =="0":
        break
    else:
        print("нет такой операции")