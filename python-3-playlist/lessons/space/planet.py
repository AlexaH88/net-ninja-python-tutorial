class Planet:

    # class-level attributes, that are shared across all instances (each new planet)
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
