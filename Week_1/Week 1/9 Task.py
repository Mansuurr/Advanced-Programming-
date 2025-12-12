ticket = input("Enter 6-digit ticket number ")
if len(ticket) != 6 or not ticket.isdigit():
    print ("Ne pravilniy nomer ticket")
else:
    first_half = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    second_half = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

if first_half == second_half:
    print("You are lucky")
else:
    print("Not Lucky")