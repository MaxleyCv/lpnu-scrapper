import time

import selenium.common
from selenium import webdriver
import pyautogui as py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class ZoomEnter:
    """
    This class is created to enter a class zoom link through a code
    """
    def __init__(self):

        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
        })

        self.driver = webdriver.Chrome(chrome_options=opt, executable_path='C://software/chromedriver.exe')

    def enter_link(self, link: str) -> None:
        self.driver.get(link)
        self.driver.maximize_window()
        time.sleep(2)
        py.press('enter')
        time.sleep(4)
        join_from_browser_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Join from Your Browser')
        join_from_browser_link.click()

        time.sleep(2)

        input_name = self.driver.find_element(By.ID, 'inputname')
        input_name.send_keys('Максим Ліщинський')

        join_button = self.driver.find_element(By.ID, 'joinBtn')
        join_button.click()

        mute_button = self.driver.find_element(By.ID, 'mic-btn')

        

        time.sleep(1000)


zoom = ZoomEnter()
zoom.enter_link('https://softserveinc.zoom.us/j/99979302138?pwd=dzlMdjgyUXpjcUtSc05oWDd1c3Z6Zz09')


