def get_week2_ex5_pattern(end=99):
    pattern = ''

    for i in range(1, 100):
        pattern = pattern + f'{i}-{end}\n'
        end -= 1

    return pattern
