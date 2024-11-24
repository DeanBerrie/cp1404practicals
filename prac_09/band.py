"""
CP1404 Prac09
Band class
Dean Berrie
"""


class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return str(vars(self))

    def add_musician(self, musician):
        self.musicians.append(musician)