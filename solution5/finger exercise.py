my_string = input("Enter a string: ")
new_string = ""
for i in range(len(my_string)):
    if i % 2 == 0:
        new_string = new_string + my_string[i]
print(new_string)
