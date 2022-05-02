"""Call your class ProgrammingLanguage (using Python's recommended "PascalCase" or "CapWords" style)"""


class ProgrammingLanguage:
    """create the fields and set them to the parameters passed in"""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of ProgrammingLanguage"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def check_dynamic(self):
        """Returns True/False if the programming language is dynamically typed or not."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    for language in languages:
        if language.check_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
