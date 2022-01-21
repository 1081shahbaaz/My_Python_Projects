no1 = int(input("eneter first number: ")) #Take number 1 from the user
no2 = int(input("enter second number: ")) #Take number 2 from the user



oper = input("choose one operation: +, -, *, /: ") #tell user to choose which operation they want to do and store it in oper variable

if oper == '+':
    print(no1 + no2)  #if user choose + oper then it do sum of two number 
elif oper == '-':
    print(no1 - no2)  #if user choose - oper then it do subtract two number
elif oper == '*':
    print(no1 * no2)  #if user choose * oper then it do multiply of two number
elif oper == '/':
    print(no1 / no2)  #if user choose / oper then it do divide two number
else:
    print("you does not choose any operation")  #else part