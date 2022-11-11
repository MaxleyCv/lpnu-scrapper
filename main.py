import time

from schedule import Schedule
from zoom_api import ZoomEnter

if __name__ == '__main__':
    schedule = Schedule()
    zoom = ZoomEnter()
    while True:
        link = schedule.get_current_link()
        if link:
            zoom.enter_link(link)
        time.sleep(1000)
