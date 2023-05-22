# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print('Введите трехзначное число')
number = int(input())
numberPrint = number
sum = 0
if (100 <= number) and (number <= 999):
    while number > 0:
        digit = number % 10
        number = number // 10
        sum += digit
    print(f'Сумма цифр числа {numberPrint}: {sum}') 
else:
    print('Ввели не трехзначное число!!!')