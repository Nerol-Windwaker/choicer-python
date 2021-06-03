import config

def get_all_lines():
    file = open(config.choices_file, 'r', encoding='utf-8')
    choices_list = list(filter(lambda a: len(a)>0,file.read().split('\n')))
    file.close()
    return choices_list

def add_line(new_content):
    file = open(config.choices_file, 'a', encoding='utf-8')
    file.write('\n'+new_content)
    file.close()

def edit_line(line_num,new_content):
    file_edit = open(config.choices_file, 'r', encoding='utf-8')
    lines = list(filter(lambda a: a not in '\n ', file_edit.readlines()))
    file_edit.close()
    try:
        lines[line_num] = new_content + '\n'
    except IndexError:
        return False
    file_save = open(config.choices_file, 'w', encoding='utf-8')
    file_save.writelines(lines)
    file_save.close()
    return True

def delete_line(line_num):
    choices_list = get_all_lines()
    try:
        choices_list.pop(line_num)
    except IndexError:
        return False
    file = open(config.choices_file, 'w', encoding='utf-8')
    for choice in choices_list:
        file.write(choice +'\n')
    file.close()
    return True
