# Задача 8: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите размеры шоколадки:')
n = int(input('Введите значение n:')) 
m = int(input('Введите значение m:')) 
k = int(input('Введите количество долек, которое нужно отломить:'))

if n*m <= k:
    print(f'{k} долек, которое нужно отломить, больше либо равно {n*m} долек в шоколадке') 
elif (k % n == 0) or (k % m == 0):
   print(f'У шоколадки размером {n} x {m} МОЖНО отломить {k} долек за один разлом') 
else:
    print(f'У шоколадки размером {n} x {m} НЕЛЬЗЯ отломить {k} долек за один разлом') 

    