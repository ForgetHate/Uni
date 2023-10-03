import datetime
from datetime import datetime

if __name__ == '__main__':
    name = input("Hello, what is your name? ")

    year_now = datetime.now().year
    year_born = int(input("What year was you born? "))

    age = year_now - year_born

    print(f"Hello, {name}. You will be {age} this year.")
