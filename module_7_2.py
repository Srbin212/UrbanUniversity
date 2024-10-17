
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    res  ={}
    file = open(file_name, 'w', encoding='utf-8')
    cur_str_num = 1
    for i in strings:
        cur_tell = file.tell()
        file.write(f'{i}\n')
        res.update({(cur_str_num,cur_tell) : i})
        cur_str_num += 1
    file.close()
    return res

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)