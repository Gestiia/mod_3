def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(3)
print_params(10, "opa", False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [140, 'for', False]
values_dict = {'a': 102, 'b': '120', 'c': 560.1}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [234, 'lol']
print_params(*values_list_2, 42)
