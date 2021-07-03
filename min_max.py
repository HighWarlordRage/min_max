#Title: Project-3a
print("How many integers would you like to enter?")
integer = int(input( ))
print("Please enter",integer,"integers.")
starting_value = 0
min = int(input( ))
max = 0
for integers in range(integer-1):
    integers = int(input( ))
    if integers<min:
        min = integers;
    if integers>max:
        max = integers;
print("min:",min)
print("max:",max)





