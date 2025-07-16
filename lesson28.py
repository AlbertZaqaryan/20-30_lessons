# class Car:

#     def __init__(self, model, year):
#         self.model = model
#         self.year = year


# class Hecaniv:

#     def __init__(self, aker):
#         self.aker = aker

# class Fiat(Hecaniv, Car):

#     def __init__(self, model, year, size, aker):
#         Hecaniv.__init__(self, aker)
#         Car.__init__(self, model, year)
#         self.size = size
# --------------------------------------------------------------
# from abc import ABC, abstractmethod


# class Transport(ABC):


#     def __init__(self, model, year):
#         self.model = model
#         self.year = year


#     @abstractmethod
#     def delivery(self):
#         pass



# class Moped(Transport):


#     def __init__(self, model, year, company_name):
#         super().__init__(model, year)
#         self.company_name = company_name


#     def delivery(self):
#         return "Moped delivery method"


# class Truck(Transport):


#     def __init__(self, model, year, trailer_size):
#         super().__init__(model, year)
#         self.trailer_size = trailer_size

#     def delivery(self):
#         return "Truck delivery method"

# x = Truck('MAN', 2020, 5)
# print(x.delivery())

# y = Moped('Suzuki', 2018, 'Glovo')
# --------------------------------------------------------------
# inputList = [3, 6, -2, -5, 7, 3]
# max_value = 0
# for i in range(0, len(inputList) - 1):
#     if inputList[i] * inputList[i + 1] > max_value:
#         max_value = inputList[i] * inputList[i + 1]
# print(max_value)

# inputList = [3, 6, -2, -5, 7, 3]
# print(max([inputList[i] * inputList[i + 1] for i in range(0, len(inputList) - 1)]))


# inputList = ["aba", "aa", "ad", "vcd", "aba"]
# inputList.sort(key=len)
# max_len = len(inputList[-1])
# for i in inputList:
#     if len(i) == max_len:
#         print(i)


# n = 2341
# n = str(n)
# print(sum([int(i) for i in n[:len(n) // 2]]) == sum([int(i) for i in n[len(n) // 2:]]))


# a = [-1, -25, 150, 190, 170, -1, -1, 160, 180]
# b = [i for i in a if i != -1]
# b.sort()
# index = 0
# for i in range(0, len(a)):
#     if a[i] == -1:
#         continue
#     else:
#         a[i] = b[index]
#         index += 1
# print(a)


# cube_matrix_sum=lambda i:sum(sum(sum(i,[]),[]))

# x = [
#   [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#   [[10,11,12],[13,14,15],[16,17,18]],
#   [[19,20,21],[22,23,24],[25,26,27]]
# ]
# print(sum(sum(sum(x,[]), [])))
# print(cube_matrix_sum(x))

# print(str(x))
# print(len(x))
# print(x)
# print(sum(sum(sum(i) for i in x) for x in x))
# print(sum(sum(sum(i)) for i in x))

# print(len('def cube_matrix_sum(x):return sum([sum(i) for i in x for i in i])'))
# cube_matrix_sum=lambda x:sum([sum(i) for i in x for i in i])
# print(cube_matrix_sum(x))

# x = lambda a,b:a + b
# print(x(7, 5))


#    16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


# def digital_root(n, summ = 0):
#     if n == 0 and summ < 10:
#         return summ
#     elif summ == 0 and n < 10:
#         return n
#     else:
#         summ += n % 10
#         return n % 10 + digital_root(n // 10)

# n = 132189
# print(digital_root(n))


# n = 942
# summ = 0
# while True:
#     if n == 0 and summ < 10:
#         print(summ)
#         break
#     elif n < 10 and summ == 0:
#         print(n)
#         break
#     else:
#         summ += n % 10
#         n //= 10
#         if n < 10:
#             n += summ
#             summ = 0
        