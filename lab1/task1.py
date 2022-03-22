documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_owner(num: str) -> str:
    for document in documents:
        if document['number'] == num:
            return document['name']
    return None


def get_directory(num: str) -> str:
    for directory, nums in directories.items():
        if num in nums:
            return directory
    return None


def list_documents() -> str:
    return '\n'.join(map(lambda document: f'№: {document["number"]}, тип: {document["type"]}, владелец: {document["name"]}, '
                                          f'полка хранения: {get_directory(document["number"])}', documents))


def add_directory(directory: str) -> str:
    if directory in directories.keys():
        return 'Такая полка уже существует'
    directories[directory] = []
    return 'Полка добавлена'

def del_directory(directory: str) -> str:
    if directory not in directories.keys():
        return 'Такой полки не существует'
    if len(directories[directory]) > 0:
        return 'На полке есть документы, удалите их перед удалением полки'
    del directories[directory]
    return 'Полка удалена'

while True:
    command = input('Введите команду:\n')
    if command == 'q':
        break
    elif command == 'p':
        num = input('Введите номер документа:\n')
        print(get_owner(num))
    elif command == 's':
        num = input('Введите номер документа:\n')
        print(get_directory(num))
    elif command == 'l':
        print(list_documents())
    elif command == 'ads':
        directory = input('Введите номер полки:\n')
        print(add_directory(directory), end='. Текущий перечень полок: ')
        print(', '.join(directories.keys()))
    elif command == 'ds':
        directory = input('Введите номер полки:\n')
        print(del_directory(directory), end='. Текущий перечень полок: ')
        print(', '.join(directories.keys()))
