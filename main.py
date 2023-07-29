'''A mobile cell service provider in Ottawa broadcasts an automated time standard to its mobile users
that reflects the local time at the user’s actual location in Canada. This ensures that text messages
have a valid local time attached to them.
For example, when it is 1420 in Ottawa on Tuesday February 24, 2009 (specified using military,
24 hour format), the times across the country are shown in the table below:
Pacific Time Mountain Time Central Time Eastern Time Atlantic Time Newfoundland Time
Victoria, BC Edmonton, AB Winnipeg, MB Toronto, ON Halifax, NS St. John’s, NL
Tuesday Tuesday Tuesday Tuesday Tuesday Tuesday
2/24/2009 2/24/2009 2/24/2009 2/24/2009 2/24/2009 2/24/2009
1120 PST 1220 MST 1320 CST 1420 EST 1520 AST 1550 Newfoundland ST
Write a program that accepts the time in Ottawa in 24 hour format and outputs the local time in
each of the cities listed above including Ottawa. You should assume that the input time will be
valid (i.e., an integer between 0 and 2359 with the last two digits being between 00 and 59).
You should note that 2359 is one minute to midnight, midnight is 0, and 13 minutes after midnight
is 13. You do not need to print leading zeros, and input will not contain any extra leading zeros.
'''

def calculate_local_time(ottawa_time):
    time_diff = {
        'Victoria': -3,
        'Edmonton': -2,
        'Winnipeg': -1,
        'Toronto': 0,
        'Halifax': 1,
        'St. John’s': 1.5
    }

    ottawa_time = int(ottawa_time)
    print(f"{ottawa_time:04d} in Ottawa")

    for city, diff in time_diff.items():
        local_time = ottawa_time + diff
        print(f"{local_time:04.0f} in {city}")


# Read input
ottawa_time = input()

# Calculate the local time in each city
calculate_local_time(ottawa_time)
