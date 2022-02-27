from curses.ascii import isdigit, islower, isupper


def is_password_secure(password: str) -> bool:
    return any(islower(c) for c in password) and any(isupper(c) for c in password) \
        and any(isdigit(c) for c in password) and len(password) >= 8

if __name__ == '__main__':
    password = input('Введите пароль: ')
    if is_password_secure(password):
        print('Ваш пароль надежный')
    else:
        print('Ваш пароль ненадежный')
