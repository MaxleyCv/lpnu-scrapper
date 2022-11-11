from datetime import datetime
from typing import Optional

from constants import DAYS


class Time:
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    def __ge__(self, other):
        return other.hour <= self.hour and other.minute <= self.minutes

    def __le__(self, other):
        return other.hour >= self.hour and other.minute >= self.minutes


CLASSES = [
    [Time(8, 30), Time(10, 0)],
    [Time(10, 20), Time(10, 40)],
    [Time(12, 10), Time(13, 25)],
    [Time(14, 15), Time(15, 55)],
    [Time(16, 0), Time(17, 35)],
    [Time(17, 40), Time(19, 15)]
]


def time_between(main_time: datetime, lower: Time, upper: Time) -> bool:
    return lower <= main_time <= upper


def get_current_class_id():
    for index in range(6):
        time = datetime.now()
        if time_between(time, *CLASSES[index]):
            return index
    return None


def get_current_day_id() -> Optional[int]:
    day = datetime.now().strftime("%a")
    return DAYS.index(day)
