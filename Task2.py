"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""

def create_argument_dictionary(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        if hashable(value):
            argument_dict[value] = key
        else:
            argument_dict[str(value)] = key
    return argument_dict

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

# Пример использования функции
result = create_argument_dictionary(arg1=10, arg2='hello', arg3=[1, 2, 3])

# Вывод полученного словаря
for key, value in result.items():
    print(f'{key}: {value}')

