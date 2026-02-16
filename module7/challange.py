def calculator(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1-number2
    elif operator == "*":
        return number1*number2
    elif operator == "/":
        return number1/number2
    else :raise ValueError("unvalid operator")


try :
    num1 = float(input("Shkruaj numrin e pare:"))
    num2 = float(input("Shkruaj numrin e dyte:"))
    op = input("Shkruaj operacionin (+,-,*,/):"))

     result = calculate(num1,num2,op)
     print("rezultati eshte" ,result)

 except ValueError as ve:
    print("gabim ne input operator")

except ZeroDivisionError:
    print("gabim nuk lejohet pjestimi me zero")
    

