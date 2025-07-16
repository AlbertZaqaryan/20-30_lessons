# list_ = [7, 10, 5, 6, 9, -4, 50, 6]
# list_.sort()
# print(list_)

# -----------------------------------------------------------
# def coins(count, amount):
#     if count == 0 or amount == 0:
#         return count == amount
#     return coins(count - 1, amount - 25) or coins(count - 1, amount - 10) or coins(count - 1, amount - 5) or coins(count - 1, amount - 1)
# print(coins(8, 64)) 
# -----------------------------------------------------------
# def decoding(mylist, count=1):
#     if len(mylist) == 1:
#         return [mylist[0], count]
#     elif mylist[0] == mylist[1]:
#         return decoding(mylist[1:], count + 1)
#     else:
#         return [mylist[0], count] + decoding(mylist[1:], count=1)

# print(decoding(["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B", "B"]))

# ["A", 12, "B", 4, "A", 6, "B", 2]
# -----------------------------------------------------------
# def decode(mylist, count=1, newlist=[]):
#     if len(mylist) == 0 and len(newlist) == 1:
#         return count
#     elif len(mylist) == 1 and len(newlist) == 0:
#         return count
#     elif len(mylist) == 1 and len(newlist) == 1:
#         return len(mylist) + len(newlist)
#     elif len(mylist) == 0 and len(newlist) > 1:
#         return decode(newlist, count=1, newlist=[])
#     elif len(mylist) == 1 and len(newlist) > 1:
#         return decode(mylist=[], count=1, newlist = newlist + [count])
#     elif mylist[0] == mylist[1]:
#         return decode(mylist[1:], count + 1, newlist)
#     else:
#         return decode(mylist[1:], count=1, newlist= newlist + [count])
# print(decode([1, 1, 1]))
# [3, 2, 2, 2, 1, 3]
# [1, 3, 1, 1]
# [1, 1, 2]
# [2, 1]
# [1, 1]
# [2]
# -----------------------------------------------------------


# def count_positives_sum_negatives(arr):
#     count = 0
#     summ = 0
#     for i in arr:
#         if i > 0:
#             count += 1
#         else:
#             summ += i
#     return [] if count == 0 and summ == 0 else [count, summ]

# print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))


# def mygcd(x, y):
#     if y == 0:
#         return x
#     else:
#         return mygcd(y, x % y)
#     # 36, 24
#     # 24, 12
#     # 12, 0
# print(mygcd(24, 36))



def reorder(a, b):
    list1 = [i for i in range(0, a // 2)]
    list2 = [i for i in range(a // 2, a)]
    for i in range(b):
        item1 = list1[-1]
        item2 = list2[-1]
        list1.pop()
        list2.pop()
        list1.insert(0, item1)
        list2.insert(0, item2)
    return [list1, list2]

print(reorder(10, 1))