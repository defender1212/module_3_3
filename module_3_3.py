#Часть 1
def print_params(a=1, b='строка', c = True):
    print(a, b, c)
print_params()
print_params(b=2, c='f')
print_params(a=3, b='новое значение', c=False)
print_params(a=5)
print_params(b = 25)
print_params(c = [1,2,3])

#Часть 2
values_list = [1, 'цветок', True]
values_dict = {'a':12, 'b':"список", 'c':False}
print_params(*values_list)
print_params(**values_dict)

#Часть 3
values_list_2 = [45, 'Pencere']
print_params(*values_list_2, 42)

