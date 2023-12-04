# stars, top 50 locations to have problems
# I need to check all 50 stars by Dec 25
# calibration doc has lines of text, each with a calibration value.
# combining first digit and last digit to form a 2 digit number

file = open("day-1-input.txt", "r")
lines = file.readlines()
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
num_string = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
accumulator = 0

for line in lines:
    first_digit = 0
    last_digit = 0

    for char in line:
        if char in numbers:
            index = numbers.index(char)
            if first_digit == 0:
                first_digit = index
            last_digit = index

    accumulator += int(str(first_digit) + str(last_digit))
