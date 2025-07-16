# set1 = {1, 1, 2, 3, 4, 1, 1, 1}
# print(set1)


# set1 = {2, 3, 1, 2, 1}
# set2 = {1, 2}
# print(set2.issubset(set1))


# set1 = set()
# print(type(set1))


# dict1 = {'a':1}
# set1 = {'a', 1}

# set1 = {1, 2, 3}
# set1.add(4)
# set1.discard(2)
# print(set1)


# set1 = {2, 3, 1, 11, 2, 3, 4, 5}
# set2 = {7, 4, 1, 2, 3, 6, 5}
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.union(set2))
# print(set1.intersection(set2))

# mylist = [2, 2, 2, 3, 1, 2, 2, 2, 3, 4]
# print(list(set(mylist)))

# ----------------------------------------------------------------
# user1 = [[5, 17], [20, 30], [45, 62], [78, 93]]
# user2 = [[1, 8], [32, 33], [34, 60], [70, 74], [83, 92], [97, 100]]
# duration = 9
# i = 0
# j = 0
# while True:
#     if i == len(user1) or j == len(user2):
#         print('ERROR')
#         break
#     if user2[j][1] >= user1[i][0] >= user2[j][0] or user1[i][1] >= user2[j][0] >= user1[i][0]:
#         inter_1 = max(user1[i][0], user2[j][0])
#         inter_2 = min(user1[i][1], user2[j][1])
#         if inter_2 - inter_1 >= duration:
#             print(inter_1, inter_2)
#             break
#         elif user1[i][1] > user2[j][1]:
#             j += 1
#         else:
#             i += 1
#     else:
#         if user1[i][1] < user2[j][0]:
#             i += 1
#         else:
#             j += 1
# ----------------------------------------------------------------
# import random
# import msvcrt
# import os


# monkey_i = random.randint(1, 18)
# monkey_j = random.randint(1, 18)

# banana_i = random.randint(1, 18)
# banana_j = random.randint(1, 18)
# points = 0
# while True:
#     for i in range(20):
#         for j in range(20):
#             if i == monkey_i and j == monkey_j:
#                 print('🐒', end=' ')
#             elif i == banana_i and j == banana_j:
#                 print('🍌', end=' ')
#             else:
#                 print('.', end='  ')
#         print()
#     print(f'Monkey score = {points}\nEnter W|A|S|D===>')
#     cord = msvcrt.getwch()
#     if cord == 'w':
#         monkey_i -= 1
#     elif cord == 's':
#         monkey_i += 1
#     elif cord == 'a':
#         monkey_j -= 1
#     elif cord == 'd':
#         monkey_j += 1
#     else:
#         break
#     if monkey_i == banana_i and monkey_j == banana_j:
#         points += 1
#         banana_i = random.randint(1, 18)
#         banana_j = random.randint(1, 18)
#     os.system('cls')
# ----------------------------------------------------------------
# mylist = [2, 0, 1, 3, 1] # False
# mylist = [1, 0, 4, 2] # False
# mylist = [1, 1, 2, 0, 1, 1] # True
# index = 0
# while True:
#     if index >= len(mylist):
#         print(False)
#         break
#     elif mylist[index] == 0 and index < len(mylist) - 1:
#         print(False)
#         break
#     elif index == len(mylist) - 1:
#         print(True)
#         break
#     else:
#         index += mylist[index]
# ----------------------------------------------------------------
# mylist = [1, 2, 3, 4, 5, 6, 7]
# newlist = [[]]
# for i in range(0, len(mylist)):
#     for j in range(i + 1, len(mylist) + 1):
#         newlist.append(mylist[i:j])
# newlist.sort(key=len)
# print(newlist)
# ----------------------------------------------------------------
