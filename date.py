# Author : Jose Tellez and Gabriel Lebre

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


    if is_leap_year(year) and (month == 1 or month == 2):
        month_code += 6

    year_offset = calculate_year_offset(year)

    addition = (number_of_twelves_in_last_digits +
                remainder +
                number_of_fours_in_remainder +
                day +
                month_code +
                year_offset)

    modulo_of_addition = addition % 7
    day_code = get_day_code(modulo_of_addition)

    return day_code


def get_day_code(modulo):
    """
    Takes the modulo as an int and returns a day of the wek
    :param modulo: as int
    :return: day of week as string
    """
    day = None

    if modulo == 0:
        day = "Saturday"
    elif modulo == 1:
        day = "Sunday"
    elif modulo == 2:
        day = "Monday"
    elif modulo == 3:
        day = "Tuesday"
    elif modulo == 4:
        day = "Wednesday"
    elif modulo == 5:
        day = "Thursday"
    elif modulo == 6:
        day = "Friday"
    else:
        print("bad day")
    return day


def get_month_code(month):
    """
    Reads month , as an int , and then evaluates conditional to find the appropriate code
    Key: Month , Value:Code
    :param month: Mont of the year , in number
    :return: month code
    """
    month_code = None
    if month == 1:
        month_code = 1
    elif month == 2:
        month_code = 4
    elif month == 3:
        month_code = 4
    elif month == 4:
        month_code = 0
    elif month == 5:
        month_code = 2
    elif month == 6:
        month_code = 6
    elif month == 7:
        month_code = 0
    elif month == 8:
        month_code = 3
    elif month == 9:
        month_code = 6
    elif month == 10:
        month_code = 1
    elif month == 11:
        month_code = 4
    elif month == 12:
        month_code=6
    else:
        print("oops")
    return month_code


def calculate_year_offset(year):
    """
    Calculates year offset based on the year passed
    :param year in number
    :return:the leap year code offset
    """
    first_two_digits = year//100
    if first_two_digits == 16:
        return 6
    elif first_two_digits == 17:
        return 4
    elif first_two_digits == 18:
        return 2
    elif first_two_digits == 19:
        return 0
    elif first_two_digits == 20:
        return 6
    elif first_two_digits == 21:
        return 4
    else:



def is_leap_year(year):
    """
    Returns true if a year is a leap year
    :param year: year in numbers
    :return: true if the year is a leap year , false if is not a leap year
    """
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 400 != 0:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
