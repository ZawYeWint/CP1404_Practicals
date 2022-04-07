"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Start of Program"""
    subject_details = get_data()
    print_subjects(subject_details)

    print("End of Program")


def print_subjects(subject_details):
    """Display subject, lecturer and number of students"""
    for subject_data in subject_details:
        print(subject_details[0], subject_details[1], subject_details[2])
        print(f"{subject_details[0]} is taught by {subject_details[1]:12} and has {subject_details[2]:3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_details = [parts[0], parts[1], parts[2]]  # Subject ID, Lecturer and Number of Students
        subject_details.append(subject_details)

    input_file.close()
    return subject_details


main()
