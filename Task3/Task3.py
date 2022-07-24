# Найти сумму чисел списка стоящих на нечетной позиции
import random
def EvenOddSum(a, n):
    even_sum = sum(a[::2])
    odd_sum = sum(a[1::2])
    print("Сумма чисел на чётных позициях = ", even_sum)
    print("Сумма чисел на нечётных позициях нечётных чисел = ", odd_sum)

arr = [random.randrange(1, 50, 1) for i in range(10)]
print ("Строка случайных чисел с заданным количеством =\n " +  str(arr))
n = len(arr)
EvenOddSum(arr, n)