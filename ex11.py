# Exercise 11 - Hours, Minutes, Seconds

"""
Websites often use relative timestamps such as "3 days ago" or "about 3h ago" so the user
doesn't need to compare an absolute timestamp to the current time.

In this exercise, we write a function that converts a number of seconds
into a string with the number of hours, minutes, and seconds.
"""

MINUTE = 60
HOUR = 60 * MINUTE
DAY = HOUR * 24


def seconds_to_units(total_seconds, unit_seconds):
    units = total_seconds // unit_seconds
    remaining_seconds = total_seconds % unit_seconds

    return units, remaining_seconds


def get_hours_minutes_seconds(total_seconds):
    if total_seconds == 0:
        return '0s'

    d, s = seconds_to_units(total_seconds, DAY)
    h, s = seconds_to_units(s, HOUR)
    m, s = seconds_to_units(s, MINUTE)

    hms = [f'{d}d', f'{h}h', f'{m}m', f'{s}s']

    return ' '.join(item for item in hms if item[0] != '0')


assert get_hours_minutes_seconds(30) == '30s'
assert get_hours_minutes_seconds(60) == '1m'
assert get_hours_minutes_seconds(90) == '1m 30s'
assert get_hours_minutes_seconds(3600) == '1h'
assert get_hours_minutes_seconds(3601) == '1h 1s'
assert get_hours_minutes_seconds(3661) == '1h 1m 1s'
assert get_hours_minutes_seconds(90042) == '1d 1h 42s'
assert get_hours_minutes_seconds(0) == '0s'
assert get_hours_minutes_seconds(1) == '1s'
