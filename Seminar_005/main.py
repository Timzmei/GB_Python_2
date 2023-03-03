'''
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
'''
list = [int(i) for i in (input("Введите элементы первого множества через пробел или запятую: ").split())]
print(list)
print(ChangeMinMax(list))
def ChangeMinMax(list):
    min = min(list)
    max = max(list)

    for i in range (0, len(list)):
        if list[i] == max:
            list[i] = min
    return list
            


# def inputList(size):
#     list_1 = []
#     for i in range(size):
#         list_1.append(int(input(f"{i}: ")))
#     return list_1

# def changeNum(list_1):
#     max1 = max(list_1)
#     min1 = min(list_1)
#     for number in range(len(list_1)):
#         if list_1[number] == max1:
#             list_1[number] = min1
#     return list_1

# score = inputList(10)
# print(score)
# score = changeNum(score)
# print(score)



'''
4. Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в обратном порядке.

***Примечание.*** В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
'''
