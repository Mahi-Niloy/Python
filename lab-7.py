#Dictionary:

# student_Result={"Math":60,"Eng":70,"Physics":85}
# print(student_Result.values())
# print(student_Result.keys())
# print(student_Result.items())
# mean_result = sum(student_Result.values()) / len(student_Result)
# print(mean_result)


# student_marks = {
#     "Student1": {"Math": 60, "Eng": 70, "Physics": 85},
#     "Student2": {"Math": 65, "Eng": 73, "Physics": 60},
#     "Student3": {"Math": 55, "Eng": 75, "Physics": 78}


# for student, marks in student_marks.items():
#     average = sum(marks.values()) / len(marks)
   
    #print("The average marks for " + student + " are: " + str(average))
     
# average_marks = {}

# for student, marks in student_marks.items():
#     average = sum(marks.values()) / len(marks)
#     average_marks[student] = average

# print("Average-Marks=" + str(average_marks))



# strings = ["aabbcde", "str123str", "ccc123ddaa"]
# for idx, word in enumerate(strings, 1):
#     char_counts = []

   
#     for char in word:
#         if char.isalpha():  
#             found = False
#             for entry in char_counts:
#                 if entry[0] == char:
#                     entry[1] += 1
#                     found = True
#                     break
#             if not found:
#                 char_counts.append([char, 1])

    
#     output_str = [str(count) + char for char, count in char_counts]
#     output_str = ''.join(output_str)

   
#     print("SubString{} = [{}]".format(idx, output_str))


# # Set in Python:
numbers={10,9,11,13}
# number2={10,2,3}
# numbers.update(number2)
# numbers.add(8)
# print(numbers)
print(all(x%2==0 for x in numbers))
print(any(x%2==0 for x in numbers))
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))
print(list(enumerate(numbers)))






