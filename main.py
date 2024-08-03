# Import the pyttsx3 library for text-to-speech functionality
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Make the calculator talk
engine.say('''Calculator at your service. What's your math query? 
press 1 for addition, 
press 2 for subtraction, 
press 3 for division, 
and press 4 for multiplication. 
press 5 for floor division, 
press 6 for exponential, 
and press 7 for modulus.''')
engine.runAndWait()

print("Welcome to the Calculator Program!")

# Display the calculator menu
print('''Calculator at your service. What's your math query? 
press 1 for addition, 
press 2 for subtraction, 
press 3 for division, 
and press 4 for multiplication. 
press 5 for floor division, 
press 6 for exponential, 
and press 7 for modulus.''')
a = int(input("enter your choice:"))

# Perform addition
if a == 1:
    print("addition")
    num1 = int(input("enter first number :\n"))
    num2 = int(input("enter second number :\n"))
    total = num1 + num2
    print(total)
    engine.say(f"You chose addition. Your first number is {num1} and number 2 is {num2}, and your answer is {total} ")
    engine.runAndWait()
    print(f"Your first number is {num1} and number 2 is {num2}, and your answer is {total} ")

# Perform subtraction
elif a == 2:
    print("subtraction")
    num1 = int(input("enter first number :\n"))
    num2 = int(input("enter second number :\n"))
    sub = num1 - num2
    print(sub)
    engine.say(f"You chose subtraction. Your first number is {num1} and number 2 is {num2}, and your answer is {sub} ")
    engine.runAndWait()
    print(f"Your first number is {num1} and number 2 is {num2}, and your answer is {sub} ")

# Perform division
elif a == 3:
    print("division")
    num1 = int(input("enter first number :\n"))
    num2 = int(input("enter second number :\n"))
    div = (num1/num2)
    print(div)
    engine.say(f"You chose division. Your first number is {num1} and number 2 is {num2}, and your answer is {div} ")
    engine.runAndWait()
    print(f"Your first number is {num1} and number 2 is {num2}, and your answer is {div} ")

# Perform multiplication
elif a == 4:
    print("multiplication")
    num1 = int(input("enter first number :\n"))
    num2 = int(input("enter second number :\n"))
    mul = num1 * num2
    print(mul)
    engine.say(f"You chose multiplication. Your first number is {num1} and number 2 is {num2}, and your answer is {mul} ")
    engine.runAndWait()
    print(f"Your first number is {num1} and number 2 is {num2}, and your answer is {mul} ")

# Perform floor division
elif a == 5:
    print("floor division")
    num1 = int(input("enter first number :\n"))
    num2 = int(input("enter second number :\n"))
    floor_div = num1//num2
    print(floor_div)
    engine.say(f"You chose floor division. Your first number is {num1} and your second number is {num2} and your answer is {floor_div}. ")
    engine.runAndWait()
    print(f"Your first number is {num1} and second number is {num2} and answer is {floor_div}")

# Perform exponential
elif a == 6:
    print("exponential")
    num1 = int(input("enter first number :\n"))
    num2 = int(input("enter second number :\n"))
    expo = num1 ** num2
    print(expo)
    engine.say(f"You chose exponential. Your first number is {num1} and second number is {num2} and answer is {expo}")
    engine.runAndWait()
    print(f"Your first number is {num1} and second number is {num2} answer is {expo}")

# Perform modulus
elif a == 7:
    print("modulus")
    num1 = int(input("enter first number :\n"))
    num2 = int(input("enter second number :\n"))
    mod = (num1 % num2)
    print(mod)
    engine.say(f"You chose modulus and your first number is {num1} and your second number is {num2} and answer is {mod}")
else:
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(f"Wow, I'm impressed. You managed to enter the wrong choice. That takes skill. Please try again, and maybe use a little less skill this time.")
    engine.runAndWait()
    print(f"Wow, I'm impressed. You managed to enter the wrong choice. That takes skill. Please try again, and maybe use a little less skill this time.")
    


    
