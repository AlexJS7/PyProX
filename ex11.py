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


def get_hours_minutes_seconds(total_seconds):
    if total_seconds == 0:
        return '0s'

    # how many seconds left
    s = total_seconds

    d = total_seconds // DAY
    s = s - d * DAY

    h = s // HOUR
    s = s - h * HOUR

    m = s // MINUTE
    s = s - m * MINUTE

    hms = [f'{d}d', f'{h}h', f'{m}m', f'{s}s']

    return ' '.join(item for item in hms if item[0] != '0')


assert get_hours_minutes_seconds(90) == '1m 30s'
assert get_hours_minutes_seconds(30) == '30s'
assert get_hours_minutes_seconds(60) == '1m'
assert get_hours_minutes_seconds(90) == '1m 30s'
assert get_hours_minutes_seconds(3600) == '1h'
assert get_hours_minutes_seconds(3601) == '1h 1s'
assert get_hours_minutes_seconds(3661) == '1h 1m 1s'
assert get_hours_minutes_seconds(90042) == '1d 1h 42s'
assert get_hours_minutes_seconds(0) == '0s'
