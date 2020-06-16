import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': '.\data\chicago.csv',
             'new york city': '.\data\\new_york_city.csv',
             'washington': '.\data\washington.csv'}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

LINE_LEN = 90

# print long string with repeating char, used to separate sections of output
print_line = lambda char: print(char[0] * LINE_LEN)


def print_processing_time(start_time):
    time_str = "[... %s seconds]" % round((time.time() - start_time), 3)
    print(time_str.rjust(LINE_LEN))
    print_line('-')


def get_filter_city():
    """
    Asks user to specify a city.
    Returns:
        (str) city - name of the city to analyze
    """
    # build and display the list of cities for which we have datasets
    cities_list = []
    num_cities = 0

    for a_city in CITY_DATA:
        cities_list.append(a_city)
        num_cities += 1
        print('        {0:20}. {1}'.format(num_cities, a_city.title()))

    # ask user to input a number for a city from the list; easier for user than string input
    while True:
        try:
            city_num = int(input("\n    Enter a number for the city (1 - {}):  ".format(len(cities_list))))
        except:
            continue

        if city_num in range(1, len(cities_list) + 1):
            break

    # get the city's name in string format from the list
    city = cities_list[city_num - 1]
    return city


def get_filter_month():
    """
    Asks user to specify a month to filter on, or choose all.
    Returns:
        (str) month - name of the month to filter by, or "all" for no filter
    """
    while True:
        try:
            month = input("    Enter the month with January=1, June=6 or 'a' for all:  ")
        except:
            print("        ---->>  Valid input:  1 - 6, a")
            continue

        if month == 'a':
            month = 'all'
            break
        elif month in {'1', '2', '3', '4', '5', '6'}:
            # reassign the string name for the month
            month = MONTHS[int(month) - 1]
            break
        else:
            continue

    return month


def get_filter_day():
    """
    Asks user to specify a day to filter on, or choose all.
    Returns:
        (str) day - day of the week to filter by, or "all" for no filter
    """
    while True:
        try:
            day = input("    Enter the day with Monday=1, Sunday=7 or 'a' for all:  ")
        except:
            print("        ---->>  Valid input:  1 - 7, a")
            continue

        if day == 'a':
            day = 'all'
            break
        elif day in {'1', '2', '3', '4', '5', '6', '7'}:
            # reassign the string name for the day
            day = WEEKDAYS[int(day) - 1]  # here we MUST -1 to get correct index
            break
        else:
            continue

    return day


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print_line('=')
    print('\n  Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington).
    #  HINT: Use a while loop to handle invalid inputs

    city = get_filter_city()

    # get user input for month (all, january, february, ... , june)
    month = get_filter_month()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_filter_day()

    return city, month, day


def filter_summary(city, month, day, init_total_rides, df):
    """
    Displays selected city, filters chosen, and simple stats on dataset.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (int) init_total_rides - total number of rides in selected city before filter
        (dataframe) df - filtered dataset
    """
    start_time = time.time()

    filtered_rides = len(df)
    num_stations_start = len(df['Start Station'].unique())
    num_stations_end = len(df['End Station'].unique())

    print('  Gathering statistics for:      ', city)
    print('    Filters (month, day):        ', month, ', ', day)