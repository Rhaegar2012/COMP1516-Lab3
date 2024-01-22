# Author : Jose Tellez

def main():
    """
    Execute program
    :return: true or false for each one of the tests written below
    """
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Monday" == get_day_of_the_week(12, 18, 1899))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))


def get_day_of_the_week(month, day, year):
    """
    Receives a date and returns the name of the day of the week for that day, month, year
    :param month: month in numbers
    :param day: day in numbers
    :param year: year in numbers
    :return: Day name as string
    """
    last_two_digits_of_year = year % 100
    number_of_twelves_in_last_digits = last_two_digits_of_year // 12
    remainder = last_two_digits_of_year - (number_of_twelves_in_last_digits * 12)
    number_of_fours_in_remainder = remainder // 4
    month_code = get_month_code(month)
    if is_leap_year(year):
        if month == 1 or month == 2:
            month_code += 6
    year_offset = calculate_year_offset(year)
    addition = (number_of_twelves_in_last_digits +
                remainder +
                number_of_fours_in_remainder +
                day +
                month_code +
                year_offset)
    modulo_of_addition = addition % 7
    day_code = {0: "Saturday", 1: "Sunday", 2: "Monday",
                3: "Tuesday", 4: "Wednesday", 5: "Thursday",
                6: "Friday"}

    return day_code[modulo_of_addition]


def get_month_code(month):
    """

    :param month: Mont of the year , in number
    :return: month code
    """
    month_code = {1: 1, 2: 4, 3: 4,
                  4: 0, 5: 2, 6: 5,
                  7: 0, 8: 3, 9: 6,
                  10: 1, 11: 4, 12: 6}
    return month_code[month]
def calculate_year_offset(year):
    """
    Calculates year offset based on the year passed
    :param year in number
    :return:the leap year code offset
    """
    first_two_digits = year//100
    if first_two_digits == 16:
        return 6
    if first_two_digits == 17:
        return 4
    if first_two_digits == 18:
        return 2
    if first_two_digits == 19:
        return 0
    if first_two_digits == 20:
        return 6
    if first_two_digits == 21:
        return 4


def is_leap_year(year):
    """

    :param year: year in numbers
    :return: true if the year is a leap year , false if is not a leap year
    """
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        if year % 100 != 0:
            return True
        if year % 100 == 0 and year % 400 != 0:
            return False
    else:
        return False


if __name__ == "__main__":
    main()


