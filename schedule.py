import time
from typing import Optional

import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By

from constants import SCHEDULE_LINK
from time_tools import get_current_day_id, get_current_class_id


class Schedule:
    def __init__(self):
        self.driver = webdriver.Chrome('C://software/chromedriver.exe')

    def get_current_link(self) -> Optional[str]:
        self.driver.get(SCHEDULE_LINK)
        time.sleep(10)
        all_links = self.driver.find_elements(By.CLASS_NAME, "timetable-cell")
        all_links = all_links[7:]
        day_id = get_current_day_id()
        if not day_id:
            return None
        elements = [all_links[index] for index in range(len(all_links)) if index % 6 == day_id]
        current_class = get_current_class_id()
        if not current_class:
            return None
        try:
            current_class_link = elements[current_class].find_element(By.CLASS_NAME, 'url').get_property('href')
        except selenium.common.ElementNotSelectableException:
            return None
        return current_class_link
