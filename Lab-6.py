# st1="Welcome to python programming"
# st2="""Welcome to python, let's explore it"""
# print(st1.split())
# print(st2.split(","))


# user_input = input("Enter a single line string: ") 
# split_string = user_input.split() 
# print(split_string) 


# user_input = input("Enter a single line string: ")
# result = [alphabet.upper() for alphabet in user_input.split()]
# print(result)

# str1="welcome to python"
# x=str1.find("welcome")
# print(x)

# str1="welcom to python!"
# x=str1.rstrip("!")
# print(x)

# user_input = input("Enter a single line string: ")
# result = [alphabet.upper() for alphabet in user_input.split()]
# print(result)




# user_input = input("Enter a list of strings separated by commas: ")
# split_strings = user_input.split(',')
# strings_list = [string.upper() for string in split_strings]
# strings_list = [string.strip() for string in strings_list]
# strings_list.sort()
# print("Sorted and formatted strings:", strings_list)


# import random
# import string

# def modify_string(input_string):
#     if len(input_string) < 8:
#         return "Input string should be at least 8 characters long."

    
#     digits = ''.join(random.choices(string.digits, k=3))

#     special_characters = "!@#$%^&*()_+[]{}|;:,.<>?/`~"
#     random_special_chars = ''.join(random.choice(special_characters) for _ in range(3))

   
#     uppercase_string = input_string.upper()

 
#     modified_string = digits + uppercase_string[3:-3] + random_special_chars

#     return modified_string


# user_input = input("Enter a string (at least 8 characters): ")
# modified_output = modify_string(user_input)
# print(modified_output)



two_d_list = []
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        element = int(input("Enter an element: "))
        row.append(element)
    two_d_list.append(row)

print(two_d_list)
print(num_rows, num_cols)

# for row in two_d_list:
#     for element in row:
#         print(element, end=" ")
#     print()




