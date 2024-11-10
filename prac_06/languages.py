"""
CP1404 Prac 6
Languages
Estimated time: 20 minutes
Time taken: 15 minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.language)


main()
