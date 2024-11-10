class Guitar:
    """Class for storing guitar details"""
    current_year = 2024
    vintage = 50

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display the Guitar object in string formatting"""
        return f'{self.name} ({self.year}) : ${self.cost}'

    def get_age(self):
        """Get the age of the guitar based on the current year"""
        return self.current_year - self.year

    def is_vintage(self):
        """Determine is guitar is vintage (greater than 50 years old)"""
        return self.get_age() >= self.vintage
