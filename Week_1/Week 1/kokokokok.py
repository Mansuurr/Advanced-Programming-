#first = input("Your first name... ")
#last = input("Your last name...")
#age = input("How old are you... ")
#phone = input("Your phone number... ")
#print("Your full name: ",first, last)
#print("Your age: ",age)
#print("Your phone: ",phone)
#-------------------------------------------------------------------------------
#zarplata = list(map(int, input().split()))
#print(max(zarplata) - min(zarplata))
#-------------------------------------------------------------------------------
#a = float(input("Enter a number with two decimal places:"))
#w_n = int(a)
#f_n = int(round((a - w_n) * 100))
#new_n = f_n + w_n / 100
#print(new_n)
#-------------------------------------------------------------------------------
#n = int(input())
#if n >= 1:
#    print (n * (n + 1) // 2)
#else:
#    print ((1 + n) * (1 - n + 1) // 2)
#--------------------------------------------------------------------------------
#otvet = int(input("Enter result: "))
#zagadal = (r - 16) // 10
#print("Your number: ",x)
#---------------------------------------------------------------------------------
#a = float(input("Your first number: "))
#operation = input("Operation (+ - * /): ")
#b = float(input("Your second number: "))
#if operation == "+":
#    print(a + b)
#elif operation == "-":
#    print(a - b)
#elif operation == "*":
#    print(a * b)
#elif operation == "/":
#    print(a/b)
#-----------------------------------------------------------------------------------
#a = float(input("First number: "))
#operation = input("Operation (+ - * /): ")
#b = float(input("Your second number: "))
#if operation == "/":
#    print(a / b if b != 0 else "Error: division by zero")
#-------------------------------------------------------------------------------------
#word = input("Word: ")
#n = int(input("Number: "))
#for ch in word:
#    print(ch * n)
#-----------------------------------------------------------------------------------------
#ticket = input("Enter 6-digit ticket number ")
#if len(ticket) != 6 or not ticket.isdigit():
#    print ("Ne pravilniy nomer ticket")
#else:
#    first_half = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
#    second_half = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

#if first_half == second_half:
#    print("You are lucky")
#else:
#    print("Not Lucky")