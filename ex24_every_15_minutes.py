# Exercise 24 - Every 15 Minutes


"""
    Clocks have an unusual counting system compared to the normal
    decimal number system we're familiar with.
    Instead of beginning at 0 and going to 1, 2, and so on forever,
    clocks start at 12 and go on to 1, 2, and so on up to 11.
    Then it loops back to 12 again.
    (Clocks are quite odd if you think about it:
    12 am comes before 11 am and 12 pm comes before 11 pm.)
"""


def get_time_for_every_15_minutes() -> str:
    """
    Generate time strings for every 15-minute interval in a 12-hour day.

    Returns:
        str: Newline-separated time values from '12:00 am' through '11:45 pm', formatted as 'H:MM am/pm'.
    """

    periods = ('am', 'pm')
    hours = 12
    minute_interval = 15

    lines = []

    for period in periods:
        for hour in range(hours):
            display_hour = 12 if hour == 0 else hour

            for minute in range(0, 60, minute_interval):
                time_line = f'{display_hour}:{minute:02d} {period}'
                lines.append(time_line)

    return '\n'.join(lines)


print(get_time_for_every_15_minutes())
