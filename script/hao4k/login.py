

from lib2to3.pgen2.token import tok_name
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from settings import Setting
class Login:
  def __init__(self) -> None:
    self.LOGIN_RESULT = False
    self.my_chrome_options = Options()
    self.my_chrome_options.add_argument('--headlesss')
    self.driver = webdriver.Chrome(options=self.my_chrome_options)

    self.settings = Setting()

  def DefaultLoginWay(self):
    print("登录")
    #登录连接
    self.driver.get(self.settings.LOGIN_URL)
    username_input = WebDriverWait(self.driver, '10').until(
            EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]'))
        )
    username_input.send_keys(self.settings.USERNAME)
    password_input =WebDriverWait(self.driver, '10').until(
            EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/div[1]/input[1]'))
                                                       
        )
    password_input.send_keys(self.settings.PASSWORD)

    login_button = WebDriverWait(self.driver, '10').until(
            EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/form[1]/button[1]'))
                                                       
        )
    login_button.click()
    #验证码图片
    verification_code = WebDriverWait(self.driver, '10').until(
            EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/img[1]'))
                                                       
        )
    # #
    # login_button.click()
    time.sleep(5)

  def LoginByCookie(self):
    print("以session方式登录")
