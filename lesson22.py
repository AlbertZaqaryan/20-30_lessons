# def QuickSort(mylist):
#     if len(mylist) <= 1:
#         return mylist
#     else:
#         item = mylist[0] # 7
#         list1 = [i for i in mylist if i < item]
#         list2 = [i for i in mylist if i == item]
#         list3 = [i for i in mylist if i > item]
#         return QuickSort(list1) + list2 + QuickSort(list3)
# # Q([4, 5, 1, 6, 3]) + [7] + Q([10, 9, 12])
# # Q([1, 3]) + [4] + Q([5, 6]) + [7] + Q([10, 9, 12])
# # [] + [1] + [3] + [4] + Q([5, 6]) + [7] + Q([10, 9, 12])
# # [] + [1] + [3] + [4] + [] + [5] + [6] + [7] + Q([10, 9, 12])
# # [] + [1] + [3] + [4] + [] + [5] + [6] + [7] + [9] + [10] + [12]

# mylist = [7, 10, 4, 5, 1, 9, 6, 12, 3]
# print(QuickSort(mylist))
# -----------------------------------------------------------
# class Vedro:

#     def avelacnel():
#         pass

# x = Vedro()
# x.avelacnel(4)
# -----------------------------------------------------------
# class Mard:

#     def __init__(self, anun, tariq):
#         self.x = anun # attr
#         self.y = tariq # attr
#         self.z = 'Audi'

#     def im_masin(self): # method
#         return f'Barev es {self.x}n em ev {self.y} tarekan em'
    
#     def vazel(self):
#         return f'{self.x}y vazum e'

# mard1 = Mard('Arnold', 20) # exp | obj | instance
# mard2 = Mard('Knarik', 22) # exp | obj | instance
# mard3 = Mard('Gohar', 25) # exp | obj | instance
# print(mard1.im_masin())
# print(mard2.im_masin())
# print(mard3.im_masin())

# print(mard1.vazel())
# print(mard2.vazel())
# print(mard3.vazel())
# -----------------------------------------------------------
# class Car:

#     def __init__(self, model, year, color, hp):
#         self.model_ = model
#         self.year_ = year
#         self.color_ = color
#         self.hp_ = hp

#     def info(self):
#         return f'Car mode -> {self.model_}\nCar year -> {self.year_}\nCar color -> {self.color_}\nCar hp -> {self.hp_}'
    
#     def stage(self, new_hp):
#         self.hp_ += new_hp

#     def change_color(self, new_color):
#         self.color_ = new_color

# car1 = Car('Honda Civic', 2002, 'Black', 192)
# car2 = Car('Fiat 500C', 2020, 'White', 120)
# car3 = Car('Aston Martin', 2021, 'Green', 300)
# print(car1.info())
# car1.stage(70)
# print(car1.info())

# print(car2.info())
# car2.change_color('Red')
# print(car2.info())
# print(type(car1))
# print('------------------------------------')
# print(car2.info())
# print('------------------------------------')
# print(car3.info())
# print('------------------------------------')
# -----------------------------------------------------------

# class BankAccount:

#     def __init__(self, account_number:str, balance:int=0):
#         self.account_number = account_number
#         self.balance = balance
#         self.transactions = []

#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f'Deposit: +${amount}')

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             self.transactions.append(f'Withdraw: -${amount}')
#         else:
#             raise Exception('No 💸 error')
    
#     def transfer(self, other_account, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             other_account.balance += amount
#             self.transactions.append(f'Transfer to {other_account.account_number}: -${amount}')
#             other_account.transactions.append(f'Transfer from {self.account_number}: +${amount}')
#         else:
#             raise Exception('No 💸 error')

#     def generate_statement(self):
#         return self.transactions
    
#     def get_balance(self):
#         return self.balance
    
#     def clear_transactions(self):
#         self.transactions.clear()

# Knarik = BankAccount('3012 7455 9685 1002', 25000)
# Gohar = BankAccount('1145 7745 9851 2236', 24000)
# Knarik.deposit(1500)    
# Knarik.deposit(1500)    
# Knarik.withdraw(7000)
# Gohar.deposit(3400)
# Gohar.transfer(Knarik, 7000)
# print('------------ Gohar ---------------')
# print(Gohar.generate_statement())
# print(Gohar.get_balance())    

# print('------------ Knarik ---------------')
# print(Knarik.generate_statement())
# print(Knarik.get_balance())    
# -----------------------------------------------------------

    

