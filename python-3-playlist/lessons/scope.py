my_name = 'ryu'


def print_name():
    global my_name
    my_name = 'yoshi'
    print('The name inside the function is', my_name)


print_name()
print('Outside the function the name is', my_name)