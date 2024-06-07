#Recursion

#list Slicing
n=[1,2,3,4,5,6,"python"]
# print(n[:])
# print(n[2:5]) 
# print(n[:5])
#print(n[-2:])
# print(n[::-1])

#list comprehension
#list_nums = [1, 2, 3, 4]
# n1 = [x**2 for x in list_nums]
# print(n1)

#import math
#list_nums = [1, 2, 3, 4]
# list_nums= [math.pow(i, 2) for i in list_nums]
# print("Square Elements:",list_nums)

# list_nums = [1, 2, 3, 4]
# squrar=[n[x]**2 for x in range(len(list_nums))]
# print(squrar)

#using list comprehension
n = [4, 3, 5, 6, 2, 1, 8]
even_squares = [num**2 for num in n if num % 2 == 0]
print(even_squares)

#using for loop
n = [4, 3, 5, 6, 2, 1, 8]
even_squares = []
for num in n:
    if num % 2 == 0:
        even_squares.append(num**2)
print(even_squares)