def check_pwd(pw):
    count_lower = 0

    pw_length = len(pw)

    if (pw_length > 20 or pw_length < 8):
        return False

    for char in pw:
        if char.islower():
            count_lower += 1
    if count_lower == 0:
        return False

    return True
