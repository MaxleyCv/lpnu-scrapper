from datetime import datetime


class Time:
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    def __ge__(self, other):
        return other.hour <= self.hour and other.minute <= self.minutes

    def __le__(self, other):
        return other.hour >= self.hour and other.minute >= self.minutes


ZOOM_API = 'https://zoom.us/join'
CHROME_DRIVER = 'C://software/chromedriver.exe'
SCHEDULE_LINK = 'https://zubiden.github.io/nulp-timetable/#/%D0%86%D0%A0-41/1'
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
CLASSES = [
    [Time(8, 30), Time(10, 0)],
    [Time(10, 20), Time(10, 40)],
    [Time(12, 10), Time(13, 25)],
    [Time(14, 15), Time(15, 55)],
    [Time(16, 0), Time(17, 35)],
    [Time(17, 40), Time(19, 15)]
]