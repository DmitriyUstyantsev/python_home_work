#Задача 2: Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) ''|

var = int(input("введи трехзначное число: "))
print(f"Сумма всех чисел трехзначного числа: {var//100+var//10%10+var%10}")
