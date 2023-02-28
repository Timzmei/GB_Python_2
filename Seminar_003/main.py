# spisok = [1, 1, 2, 0, -1, 3, 4, 4, 5, 5, 7]
# list = []
# for i in range(0, len(spisok)):
#     if spisok[i] not in list:
#         list.append(spisok[i])
# print(len(list))

# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

'''
spisok = [1, 2, 3, 4, 5, 6, 7]
k = int(input('Введите число сдвига: '))
temp = None
for i in range(0, k):
    for j in range(len(spisok)-1, 0, -1):
        temp = spisok[j]
        spisok[j] = spisok[j-1]
        spisok[j-1]= temp
print(spisok)
'''

list_1 = [1, 2, 3, 4, 5, 6, 7]
k = int(input())
result = []
temp1 = list_1[:-k]
temp2 = list_1[-k:]
result = temp2 + temp1
print (result)


"""
Задача №21. 
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
"""

list_of_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 

list = []
j = 0
for i in list_of_dict:
    for j in i.values():       
        if j not in list:
            list.append(j)
    
print(list)

spisok = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"},
          {" VIII ": "S007"}]
result = list()
for dict in spisok:
    for k in dict:
        result.append(dict[k])
print(set(result))


'''
Дан массив, состоящий из целых чисел. 
Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
'''

list = [1, 4, 3, 4, 5]
count = 0
for i in range(0, len(list)-1):
    if list[i+1]>list[i]:
        count+=1

print(count)