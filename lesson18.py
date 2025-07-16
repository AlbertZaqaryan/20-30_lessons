# def asteroid_collision(asteroids):
#     i = 0
#     while i < len(asteroids):
#         if asteroids[i] > 0:
#             if i + 1 < len(asteroids) and asteroids[i+1] < 0:
#                 s = asteroids[i] + asteroids[i+1]
#                 if s > 0: 
#                     asteroids.pop(i+1)
#                 else:
#                     asteroids.pop(i)
#                     if s == 0: 
#                         asteroids.pop(i)
#                     i -= 1
#                 if i >= 0: continue
#         i += 1
#     return asteroids
# print(asteroid_collision([10, 2, -5]))
# ---------------------------------------------------------------------

# try:
#     x = int(input('Enter x: '))
#     y = int(input('Enter y: '))
#     print(x / y)
# except ZeroDivisionError:
#     print('Cannot divide by zero')
# except ValueError:
#     print('Enter only numbers')

# ---------------------------------------------------------------------

# try:
#     x = int(input('Enter x: '))
#     y = int(input('Enter y: '))
#     print(x / y)
# except:
#     print('Error')
# ---------------------------------------------------------------------


# try:
#     print(x
# except SyntaxError:
#     print('Error')
# ---------------------------------------------------------------------

# SyntaxError
# NameError
# ValueError
# TypeError
# ZeroDivisionError
# KeyError
# IndexError
# IndentationError
# FileNotFoundError
# ---------------------------------------------------------------------
    
# x = 10

# try:
#     x = y
#     x += 2
# except:
#     print('x+=2 does not working')

# print(x)
# ---------------------------------------------------------------------
# file = open('new.txt')
# print(file.read())
# ---------------------------------------------------------------------


# file = open('file.txt', encoding='utf-8')
# print(file.read())
# ---------------------------------------------------------------------


# file = open('../myfile.txt')
# print(file.read())
# ---------------------------------------------------------------------

# 'r' # read
# 'w' # write
# 'a' # append
# file = open("C:\\Users\\ASUS\\Desktop\\myfile.txt", encoding='utf-8', mode='r')
# print(file.read())
# file.close()
# ---------------------------------------------------------------------


# file = open('file.txt', mode='r')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline(3))
# print(file.readlines()[2].strip())

# file.close()
# ---------------------------------------------------------------------


# file = open('file.txt', mode='w')
# file.write('Gohary ushanum e')
# file.close()
# ---------------------------------------------------------------------


# file = open('file.txt', mode='a')
# for i in range(10):
#     file.write("\nGohary ushanum e")
# file.close()

# ---------------------------------------------------------------------
# file = open('file.txt', mode='r')
# text = file.read()
# mylist = text.split('\n')
# mylist.sort(key=len)
# print(mylist[-1])

# file.close()
# ---------------------------------------------------------------------
# file = open('IMG_2826.jpg', mode='rb')
# new_file = open('NEW_IMG1', mode='wb')
# new_file.write(file.read())
# file.close()
# new_file.close()
# ---------------------------------------------------------------------
# file = open('file.txt', mode='r')
# print(file.readlines())
# ---------------------------------------------------------------------


# file = open('file.txt', mode='w')
# file.write('Good')

# file.close()

# ---------------------------------------------------------------------

# file = open('file.txt', mode='a')
# file.write('\nGood')

# file.close()
# ---------------------------------------------------------------------

# file = open('file.txt', mode='r', encoding='utf-8')
# print(file.read())
# file.close()
# ---------------------------------------------------------------------


# file = open('IMG_2826.jpg', 'rb')
# new_file = open('new_IMG_2826.jpg', 'wb')
# new_file.write(file.read()[:-50000])
# file.close()
# new_file.close()

# ---------------------------------------------------------------------
# file = open('file.txt', 'r')
# print(file.read())
# file.close()
# ---------------------------------------------------------------------
# with open('file.txt', 'r') as file:
#     print(file.read())
# ---------------------------------------------------------------------
# file = open('file.txt', mode='r')
# count = 0
# text = file.read()
# for i in text:
#     if i.isdigit():
#         count += 1
# print(count)
# file.close()
# ---------------------------------------------------------------------
# def count_numbers(filename:str) -> int:
#     count = 0
#     try:
#         with open(filename, 'r') as file:
#             text = file.read()
#             for i in text:
#                 if i.isdigit():
#                     count += 1
#         return count
#     except FileNotFoundError:
#         print('No File')
#         return 0
# file_name = input('Enter filename: ')
# print(count_numbers(file_name))
# ---------------------------------------------------------------------







