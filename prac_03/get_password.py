"""
Description: A simple password checker
Name: Patrick
"""


def is_valid_password(text):
    """Check whether a given text has correct password format"""
    return 8 <= len(text) <= 20 and "#" in text


def main():
    new_password = "helloworld#"
    print(f"{new_password} is a valid password? {is_valid_password(new_password)}")


if __name__ == '__main__':
    main()
