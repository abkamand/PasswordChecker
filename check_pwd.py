def check_pwd(pw):
    pw_length = len(pw)

    if (pw_length > 20 or pw_length < 8):
        return False

    return True
