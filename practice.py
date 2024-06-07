# def check(n):
#     if n % 2 == 0:
#         return f'The Number {n} is even'
#     else:
#         return f'The number {n} is odd'

# ls = [1, 2, 3, 4, 5, 6, 7, 8]
# result = map(check, ls)
# print('\n'.join(result))

# passes=0
# failed=0

# for i in range(10):
#     inp=int(input("If pass, Press 1. If failed Press 2"))
#     if inp==1:
#         passes=passes+1
#     elif inp==2:
#         failed=failed+1
# print("Passed: ", passes)
# print("Failed: ",failed)

# a, b = map(int, input("Enter 2 numbers: ").split())
# print(a, b)

# def check(n):
#     if  ( n >100 or n<0):
#         print("Invalid")
# a=int(input("Enter your number: "))
# check(a)

# a='programming'
# for i in a:
#     print(i, end=' ')

# total=0
# lts=[2,3,4,5]
# for i in lts:
#     total=total+i
# print(total)    

# lst=[1,2,3,4]
# lst1=sum(lst)
# print(lst1)
# n=int(input("Enter a number: "))
# for i in range(1,11):
#     print(i,"x",n,"=",i*n)
# lst=[1,2,3,4]
# total=0
# for lst in range(len(lst)+1):
#       total=total+lst
# print(total)

# for number in range(10,5,-1):
#     print(number, end=' ')
# str='hello'
# str1=str[::-1]
# print(str1)
# for i in range(15):
#     if i==10:
#         break
#     print(i, end=' ')

# a=74
# print(a)
# numbers=[1,2,3,4]
# numbers.insert(3,a)
# numbers.append(5)
# numbers.append(6)
# numbers.extend([7,8,a])
# print(numbers)

# lst=[1,2,3,4]
#lst.reverse()
#sorted(lst)
# print(lst)


# def pal(n):
#     if n==n[::-1]:
#      print("true")
#     else: 
#      print("False")

# a=input("Enter a string: ")
# list(map(pal,a))







N = int(input("Enter the limit for the Fibonacci sequence: "))
a, b = 0, 1
print("Fibonacci Sequence:")
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b










