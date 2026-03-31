print("🔢 Welcome to Smart Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

choice = input("Enter your choice: ")

if choice == "+":
    print(f"Result: {num1 + num2}")

elif choice == "-":
    print(f"Result: {num1 - num2}")

elif choice == "*":
    print(f"Result: {num1 * num2}")

elif choice == "/":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero not allowed")

else:
    print("Invalid choice")
