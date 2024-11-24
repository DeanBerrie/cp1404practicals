"""
CP1404 Prac09
Silver service taxi
Dean Berrie
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represents a silver service taxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """returns a string representation of silver service taxi"""
        return f'{super().__str__()} plus flagfall of ${self.flagfall}'

    def get_fare(self):
        """get fare"""
        return self.flagfall + super().get_fare()