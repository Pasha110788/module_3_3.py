def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [3, 'string', False]
values_dict = {'a': 5, 'b': 'alex', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [5, 'max']
print_params(*values_list2, 42)
