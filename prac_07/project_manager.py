from project import Project
import datetime

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- "
        "(A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    print("Welcome to pythonic project manager")
    projects = get_projects()
    print(f'Loaded {len(projects)} projects from {FILENAME}')
    print(MENU)
    user_input = input(">>>").upper()
    while user_input != "Q":
        if user_input == "L":
            projects = get_projects()
            print(f'Loaded {len(projects)} projects from {FILENAME}')
        elif user_input == "S":
            write_to_file(projects)
        elif user_input == "D":
            for project in projects:
                print(project)
        elif user_input == "F":
            user_star_date = input("Show project that start after date ")
            print(project for project in projects if project > user_star_date)
        elif user_input == "A":
            name = input("Name: ")
            start_date = input("start date: ")
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost: "))
            percent_complet = int(input("Percent Complete: "))
            project = Project(name, start_date, priority, cost_estimate, percent_complet)
            projects.append(project)
            print(f'{project} added.')
        elif user_input == "U":
            update_project(projects)

        else:
            print("Invalid")
        user_input = input(">>>").upper()
    user_save = input("Would you like to save Y/N: ").upper()
    if user_save == "Y":
        write_to_file(projects)
    print("Thank you for using custom-built project management software.")


def update_project(projects):
    for i, project in enumerate(projects, 0):
        print(f'{i} {project}')
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = int(input("New percentage: "))
    projects[project_choice][4] = new_percentage


def write_to_file(projects):
    with open(FILENAME, "w") as out_file:
        for project in projects:
            print(project, file=out_file)
    print(f'{len(projects)} places have been saved to {FILENAME}')


def get_projects():
    projects = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


main()
