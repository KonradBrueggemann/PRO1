class Physical_Entity:
    def __init__(self, age, function, invention, maxAge):
        self.age = age
        self.function = function
        self.invention = invention
        self.maxAge = maxAge

    def aging(self, years):
        """

        Precondition:
        age < maxAge
        age, maxAge must be of the Type int.

        """
        assert self.age < self.maxAge, "The physical entity has reached its maximum age."
        assert type(self.age) == int and type(self.maxAge) == int, "Wrong Format"

        self.age += years
        if self.age > self.maxAge:
            self.function = False

class Machine(Physical_Entity):
        def __init__(self, age, function, invention, maxAge, difficulties):
            Physical_Entity.__init__(self, age, function, invention, maxAge)
            self.difficulties = difficulties

        def repair(self):
            """

            Precondition:
           There must be difficulties.

            """
            assert self.difficulties == True and self.function == False, "You can't repair a running machine."
            self.function = True
            self.difficulties = False
            print("Your machine has been fixed.")

class MilkingMachine(Machine):
    def __init__(self,age, function, invention, maxAge, difficulties, milk):
        Machine.__init__(self,age, function, invention, maxAge, difficulties)
        self.milk = milk

    def milking(self, load):
        """

        Precondition:
        Milk and load must be of the type int

        """
        assert type(self.milk) == int and type(load) == int, "Wrong Format"
        self.milk += load

class Zamboni(Machine):
    def __init__(self,age, function, invention, maxAge, difficulties, smoothness):
        Machine.__init__(self,age, function, invention, maxAge, difficulties)
        self.smoothness = smoothness

    def smoothing(self):
        """

        Precondition:
        Smoothness = False
        Smoothness must be of the type bool.

        """
        assert self.smoothness == False, "You can't smooth something that is already smooth."

        self.smoothness = True


