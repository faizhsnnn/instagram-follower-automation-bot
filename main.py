import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "YOUR_IG_USERNAME"
PASSWORD = "YOUR_IG_PASS"
SIMILAR_ACC = "instagram"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):

        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(5)

        username = self.driver.find_element(by=By.XPATH, value='//*[@id="_R_32d9lplcldcpbn6b5ipamH1_"]')
        password = self.driver.find_element(by=By.XPATH, value='//*[@id="_R_33d9lplcldcpbn6b5ipamH1_"]')
        
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)

        login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div/div[1]')
        login_button.click()

        time.sleep(5)

        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
                save_login_prompt.click()

        time.sleep(2)

        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
                notifications_prompt.click()

    def find_followers(self):

        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}/")
        time.sleep(5)

        wait = WebDriverWait(self.driver, 10)

        followers_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/followers')]"))
        )

        followers_link.click()

        time.sleep(5)

        # THIS is the correct scroll container
        # wait until the followers dialog appears
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))

        # scroll the popup itself
        for _ in range(3):
            self.driver.execute_script("""
                const dialog = document.querySelector('div[role="dialog"]');
                dialog.scrollTop = dialog.scrollHeight;
            """)
            time.sleep(2)

    def follow(self):

        wait = WebDriverWait(self.driver, 10)

        # wait until at least one Follow button appears
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//button")))

        # get buttons inside the followers dialog
        buttons = self.driver.find_elements(By.XPATH, "//div[@role='dialog']//button")

        count = 0

        for button in buttons:
            try:
                if button.text == "Follow":
                    button.click()
                    count += 1
                    time.sleep(2)

                    if count == 5:
                        break

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Cancel')]")
                cancel_button.click()


bot = InstaFollower()

bot.login()
time.sleep(5)

bot.find_followers()
time.sleep(3)

bot.follow()