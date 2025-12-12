#c = int(input())
#f = ((9 / 5) * c + 32)
#print(f)

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

#n = int(input())
#if n % 2 == 0:
#    print("even")
#else:
#    print("odd")

#def is_alive(health):
#    if health <= 0:
#        return False
#    else:
#        return True

month = int(input("vvedi month"))
def Sezon(chislo_mes):

    month = {1: "January", 2: "February", 3: "March",
        4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September",
        10: "October", 11: "November", 12: "December"}

    if chislo_mes in [12, 1, 2]:
        Sezon = "Na ulice sneg"
    elif chislo_mes in [3, 4, 5]:
        Sezon = "Na ulice vesna"
    elif chislo_mes in [6, 7, 8]:
        Sezon = "Na ulice solnceeee"
    else: 
        Sezon = "Na ulice padaut listie"

    print (f"Ty rodilcya v {month[chislo_mes]}. {Sezon}.")

Sezon(month)