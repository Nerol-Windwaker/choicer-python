import config
import work_with_file
import random_choice

def make_choice(choices_list):
    return random_choice.random_choice(choices_list)

def get_all_choices():
    return work_with_file.get_all_lines()

def add_choice(new_choice):
    work_with_file.add_line(new_choice)

def edit_choice(line_num, new_choice):
    return work_with_file.edit_line(line_num, new_choice)

def delete_choiсe(line_num):
    return work_with_file.delete_line(line_num)

def end_program():
    import sys
    sys.exit(0)