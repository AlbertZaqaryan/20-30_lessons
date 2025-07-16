# import math

# class Circle:

#     def __init__(self, x=0, y=0, r=1):
#         self.x = x
#         self.y = y
#         self.r = r

#     def S(self):
#         return math.pi * self.r ** 2

#     def L(self):
#         return 2 * math.pi * self.r

#     def maxK(self, k):
#         self.r *= k

#     def intersection(self, other_circle):
#         l = ((self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2) ** 0.5
#         if l <= self.r + other_circle.r:
#             return True
#         else:
#             return False
        
# c1 = Circle()
# c2 = Circle(2, 2, 4)
# print(c2.S())
# c2.maxK(3)
# print(c2.S())
# -----------------------------------------------------
# import random
# import time

# class Spartanec:

#     def __init__(self):
#         self.points = 100

#     def minus_points(self):
#         self.points -= 20

# S1 = Spartanec()
# S2 = Spartanec()
# while True:
#     if S1.points == 0:
#         print('Win S2')
#         break
#     elif S2.points == 0:
#         print('Win S1')
#         break
#     else:
#         time.sleep(1)
#         random.choice([S1, S2]).minus_points()
#         print(f'S1 -> {S1.points} | S2 -> {S2.points}')
# -----------------------------------------------------
# class Student:

#     def __init__(self, name:str, group:int, subjects:list[int]):
#         self.name = name
#         self.group = group
#         self.subject = subjects

#     def mean_score(self):
#         return sum(self.subject) / len(self.subject)

# students = [
#     Student('Gohar', 1, [1, 1, 1, 1, 5]),
#     Student('Knarik', 2, [2, 2, 3, 3, 4]),
#     Student('Armen', 1, [5, 5, 4, 4, 4]),
#     Student('Albert', 3, [5, 5, 5, 5, 5]),
#     Student('Arnold', 2, [2, 2, 2, 1, 5]),
# ]
# list_ = [i.mean_score() for i in students]
# list_.sort(reverse=True)
# print(list_)
# users = {i.name:i.mean_score() for i in students}
# print(sorted(users, key=users.get, reverse=True))
# -----------------------------------------------------
# class Parent:

#     def __init__(self, name, age, child_list):
#         self.name = name
#         self.age = age
#         self.child_list = child_list

#     def info(self):
#         return f'My name is {self.name} I am {self.age} yeals old and I have {self.child_list} children list'

#     def sleep(self):
#         return "Sleep child"

#     def eat(self):
#         return "Eat child"

# class Child:

#     def __init__(self, name, age, sleep_lvl, hungy_lvl):
#         self.name = name
#         self.age = age
#         self.sleep_lvl = sleep_lvl
#         self.hungry_lvl = hungy_lvl
# -----------------------------------------------------
# class Human:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __add__(self, other_human):
#         return self.age + other_human.age

#     def __sub__(self, other_human):
#         return self.age - other_human.age

#     def __gt__(self, other_human):
#         if self.age > other_human.age:
#             return self.name
#         else:
#             return  other_human.name

# human1 = Human('Gohar', 30)
# human2 = Human('Knarik', 22)
# age1 = human1.age
# age2 = human2.age
# print(age1 + age2)
# print(human1 + human2)
# print(human2 - human1)
# -----------------------------------------------------
# class Human:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#     def __str__(self):
#         return f'My name is {self.name} I am {self.age} yeals old'


# human1 = Human('Vahan', 30)
# human2 = Human('Vahan', 10)
# print(human1)
# -----------------------------------------------------
import random

class Card:
    def __init__(self, mast, rang):
        self.mast = mast
        self.rang = rang

class Deck:
    def __init__(self, cards = []):
        self.cards = cards

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
    def add(self, card):
        self.cards.append(card)

list1 = [2,3,4,5,6,7,8,9,10,10,10,11]
list2 = ['♥', '♦', '♣', '♠']

kalod = Deck().cards

for i in list1:
    for j in list2:
        kalod.append(Card(j, i))

player1 = Player('Knarik', [])
player2 = Player('Armen', [])

def bajanelCards(player):
    card1 = random.choice(kalod)
    kalod.remove(card1)

    if card1.rang == 11:
        if blackJack(player) > 10:
            card1.rang = 1
    player.add(card1)

bajanelCards(player1)
bajanelCards(player1)
bajanelCards(player2)
bajanelCards(player2)



def blackJack(player):
    return sum([i.rang for i in player.cards])
   

def game(player):
    print([f'{i.mast}{i.rang}' for i in player.cards])
    while True:
        if blackJack(player) > 21:
            print(f'{player.name} You lost!')
            exit()
        else:
            text = input(f'{player.name} If you want continue press enter, if quit press Q')
            if text == '':
                bajanelCards(player)
                print([f'{i.mast}{i.rang}' for i in player.cards])
            else:
                break

        print(blackJack(player))

game(player1)
game(player2)

if(blackJack(player1) > blackJack(player2)):
    print(f'{player1.name} Win!!!!!')
elif(blackJack(player2) > blackJack(player1)):
    print(f'{player2.name} Win!!!!!')
else:
    print('nichya')