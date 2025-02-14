# Question2:
# Write a Python program that prompts the user to create a password. The password must meet all the following criteria:

# At least 8 characters long.
# Contains at least one uppercase letter.
# Contains at least one lowercase letter.
# Contains at least one digit.
# Contains at least one special character from this set: !@#$%^&*().
# If the password meets all criteria, print "Strong password!". Otherwise, print a list of the conditions that were not met.
password=input("Enter a password: ")
if len(password)<8:
    print("Password must be at least 8 characters long.")
elif password.isupper():
    print("Password must contain at least one uppercase letter.")
elif password.islower():
    print("Password must contain at least one lowercase letter.")
elif password.isdigit():
    print("Password must contain at least one digit.")
elif password.isalnum():    
    print("Password must contain at least one special character from this set: !@#$%^&*().")
else:
    print("Strong password!")