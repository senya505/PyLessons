from task2 import generate_password
from task3 import is_password_secure


password = generate_password()
tries = 1
while not is_password_secure(password):
    password = generate_password()
    tries += 1

print(password)
print(f'Generation took {tries} tries')
