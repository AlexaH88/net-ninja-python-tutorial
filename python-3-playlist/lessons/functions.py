# def greet(name, time):
#     print(f'Good {time}, {name}, hope you are well')


# # name = input('Enter your name: ')
# # time = input('Enter the time of day: ')

# greet(name, time)


# gives a default value to the parameters that runs if none are entered
# def greet(name='ryu', time='morning'):
#     print(f'Good {time}, {name}, hope you are well')


# # name = input('Enter your name: ')
# # time = input('Enter the time of day: ')

# greet()


def area(radius):
    return 3.142 * radius * radius


def vol(area, length):
    print(area * length)


radius = int(input('Enter a radius: '))
length = int(input('Enter a length: '))

#  create a variable to be able to pass it into the vol function calculation
# area_calc = area(radius)
# vol(area_calc, length)

# OR pass the function straight into the other function
vol(area(radius), length)
