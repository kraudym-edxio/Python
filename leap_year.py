"""
    leap_year.py
    Created by: Edxio Kraudy Mora
    Date: November 27, 2019
"""

#Ask user to input a year
year = int (input("Type in a year to determine whether it is a leap year: "))

#Determine if the year is a century year
if year % 100 == 0:

    if year % 400 == 0:
        print("The year %d is a leap year." %year)

    else:
        print("The year %d is not a leap year." %year)

#Process if year is not century year
else:

    if year % 4 == 0:
        print("The year %d is a leap year." %year)

    else: 
        print("The year %d is not a leap year." %year)

        
