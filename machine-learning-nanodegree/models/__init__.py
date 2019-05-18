# Passengers module to wrap all passengers related info

class Passenger(object):
    def __init__(self, survived=None, pclass=None, name=None, sex=None,
                 age=None, sibsp=None, parch=None, ticket=None, fare=None, cabin=None, embarked=None):

        self.survived = survived
        self.pclass = pclass
        self.name = name
        self.sex = sex
        self.age = age
        self.sibsp = sibsp
        self.parch = parch
        self.ticket = ticket
        self.fare = fare
        self.cabin = cabin
        self.embarked = embarked


