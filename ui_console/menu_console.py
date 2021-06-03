from . import animations_console
import menu_functions
import config

def start_board():
    start_board_text = "CHOIСER - WHEN ALREADY TIRED TO CHOOSE YOURSELF!!!" \
                       "Choiсer makes a random selection from your choices. " \
                       "Now you don't have to spend hours to choose what you want to do!"
    print('-' * 30)
    print(start_board_text)
    print('-' * 30)

def main_menu():
    start_board()
    menu_options = "1) Make choice \n" \
                   "2) Show all choices \n" \
                   "3) Add choice \n" \
                   "4) Edit choice \n" \
                   "5) Delete choice \n" \
                   "6) End program"
    while True:
        print(menu_options)
        option = int(input("Choose option (number): "))
        print('-' * 30)
        if option == 1:
            make_choice()
        if option == 2:
            show_all_choices()
        if option == 3:
            add_choice()
        if option == 4:
            edit_choice()
        if option == 5:
            delete_choiсe()
        if option == 6:
            end_program()
        print('-' * 30)

def make_choice():
    choices_list = menu_functions.get_all_choices()
    if len(choices_list) == 0:
        print("You can`t choose from nothing! Add some choices!")
        return
    choice = menu_functions.make_choice(choices_list)
    try:
        animations_console.anim_start(config.anim_name, menu_functions.get_all_choices(), choice)
    except Exception as err:
        print("Something wrong with animation. Error:")
        print('*'*30)
        print(err)
        print('*'*30)
        print("Your random choice: {0}".format(choice))

def show_all_choices():
    choices = menu_functions.get_all_choices()
    choice_num = 1
    for choice in choices:
        item_text = "{0}) {1}".format(choice_num, choice)
        print(item_text)
        choice_num += 1

def add_choice():
    new_choice = input("Write new choice: ")
    menu_functions.add_choice(new_choice)

def edit_choice():
    choice_num = input("What choice to change (number): ")
    new_choice = input("Write new choice: ")
    if menu_functions.edit_choice(int(choice_num)-1, new_choice):
        print("Edit success!")
    else:
        print("Can`t change this line. Maybe you wrote incorrect number?")

def delete_choiсe():
    choice_num = input("What choice to delete (number): ")
    if menu_functions.delete_choiсe(int(choice_num)-1):
        print("Delete success!")
    else:
        print("Can`t delete this line. Maybe you wrote incorrect number?")

def end_program():
    print("Program ending...")
    menu_functions.end_program()