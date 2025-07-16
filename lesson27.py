# class Mard:

#     def __init__(self, age):
#         self.__age = age

#     def poxel_tariqy(self, x):
#         if x > 0:
#             self.__age = x


# mard1 = Mard(20)
# mard2 = Mard(30)
# mard1.poxel_tariqy(40)
# print(mard1.__age)



# ------------------------------------------------

# class Transport:


#     def __init__(self, t_type, model, year):
#         self.t_type = t_type
#         self.model = model
#         self.year = year

#     def delivery(self):
#         return f'Transport class: Delivery method'
    

# class Truck(Transport):

#     def __init__(self, t_type, model, year, trailer_size):
#         super().__init__(t_type, model, year)
#         self.trailer_size = trailer_size

#     def delivery(self):
#         return f'Truck class: Delivery method'


# class Moped(Transport):

#     def __init__(self, t_type, model, year, driver_Indi):
#         super().__init__(t_type, model, year)
#         self.driver_Indi = driver_Indi

#     def delivery(self):
#         if self.driver_Indi == True:
#             return f'Moped class: Indi driver Delivery method'
#         else:
#             return f'Moped class: Armenian driver Delivery method'




# x = Truck('Car', 'Volvo', 2020, 5)
# print(x.delivery())  
# ------------------------------------------------
# class Mard:

#     def __init__(self, anun, tariq):
#         self.anun = anun
#         self.tariq = tariq

#     def xosel(self):
#         return 'Xosel'

#     def utel(self):
#         pass


# class Biznesmen(Mard):

#     def __init__(self, anun, tariq, avtopark):
#         Mard.__init__(self, anun, tariq)
#         self.avtopark = avtopark

#     def sharjer(self):
#         pass

# class Cragravorox(Mard):

#     def __init__(self, anun, tariq, komp, makardak, kampanya):
#         Mard.__init__(self, anun, tariq)
#         self.komp = komp
#         self.makardak = makardak
#         self.kampanya = kampanya

#     def kod_grel(self):
#         pass

# class Hogeban(Mard):

#     def __init__(self, anun, tariq, pacientneri_qanak):
#         Mard.__init__(self, anun, tariq)
#         self.pacientneri_qanak = pacientneri_qanak

#     # def xosel(self):
#     #     return "Urish dzev"


# class WebCragravorox(Cragravorox):

#     def __init__(self, anun, tariq, komp, makardak, kampanya, DB, API):
#         Cragravorox.__init__(self, anun, tariq, komp, makardak, kampanya)
#         self.DB = DB
#         self.API = API

#     def migrations(self):
#         pass


# class Gohar(WebCragravorox, Hogeban):

#     def __init__(self, anun, tariq, komp, makardak, kampanya, DB, API, pacientneri_qanak):
#         WebCragravorox.__init__(self, anun, tariq, komp, makardak, kampanya, DB, API)
#         Hogeban.__init__(self, anun, tariq, pacientneri_qanak)



# mard = Gohar('Gohar', 25, 'Lenovo', 'Senior', 'Soft', 'MySQL', 'soft-api', 5)
# print(mard.xosel())
# ----------------------------------------------------------------


# class Home:

#     count = 10


# x = Home()
# y = Home()
# Home.count -= 10
# print(x.count)
# print(y.count)

# ----------------------------------------------------------------
# import time
# import random
# import os


# class Tun:

#     gumar_paharanum = 100
#     sarnaranum_uteliq = 50
#     katvi_ker = 30
#     poshi = 0


# class Mard:

#     def __init__(self, anun):
#         self.anun = anun
#         self.kusht = 30
#         self.urax = 100

#     def utel(self, count):
#         if Tun.sarnaranum_uteliq >= count:
#             self.kusht += count
#         else:
#             print('Gna uteliq ar')

#     def sirel_katvin(self):
#         self.kusht -= 10
#         self.urax += 5
    
# class Kendani:

#     def __init__(self, anun):
#         self.anun = anun
#         self.kusht = 30

#     def utel(self, count):
#         if Tun.katvi_ker >= count:
#             self.kusht += 2 * count
#         else:
#             print('Uteliq chka katvi hamar')

#     def qnel(self):
#         self.kusht -= 10

# class Amusin(Mard):
    
#     def __init__(self, anun):
#         super().__init__(anun)

#     def ashxatel(self):
#         Tun.gumar_paharanum += 150
#         self.kusht -= 10

#     def xaxal_komp(self):
#         self.kusht -= 10
#         self.urax += 20


# class Kin(Mard):
    
#     def __init__(self, anun):
#         super().__init__(anun)

#     def gnel_uteliq(self, count):
#         if Tun.gumar_paharanum >= count:
#             Tun.sarnaranum_uteliq += count
#             Tun.gumar_paharanum -= count
#             self.kusht -= 10
#         else:
#             print('Amusin gna gorci sax ory xaxum es')

#     def gnel_katvi_ker(self, count):
#         if Tun.gumar_paharanum >= count:
#             Tun.katvi_ker += count
#             Tun.gumar_paharanum -= count
#             self.kusht -= 10
#         else:
#             print('Amusin gna gorci sax ory xaxum es')

#     def gnel_shub(self):
#         if Tun.gumar_paharanum >= 350:
#             Tun.gumar_paharanum -= 350
#             self.urax += 60
#         else:
#             print('Sax shub en hagnum es chunem 😭')

#     def havaqel_tnery(self):
#         Tun.poshi = 0
#         self.kusht -= 10


# class Katu(Kendani):
    
#     def __init__(self, anun):
#         super().__init__(anun)


#     def aboyner_pokel(self):
#         Tun.poshi += 5



# a = Amusin("Hakob")
# b = Kin("Armine")
# c = Katu("Murzik")
# amusin_metodner = ['ashxatel', 'sirel katvin', 'xaxal', 'utel']
# kin_metodner = ['gnel uteliq', 'gnel uteliq katvi hamar', 'gnel shub', 'utel', 'tnery havaqel']
# katu_metodner = ['utel', 'qnel', 'pokel aboynery']
# while True:
#     print(f'🏠 --- > 💵 {Tun.gumar_paharanum}, 🍊🍉🍌 {Tun.sarnaranum_uteliq}, 🐁 {Tun.katvi_ker}, 🗑️ {Tun.poshi}')
#     time.sleep(1)
#     a_method = random.choice(amusin_metodner)
#     b_method = random.choice(kin_metodner)
#     c_method = random.choice(katu_metodner)
#     if a.kusht <= 0 or a.urax <= 0:
#         print('🪦 🪦 🪦  🤵  🪦 🪦 🪦')
#         break
#     if b.kusht <= 0 or b.urax <= 0:
#         print('🪦 🪦 🪦  👰  🪦 🪦 🪦')
#         break
#     if c.kusht <= 0:
#         print('🪦 🪦 🪦  🐈  🪦 🪦 🪦')
#         break
#     if Tun.poshi >= 90:
#         a.urax -= 10
#         b.urax -= 10
#     if a_method == 'ashxatel':
#         a.ashxatel()
#     elif a_method == 'sirel katvin':
#         a.sirel_katvin()
#     elif a_method == 'xaxal':
#         a.xaxal_komp()
#     elif a_method == 'utel':
#         a.utel(random.randint(1, 30))
#     if b_method == 'gnel uteliq':
#         b.gnel_uteliq(random.randint(1, 30))
#     elif b_method == 'gnel uteliq katvi hamar':
#         b.gnel_katvi_ker(random.randint(1, 10))
#     elif b_method == 'gnel shub':
#         b.gnel_shub()
#     elif b_method == 'utel':
#         b.utel(random.randint(1, 30))
#     elif b_method == 'tnery havaqel':
#         b.havaqel_tnery()
#     if c_method == 'utel':
#         c.utel(random.randint(1, 10))
#     elif c_method == 'qnel':
#         c.qnel()
#     elif c_method == 'pokel aboynery':
#         c.aboyner_pokel()
#     os.system('cls')
    
#     print(f'🤵 {a.anun}\nKusht {a.kusht}, Urax {a.urax}')
#     print('-----------------------------------------------------')
#     print(f'👰 {b.anun}\nKusht {b.kusht}, Urax {b.urax}')
#     print('-----------------------------------------------------')
#     print(f'🐈 {c.anun}\nKusht {c.kusht}')
#     print('-----------------------------------------------------')
# ----------------------------------------------------------------
# def queryString(s, n):

#     for num in range(n//2+1, n+1):
#         if bin(num)[2:] not in s: 
#             return False   
#     return True

     # bn_num = 0
    # if len(s) < len(bin(n))-2:
    #     return False
    # else:
    #     for i in range(1,n+1):
    #         bn_num = (bin(i))[2:]
    #         if bn_num not in s:
    #             return False
    #     else:
    #         return True


# s_ = "01101010101011110101010101111111111111111111111111111111111\
#     000000000000001111110101010100101010101010101010101010111101010\
#         10101111111111111111111111111111111111000000000000001111110101\
#             01010010101010101010101010100"
# n_ = 1000000000
# print(queryString(s = s_, n = n_))



