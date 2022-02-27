from random import choices, randint


def generate_password():
    return ''.join(map(chr, choices(range(33, 127), k=randint(7,10))))
