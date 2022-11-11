import datetime
import time
from typing import Optional

import selenium.common
from selenium import webdriver
import pyautogui as py
from selenium.webdriver.common.by import By

from constants import SCHEDULE_LINK, DAYS, CLASSES


class Schedule:
    def __init__(self):
        self.driver = webdriver.Chrome('C://software/chromedriver.exe')

    def time_between(self, main_time, lower, upper):
        return lower <= main_time <= upper

    def get_current_class_id(self):
        for index in range(6):
            time = datetime.datetime.now()
            if self.time_between(time, *CLASSES[index]):
                return index
        return None

    def get_current_day_id(self) -> Optional[int]:
        day = datetime.datetime.now().strftime("%a")
        print(datetime.datetime.now().strftime("%a, %H:%M"))
        return DAYS.index(day)

    def get_current_link(self) -> Optional[str]:
        self.driver.get(SCHEDULE_LINK)
        time.sleep(10)
        all_links = self.driver.find_elements(By.CLASS_NAME, "timetable-cell")
        all_links = all_links[7:]
        day_id = self.get_current_day_id()
        if not day_id:
            return None
        elements = [all_links[index] for index in range(len(all_links)) if index % 6 == day_id]
        current_class = 3
        if not current_class:
            return None
        try:
            current_class_link = elements[current_class].find_element(By.CLASS_NAME, 'url').get_property('href')
        except selenium.common.ElementNotSelectableException:
            return None
        return current_class_link


sched = Schedule()
print(sched.get_current_link())
