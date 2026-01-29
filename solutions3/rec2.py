# Practice Problem 1
Name = input("What's your name? ")
Length_of_Name = len(Name)
print(Length_of_Name - 5)

# Practice Problem 2
old_string = input("Please enter a string: ")
n = int(input("Enter a positive integer: "))
new_string = old_string[:n-1] + old_string[n:]
print(old_string)
print(new_string)

# Practice Problem 3
my_string = "Hello,I'm Yuanze Zhang"
length_of_my_string = len(my_string)
if (length_of_my_string > 10) or (length_of_my_string < 5):
    print("True")
else:
    print("False")

# Practice Problem 4
length_of_my_string2 = len("How many times is the letter e in this string?")
n = 0
for i in range(length_of_my_string):
    if my_string[i] == "e":
        n += 1
    else:
        n = n
print(f"The letter e occurs {n} times")



