# Первая функция
def func(list_1):
    list_1.insert(0, 'Element')
    list_1.insert(1, 'start')
    list_1.append('finish')
    return list_1
print(func(['hello', 5, 'John', ]))


# Вторая функция
def func(*args):
    dict_1 = {}
    count = 0
    for i in args:
        dict_1[i] = args.index(i) + 1
    return dict_1
print(func('x', 5, 'John'))


# Третья функция
def func(*args):
    number_list = [numbers for numbers in args]
    a = list(filter(lambda num_1: num_1 % 2 == 0, number_list))
    b = [(lambda num_2: num_2 ** 2)(num_2) for num_2 in number_list]
    return a, b
a, b = func(1, 2, 3, 4, 5)
print(a)
print(b)
