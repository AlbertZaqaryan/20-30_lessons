# mylist = []
# for i in range(100):
    # mylist.append(i)
#     mylist.insert(0, i)
# print(mylist)
# --------------------------------------------------
# user1 = [[5, 17], [20, 30], [45, 62], [78, 93]]
# user2 = [[1, 8], [20, 31], [34, 60], [70, 74], [83, 92], [97, 100]]
# duration = 9
# --------------------------------------------------
# mylist = [4, 7, 10, 5, 2, 2, 10, 5, 7, 4, 6, 3, 3, 9, 9, 8, 7, 7, 8]
# mylist.sort()
# for i in range(1, len(mylist) - 1):
#     if mylist[i] == mylist[i - 1] or mylist[i] == mylist[i + 1]:
#         continue
#     else:
#         print(mylist[i])
# --------------------------------------------------
# nums = [1,3,5,6]
# target = 2
# if target in nums:
#     print(nums.index(target))
# else:
#     nums.append(target)
#     nums.sort()
#     print(nums.index(target))


# s = "A man, a plan, a canal: Panama"
# s = ''.join([i for i in s if i.isalnum()]).lower()
# print(s == s[::-1])