# i = 0

# i = i + 1
# print("The square of i is: " + str(i**2))

# i = i + 1
# print("The square of i is: " + str(i**2))

# i = i + 1
# print("The square of i is: " + str(i**2))

# i = i + 1
# print("The square of i is: " + str(i**2))

# i = i + 1
# print("The square of i is: " + str(i**2))

# for loop
# for i in range(1,11):
#   print(f"The square of {i} is {i**2}")

# while loop
# i = 0
# while i < 5:
#   i = i + 1
#   print(f"The square of {i} is {i**2}")

# Keep asking for an input from the user, till the input is "stop"

word = ""
while word != "stop":
  word = input("Enter a word: ")

  if word != "":
    length = len(word)

    if length < 5:
      print("Word is short")
    else:
      print("Word is long")
  else:
    print("Program stopped")