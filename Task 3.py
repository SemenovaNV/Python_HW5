# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def coding(text):
    result = ''
    count = 0
    old_element = ''
    for i in text:
        if old_element == '':
            old_element = i
            count += 1
            # print(count)
            continue
        if i == old_element:
            count += 1
            # print(count)
        else:
            result = result + str(count) + old_element
            old_element = i
            count = 1
            # print(count)
            # print(result)  
    result = result + str(count) + old_element
    return result

def decoding(text):
    count = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():   #проверка на буквы
            count += text[i]
        else:
            result = result + text[i] * int(count)
            count = ''
    return result

with open('text_start.txt', 'r') as file:
    file_data_list1 = file.read()
    print(f'Входные данные {file_data_list1}')
file.close()
text_encode = coding(file_data_list1)
print(f"Текст после сжатия:{text_encode}")
with open('text_finish.txt', 'w') as data:
        data.write(text_encode)

with open('text_finish.txt', 'r') as file:
    file_data_list2 = file.read()
file.close()    
text_decode = decoding(file_data_list2)
print(f"Текст после восстановления:{text_decode}")
with open('text_finish.txt', 'a') as data:
        data.write('\n' + text_decode)
