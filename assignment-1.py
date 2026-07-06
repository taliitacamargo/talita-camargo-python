name= "Talita"
age= 28
height= 5.2
is_Student= True
currentYear = 2026


print(f"My name is {name}, type: {type(name)}")
print(f"I am {age} years old, type: {type(age)}")
print(f"My height is {height}, type: {type(height)}")
print(f"It is {is_Student} that I am a student , type:{type(is_Student)}")

name = input("What is your name? ")
birthYear = int(input("What year were you born? "))
height = input("What is your height? ")
is_Student = input("Are you a student? ").lower() == "yes"
firstNum = float(input("Please enter a number "))
secNum = float(input("Please enter another number "))

age = currentYear - birthYear
mult = firstNum * secNum



print(f"Hi {name}! you're approximately {age} years old.")
print(f"Your height is {height}.")
print(f"It's {is_Student} that you're a student.")
print(f"Here are your numbers multiplied: {firstNum} * {secNum} = {mult}")


print("===========================")
print("        RECEIPT            ")
print("===========================")
item="Computer Org With MIPS"
print(f"Item:       {item}")
price=92.99
print(f"Price:      ${price}")
quantity=3
print(f"Quantity:   {quantity}")
print("---------------------------")
calc = price * quantity
total=f"Total:      {round(calc, 2)}"
print(total)
print("===========================")


name = input("What's your name? ")
town = input("What's your hometown? ")
hobby = input("What's your favorite hobby? ")
fact = input("What's a fun fact about you? ")
birthYear = int(input("What year were you born? "))
currentYear = 2026

age = currentYear - birthYear

print("╔══════════════════════════════╗")
print(f"       PROFILE: {name}")
print("╚══════════════════════════════╝")
print(f"Hometown:   {town}")
print(f"Hobby:      {hobby}")
print(f"Fun Fact:   {fact}")
print(f"Age:        {age}")
