from lib2to3.pgen2.token import tok_name
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from settings import Setting
from verificationCode import VerificationCodeRecognition


class Login:
    def __init__(self) -> None:
        self.LOGIN_RESULT = False
        self.my_chrome_options = Options()
        # self.my_chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.my_chrome_options)
        self.driver.set_window_size(1920, 1080)
        self.settings = Setting()

    # 验证码登录
    def default_login_way(self):
        print("登录")
        # 登录连接
        self.driver.get(self.settings.LOGIN_URL)
        username_input = WebDriverWait(self.driver, '10').until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div['
                                            '1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]'))
        )
        username_input.send_keys(self.settings.USERNAME)
        password_input = WebDriverWait(self.driver, '10').until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div['
                                            '1]/div[1]/form[1]/div[2]/div[2]/div[1]/input[1]'))
        )
        password_input.send_keys(self.settings.PASSWORD)

        login_button = WebDriverWait(self.driver, '10').until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div['
                                            '1]/div[1]/form[1]/button[1]'))

        )
        login_button.click()
        time.sleep(1.8)
        # 验证码图片
        verification_code = WebDriverWait(self.driver, '10').until(
            EC.presence_of_element_located(
                (By.XPATH, '/html[1]/body[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]'))
        )
        verification_code_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html[1]/body[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]'))
        )
        verification_code_login_button = self.driver.find_elements(By.XPATH, '/html[1]/body[1]/div[4]/div[2]/div[1]/div[1]/div[3]/div[1]/button[1]')
        login_times = 0
        # 目前以是否有
        while len(verification_code_login_button) > 0:
            verification_code_input.clear()
            if login_times > 0:
                verification_code.click()
            time.sleep(1.8)
            verification_code.screenshot('verification_code.png')
            temp = login_times
            print("开始第" + str(temp+1) + '次登录')
            vcode_rec = VerificationCodeRecognition()
            vcode_rec.recognition('verification_code.png')
            if vcode_rec.VCODE is not None:
                verification_code_input.send_keys(vcode_rec.VCODE)
            else:
                print("验证码识别失败!")
            verification_code_login_button[0].click()
            time.sleep(2)
            verification_code_login_button = self.driver.find_elements(By.XPATH, '/html[1]/body[1]/div[4]/div[2]/div[1]/div[1]/div[3]/div[1]/button[1]')
            login_times += 1

        # 跳转登录
        to_sign_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html[1]/body[1]/div[11]/div[6]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/div[1]/p[1]/a[1]'))
        )
        to_sign_button.click()
        self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles)-1])
        time.sleep(5)
        sign_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[9]/div[2]/div[1]/div[1]/a[1]'))
        )
        sign_button.click()
        time.sleep(3)

    # cookie登录
    def login_by_cookie(self):
        print(self.LOGIN_RESULT)
