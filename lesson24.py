# class Mard:

#     def __init__(self, anun, tariq):
#         self.__anun = anun
#         self.__tariq = tariq # private attr


#     def get_tariq(self): # public method
#         return self.__tariq # private attr

#     def set_tariq(self, nor_tariq):
#         if nor_tariq <= 0:
#             raise Exception('Tariqy chi kara poqr kam havasar lini 0 ic!!!!')
#         self.__tariq = nor_tariq

#     def del_tariq(self):
#         del self.__tariq


#     def im_masin(self):
#         return f'Barev es {self.__anun}n em es {self.__tariq} tarekan em'


# mard1 = Mard('Arnold', 20)
# mard2 = Mard('Ani', 25)
# print(mard1._Mard__tariq)
# print(mard1.__dict__)
# mard1.set_tariq(-40)
# mard1.del_tariq()
# print(mard1.get_tariq())
# print(mard1.im_masin())
# print(mard2.im_masin())

# -------------------------------------------------------------
# import time

# def timer_decorator(func):
#     def wraps_func(*args, **kwargs):
#         '''wraps doc'''
#         st = time.time()
#         func(*args, **kwargs)
#         et = time.time()
#         return et - st
#     return wraps_func


# @timer_decorator
# def number_s():
#     '''number_s doc'''
#     return [i ** 2 for i in range(1000000)]

# @timer_decorator
# def number_c():
#     return [i ** 3 for i in range(1000000)]

# @timer_decorator
# def number_n(n):
#     return [i ** n for i in range(1000000)]


# print(number_s())
# print(number_c())
# print(number_n(7))
# -------------------------------------------------------------
# import time


# class TimerDecorator:

#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         st = time.time()
#         self.func(*args, **kwargs)
#         et = time.time()
#         return et - st


# @TimerDecorator
# def number_s():
#     '''number_s doc'''
#     return [i ** 2 for i in range(1000000)]

# @TimerDecorator
# def number_c():
#     return [i ** 3 for i in range(1000000)]

# @TimerDecorator
# def number_n(n):
#     return [i ** n for i in range(1000000)]


# print(number_s())
# print(number_c())
# print(number_n(7))
# -------------------------------------------------------------
# class Mard:

#     def __init__(self, anun, tariq):
#         self.__anun = anun
#         self.__tariq = tariq

#     @property
#     def anun(self):
#         return self.__anun
    
#     @anun.setter
#     def anun(self, nor_anun):
#         self.__anun = nor_anun

#     @property
#     def tariq(self):
#         return self.__tariq
    
#     @tariq.setter
#     def tariq(self, nor_tariq):
#         if nor_tariq <= 0:
#             raise Exception('Tariqy chi kara poqr kam havasar lini 0 ic!!!!')
#         self.__tariq = nor_tariq
    
# mard1 = Mard('Knarik', 22)
# mard1.tariq = 30
# print(mard1.tariq)
# -------------------------------------------------------------
# import datetime

# def logger(func):
#     def wraps_func(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as ex:
#             with open('error.log', 'a') as file:
#                 file.write(f'{func.__name__} --> {ex.__class__.__name__} --> {datetime.datetime.now()}\n')
#             return 'Function error please open error.log file'
#     return wraps_func


# @logger
# def func1():
#     return "Hello"

# @logger
# def func2(a, b):
#     return a + b

# @logger
# def func3(a):
#     return a ** 2

# @logger
# def func4(text):
#     return text + 4


# print(func1())
# print(func2(4, 'a'))
# print(func3(7))
# print(func4('python'))
# -------------------------------------------------------------
# class BankAccount:
#     def __init__(self, balance, account_number):
#         self.__balance = balance
#         self.__account_number = account_number
#         self.transactions = []

#     def deposit(self, amount):
#         self.__balance += amount
#         self.transactions.append(f'Deposit: ${amount}')

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             self.transactions.append(f'Withdraw: ${amount}')
#         else:
#             raise 'Not enough funds'
#     def transfer(self, other_account, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             other_account.__balance += amount
#             self.transactions.append(f'${self.__account_number}: -${amount} ->> %{other_account.__account_number} +${amount}')
#             other_account.transactions.append(f'${self.__account_number}: -${amount} ->> %{other_account.__account_number} +${amount}')
#         else:
#             raise 'Not enough funds'
        
#     def generate_statement(self):
#         return self.transactions
    
#     def get_balance(self):
#         return self.__balance
    
#     def clear_transactions(self):
#         self.transactions = []

# account1 = BankAccount(50000, '323432 4343 233434')
# print(account1.get_balance())
# account2 = BankAccount(100, '3434 3435 2323 5454')
# account1.transfer(account2, 100)
# print(account2.get_balance())
# print(account1.generate_statement())
# print(account2.generate_statement())
# print(account2.get_balance())
# -------------------------------------------------------------
# class TriangleChecker:

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def is_triangle(self):
#         try:
#             if self.a <= 0 or self.b <= 0 or self.c <= 0:
#                 return 'С отрицательными числами ничего не выйдет!'
#             else:
#                 if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
#                     return 'Ура, можно построить треугольник!'
#                 else:
#                     return 'Жаль, но из этого треугольник не сделать!'
#         except:
#             return 'Нужно вводить только числа!'
    
# triangle = TriangleChecker(14, 10, 8)
# print(triangle.is_triangle())
# -------------------------------------------------------------
# class Soda:

#     def __init__(self, app=None):
#         self.app = app

#     def show_my_drink(self):
#         if self.app:
#             return f'{self.app} gazirovka'
#         else:
#             return 'Sovorakan Gazirovka'

# soda1 = Soda()
# soda2 = Soda('Laym')
# print(soda1.show_my_drink())
# print(soda2.show_my_drink())
# -------------------------------------------------------------



