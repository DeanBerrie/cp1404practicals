class ProgrammingLanguage:
    """Represent a Programming Language object"""

    def __init__(self, language="", typing="", reflection=False, year=0):
        """Construct a programming language from the given values"""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Display the Programming Languages object as a string"""
        return f'{self.language}, {self.typing} typing, reflection={self.reflection}, First appeared in {self.year}'

    def is_dynamic(self):
        """Determine if language is dynamically typed"""
        return self.typing == 'Dynamic'

