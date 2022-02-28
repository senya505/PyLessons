def is_password_secure(password: str) -> bool:
    return any(c.islower() for c in password) and any(c.isupper() for c in password) \
        and any(c.isdigit() for c in password) and len(password) >= 8

if __name__ == '__main__':
    password = input('Введите пароль: ')
    if is_password_secure(password):
        print('Ваш пароль надежный')
    else:
        print('Ваш пароль ненадежный')
