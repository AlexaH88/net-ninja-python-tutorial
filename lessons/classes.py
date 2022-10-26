# using specific values, on one planet
# class Planet:

#     def __init__(self):
#         self.name = 'Hoth'
#         self.radius = 200000
#         self.gravity = 5.5
#         self.system = 'Hoth System'

#     def orbit(self):
#         return f'{self.name} is orbiting in the {self.system}'


# hoth = Planet()
# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(f'The gravity is: {hoth.gravity}')
# print(hoth.orbit())


# allowing for customisation for each new instance of Planet() class
class Planet:

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'The gravity is: {hoth.gravity}')
print(hoth.orbit())


naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(f'Name: {naboo.name}')
print(f'Radius: {naboo.radius}')
print(f'Gravity: {naboo.gravity}')
print(naboo.orbit())
