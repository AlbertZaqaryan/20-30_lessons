# տնային 149, 150, 151, 152, 153, 155, 156
# ----------------------------------------------
# 149
# def head(filename):
#     try:
#         with open(filename, 'r') as file:
#             mylist = file.readlines()
#         return ''.join(mylist[:5]).strip()
#     except FileNotFoundError:
#         return "No file"
    
# print(head('file.txt'))
# ----------------------------------------------
# 150
# def tail(filename):
#     try:
#         with open(filename, 'r') as file:
#             mylist = file.readlines()
#         return ''.join(mylist[-5:]).strip()
#     except FileNotFoundError:
#         return "No file"
    
# print(tail('file.txt'))
# ----------------------------------------------
# 151
# def cat(src_file, dst_file):
#     try:
#         with open(src_file, 'r') as file:
#             with open(dst_file, 'a') as file2:
#                 file2.write(file.read())
#         return 'Success'
#     except FileNotFoundError:
#         return 'Fail'
# print(cat('py.txt', 'file.txt'))
# ----------------------------------------------
# 152
# def numberic(file, new_file):
#     try:
#         with open(file, 'r') as file:
#             mylist = file.readlines()
#             with open(new_file, 'w') as file_:
#                 for i in range(0, len(mylist)):
#                     file_.write(f'{i + 1}). {mylist[i]}')
#         return 'OK'
#     except FileNotFoundError:
#         return 'Fail'
    
# print(numberic('file.txt', 'new_file.txt'))
# ----------------------------------------------
# 153
# def max_size(filename):
#     try:
#         with open(filename, 'r') as file:
#             mylist = file.read().split('\n')
#         mylist.sort(key=len)
#         return mylist[-1]
#     except FileNotFoundError:
#         return "Fail"
# print(max_size('file.txt'))
# ----------------------------------------------
# 155
# def word_count(filename):
#     try:
#         with open(filename, 'r') as file:
#             text = file.read().replace('\n', ' ').split(' ')
#         text = [i for i in text if i != '']
#         dict_ = {i:text.count(i) for i in text}
#         return sorted(dict_, key=dict_.get)[-1]
#     except FileNotFoundError:
#         print('Error')
# print(word_count('file.txt'))
# ----------------------------------------------
# 156
# def sum_of_numbers(filename):
#     try:
#         summ = 0
#         with open(filename, 'r') as file:
#             for i in file.read():
#                 if i.isdigit():
#                     summ += int(i)
#         return summ
#     except FileNotFoundError:
#         return 'Error'
# print(sum_of_numbers('file.txt'))
# ----------------------------------------------
# text = 'python 3.13'
# count = 0
# for i in text:
#     if i.isdigit():
#         count += 1
# print(count)


# import re

# text = 'python 3.13'
# print(re.findall(r'\d', text))
# import re

# with open('file.txt', 'r') as file:
#     text = file.read()

# print(re.findall(r'[a-zA-Z]+', text))
