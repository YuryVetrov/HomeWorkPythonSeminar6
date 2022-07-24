# Предложить улучшения кода для уже решённых задач с помощью использования 
# **лямбд, filter, map, zip, enumerate, list comprehension
# Дана последовательность чисел. Получить список уникальных элементов 
# заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

nums = list(map(str,input('Введите числа списка через пробел ').split()))
def print2SingleNumbers(nums):
    set1 = set()
    n = len(nums)
    for i in nums:
        if i in set1:
            set1.remove(i)
        else:
            set1.add(i)
    print("Неповторяющиеся элементы списка : " + " ".join(map(str, set1)))
print2SingleNumbers(nums)