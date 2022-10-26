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
    #class-level attributes, that are shared across all instances (each new planet)
    shape = 'round'

    # instance attributes that are specific to each individual instance of the class (each new planet)
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    # creating a class-level method (function)
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'The planet spins and spins at {speed}'


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
# accessing class-level attributes
print(Planet.shape)
# or can be accessed via the instance as it inherits the attribure from the class
print(naboo.shape)
# accessing class-level methods
print(Planet.commons())
# or can be accessed via the instance as it inherits the attribure from the class
print(naboo.commons())

# accessing static method, which needs a parameter input, or it runs the default
print(Planet.spin('a very high speed'))
# also works on the variable instance
print(naboo.spin('a very high speed'))
