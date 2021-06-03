def anim(all_lines,chosen_line):
    import random
    import time
    from reprint import output
    import colorama
    from colorama import Back, Style

    colorama.init()
    cycles = 50
    upper = random.choice(all_lines)
    middle = random.choice(all_lines)
    lower = random.choice(all_lines)
    print("Choiser going brrrrrrrrrrrrrrrrr!!!!!!!!!!!!")
    print("Roulette STARTING!!!!")
    print('-' * 30)
    with output(output_type='list', initial_len=4) as output_lines:
        for i in range(cycles):
            upper_text = "| {0}".format(upper)
            middle_text = Back.RED + "| {0} \n".format(middle) + Style.RESET_ALL
            lower_text = "| {0}".format(lower)
            output_lines[0] = upper_text
            output_lines[1] = middle_text
            output_lines[2] = lower_text
            output_lines[3] = '-' * 30
            time.sleep(0.05)

            upper = middle
            middle = lower
            if i == cycles - 2:
                lower = chosen_line
            else:
                lower = random.choice(all_lines)
        for i in range(6):
            middle_text = (Back.RED if i%2 == 0 else Back.GREEN) + "| {0} \n".format(middle) + Style.RESET_ALL
            output_lines[1] = middle_text
            time.sleep(0.1)
