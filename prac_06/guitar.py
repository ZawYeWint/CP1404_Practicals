CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return "f{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True if the guitar is 50 or more years old, False otherwise
        Hint: try using get_age() to simplify the implementation of this method"""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year
