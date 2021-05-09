def check_pwd(pw):
    count_lower = 0
    count_upper = 0
    count_digit = 0
    permitted_symbols = "~`!@#$%^&*()_+-="
    has_symbol = False

    pw_length = len(pw)

    if (pw_length > 20 or pw_length < 8):
        return False

    for char in pw:
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        if char.isdigit():
            count_digit += 1
        if char in permitted_symbols:
            has_symbol = True
    if count_lower == 0 or count_upper == 0 or count_digit == 0 or \
            has_symbol is False:
        return False

    return True
