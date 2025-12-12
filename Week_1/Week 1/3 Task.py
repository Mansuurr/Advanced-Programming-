a = float(input("Enter a number with two decimal places:"))
w_n = int(a)
f_n = int(round((a - w_n) * 100))
new_n = f_n + w_n / 100
print(new_n)