X = int(input("Enter first number: "))
Y = int(input("Enter second number: "))

total = X + Y
average = (X + Y) / 2
product = X * Y

if Y != 0:
    division = X / Y
else:
    division = "undefined (cannot divide by zero)"


print(f"Total: {total}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Division: {division}")

