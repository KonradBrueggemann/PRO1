class user_data:
    def __init__(self, age=None, name=None, tradition=None, santa=None, colour=None, season=None):
        self.age = age
        self.name = name
        self.tradition = tradition
        self.santa = santa
        self.colour = colour
        self.season = season

    def attributes(self):
        return {"age": self.age,
                "name": self.name,
                "tradition": self.tradition,
                "santa": self.santa,
                "colour": self.colour,
                "season": self.season}

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_tradition(self):
        return self.tradition

    def get_santa(self):
        return self.santa

    def get_colour(self):
        return self.colour

    def get_season(self):
        return self.season
