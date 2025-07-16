# --------------------------------------------------------------
# def is_triangle(a, b, c):
#     pass

# print(is_triangle(-1, 4, 5)) # Chi kareli bacasakan tver tal
# print(is_triangle('a', 3, 5)) # Chi kareli tarer grel
# print(is_triangle(30, 2, 1)) # Chka edpisi erankyun
# print(is_triangle(6, 7, 4)) # Stacvec
# --------------------------------------------------------------
# def func(a, b):
#     return func()
# --------------------------------------------------------------
# factorial = 1
# n = 5
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial)
# --------------------------------------------------------------
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#     # 5 * fact(4)
#     # 5 * 4 * fact(3)
#     # 5 * 4 * 3 * fact(2)
#     # 5 * 4 * 3 * 2 * fact(1)
#     # 5 * 4 * 3 * 2 * 1 = 120
# print(fact(5))

# ------------------------------------------------------
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)
#     # fib(4) + fib(5) 
#     # fib(2) + fib(3) + fib(5) 
#     # fib(0) + fib(1) + fib(3) + fib(5) 
#     # 0 + 1 + fib(3) + fib(5) 
#     # 0 + 1 + fib(1) + fib(2) + fib(5) 
#     # 0 + 1 + 1 + fib(2) + fib(5) 
#     # 0 + 1 + 1 + fib(0) + fib(1) + fib(5) 
#     # 0 + 1 + 1 + 0 + 1 + fib(5) 
#     # 0 + 1 + 1 + 0 + 1 + fib(3) + fib(4) 
#     # 0 + 1 + 1 + 0 + 1 + fib(1) + fib(2) + fib(4) 
#     # 0 + 1 + 1 + 0 + 1 + 1 + fib(2) + fib(4) 
#     # 0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(4) 
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(4) 
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(2) + fib(3) 
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3) 
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(3) 
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2) 
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(2) 
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1) 
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 = 8 
# print(fib(6))
# ------------------------------------------------------

# def get_even(mylist):
#     if mylist == []:
#         return []
#     elif mylist[0] % 2 != 0:
#         return get_even(mylist[1:])
#     else:
#         return [mylist[0]] + get_even(mylist[1:])
    
# print(get_even([7, 4, 1, 20, 6, 9, 11, 30, 17, 15]))

# ----------------------------------------------------------
# def dec_to_bin(number):
#     if number == 1:
#         return '1'
#     else:
#         return dec_to_bin(number // 2) + str(number % 2)

# print(dec_to_bin(22))
# print(dec_to_bin(15))
# print(dec_to_bin(13))
# print(dec_to_bin(18))
# ----------------------------------------------------------
# def bin_to_dec(binary_code, index=0):
#     if binary_code == '':
#         return 0
#     else:
#         return 2 ** index * int(binary_code[-1]) + bin_to_dec(binary_code[:-1], index + 1)
    

# print(bin_to_dec('10010')) # 18
# print(bin_to_dec('10110')) # 22
# print(bin_to_dec('1111')) # 15
# print(bin_to_dec('1010')) # 10
# ----------------------------------------------------------
# def encoding(mylist):
#     if mylist == []:
#         return []
#     else:
#         return [mylist[0]] * mylist[1] + encoding(mylist[2:])

# print(encoding(["A", 12, "B", 4, "A", 6, "B", 1]))
# ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
# ----------------------------------------------------------
# def decoding(mylist, count=1):
#     pass
# print(decoding(["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]))

# ["A", 12, "B", 4, "A", 6, "B", 1]
# ----------------------------------------------------------
# phonetic_dict = {
#     'A': 'Alpha',    'B': 'Bravo',    'C': 'Charlie',
#     'D': 'Delta',    'E': 'Echo',     'F': 'Foxtrot',
#     'G': 'Golf',     'H': 'Hotel',    'I': 'India',
#     'J': 'Juliet',   'K': 'Kilo',     'L': 'Lima',
#     'M': 'Mike',     'N': 'November', 'O': 'Oscar',
#     'P': 'Papa',     'Q': 'Quebec',   'R': 'Romeo',
#     'S': 'Sierra',   'T': 'Tango',    'U': 'Uniform',
#     'V': 'Victor',   'W': 'Whiskey',  'X': 'Xray',
#     'Y': 'Yankee',   'Z': 'Zulu'
# }

# def code(text):
#     if text == '':
#         return ''
#     else:
#         return phonetic_dict[text[0]] + " " + code(text[1:])

# print(code('GOHAR'))
# ----------------------------------------------------------
# def decode(mylist):
#     pass

# print(decode([1, 1, 1, 2, 2, 3, 3, 1, 1, 5, 6, 1, 4, 4, 4, 2, 1]))

# [1, 1, 1, 2, 2, 3, 3, 1, 1, 5, 6, 1, 4, 4, 4, 2, 1]
# [3, 2, 2, 2, 1, 1, 1, 3, 1, 1]
# [1, 3, 3, 1, 2]
# [1, 2, 1, 1]
# [1, 1, 2]
# [2, 1]
# [1, 1]                    
# [2]
# ----------------------------------------------------------
