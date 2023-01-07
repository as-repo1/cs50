x = float(input("give x: "))
y = float(input("give y: "))

z = x + y

print(z)

print(round(z)) #rounding the values

print(f"{z:,}") #use comma as a seperator

# rounding the floating point into nearest 
print(round(x / y, 2)) #it will round of the number to the 2'th digit (2nd)