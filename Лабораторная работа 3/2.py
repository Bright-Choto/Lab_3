def find_common_participants(group1, group2, separator=','):
    # Разделить обе строки по указанному разделителю и преобразовать их в наборы
    set1 = set(group1.split(separator))
    set2 = set(group2.split(separator))

    # # Найти общие элементы и вернуть их, отсортированные в алфавитном порядке
    common_participants = sorted(set1 & set2)
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Протестируйте функцию с помощью пользовательского разделителя
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common_participants)
