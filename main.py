# Открываем файл 'text.txt' в режиме чтения с кодировкой UTF-8
with open('text.txt', 'r', encoding='utf-8') as input_file:
    # Читаем все строки из файла и сохраняем их в список 'lines'
    lines = input_file.readlines()

# Открываем файл 'output.txt' в режиме записи с кодировкой UTF-8
with open('output.txt', 'w', encoding='utf-8') as output_file:
    # Проходим по каждой строке в списке 'lines'
    for line in lines:
        # Если длина строки (без пробелов в начале и конце) больше 5 символов, записываем её в 'output.txt'
        if len(line.strip()) > 5:
            output_file.write(line)
