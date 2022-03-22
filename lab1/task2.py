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

def get_document(num: str) -> dict:
    for document in documents:
        if document['number'] == num:
            return document


def get_owner(num: str) -> str:
    document = get_document(num)
    if document is not None:
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
        return 'Такая полка уже существует.'
    directories[directory] = []
    return 'Полка добавлена.'


def del_directory(directory: str) -> str:
    if directory not in directories.keys():
        return 'Такой полки не существует.'
    if len(directories[directory]) > 0:
        return 'На полке есть документы, удалите их перед удалением полки.'
    del directories[directory]
    return 'Полка удалена.'

def add_document(document: dict, directory: str) -> str:
    if directory not in directories.keys():
        return 'Такой полки не существует. Добавьте полку командой as.'
    documents.append(document)
    directories[directory].append(document['number'])
    return 'Документ добавлен.'

def del_document(num: str) -> str:
    directory = get_directory(num)
    if directory is None:
        return 'Документ не найден в базе.'
    documents.remove(get_document(num))
    directories[directory].remove(num)
    return 'Документ удален'

def move_document(num: str, to_dir: str) -> str:
    if to_dir not in directories.keys():
        return 'Такой полки не существует.'
    from_dir = get_directory(num)
    if from_dir is None:
        return 'Документ не найден в базе.'
    directories[from_dir].remove(num)
    directories[to_dir].append(num)
    return 'Документ перемещен'

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
        print(add_directory(directory), end=' Текущий перечень полок: ')
        print(', '.join(directories.keys()))
    elif command == 'ds':
        directory = input('Введите номер полки:\n')
        print(del_directory(directory), end=' Текущий перечень полок: ')
        print(', '.join(directories.keys()))
    elif command == 'ad':
        num = input('Введите номер документа:\n')
        doc_type = input('Введите тип документа:\n')
        owner = input('Введите владельца документа:\n')
        directory = input('Введите полку для хранения:\n')
        print(add_document({'number': num, 'type': doc_type, 'name': owner}, directory))
        print('Текущий список документов:')
        print(list_documents())
    elif command == 'd':
        num = input('Введите номер документа:\n')
        print(del_document(num))
        print('Текущий список документов:')
        print(list_documents())
    elif command == 'm':
        num = input('Введите номер документа:\n')
        to_dir = input('Введите номер полки:\n')
        print(move_document(num, to_dir))
        print('Текущий список документов:')
        print(list_documents())
