from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Capstone.Test_Data import data
from Capstone.Test_Locator import locators
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class Test_Project:
# Boot method to run Pytest using POM
   @pytest.fixture
   def setup(self):
      # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()))
      service = Service(executable_path="C:\\Users\\Nandhu\\Downloads\\chromedriver_win32\\chromedriver.exe")
      self.driver = webdriver.Chrome(service=service)
      self.driver.maximize_window()
      self.wait = WebDriverWait(self.driver, 20)
      yield
      self.driver.close()

      # Test_case: TC_PIM_01 Forgot password link


   def test_forgot_page(self,setup):  # Test case: TC_PIM_01
       self.driver.get(data.Data().url)
       forgot_pass = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().forgot_btn)))
       forgot_pass.click()

       username_field = self.wait.until(
           EC.visibility_of_element_located((By.NAME, locators.Locators().username_textbox)))
       username_field.send_keys(data.Data().Username)

       reset = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Locators().reset_btn)))
       reset.click()
       after_url = self.driver.current_url

       try:

           if data.Data().before_url != after_url:
               print("Reset Password link sent successfully")
           elif data.Data().before_url == after_url:
               print("Username Required!!")

       except TimeoutException as e:
           print(e)

   def test_invalid_case(self,setup):
       self.driver.get(data.Data().url)
       forgot_pass = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().forgot_btn)))
       forgot_pass.click()

       username_field = self.wait.until(
           EC.visibility_of_element_located((By.NAME, locators.Locators().username_textbox)))
       username_field.send_keys(data.Data().Username1)

       reset = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Locators().reset_btn)))
       reset.click()
       after_url = self.driver.current_url

       try:

           if data.Data().before_url != after_url:
               print("Reset Password link sent successfully")
           elif data.Data().before_url == after_url:
               print("Username Required!!")

       except TimeoutException as e:
           print(e)

   def test_invalid(self,setup):
       self.driver.get(data.Data().url)
       forgot_pass = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().forgot_btn)))
       forgot_pass.click()

       username_field = self.wait.until(
           EC.visibility_of_element_located((By.NAME, locators.Locators().username_textbox)))
       username_field.send_keys(data.Data().Username2)

       reset = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Locators().reset_btn)))
       reset.click()
       after_url = self.driver.current_url

       try:

           if data.Data().before_url != after_url:
               print("Reset Password link sent successfully")
           elif data.Data().before_url == after_url:
               print("Username Required!!")

       except TimeoutException as e:
           print(e)
   def test_invalid_2(self,setup):
       self.driver.get(data.Data().url)
       forgot_pass = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().forgot_btn)))
       forgot_pass.click()

       username_field = self.wait.until(
           EC.visibility_of_element_located((By.NAME, locators.Locators().username_textbox)))
       username_field.send_keys(data.Data().Username3)

       reset = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Locators().reset_btn)))
       reset.click()
       after_url = self.driver.current_url

       try:

           if data.Data().before_url != after_url:
               print("Reset Password link sent successfully")
           elif data.Data().before_url == after_url:
               print("Username Required!!")

       except TimeoutException as e:
           print(e)


   def test_negative_case(self,setup):
       self.driver.get(data.Data().url)
       forgot_pass = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().forgot_btn)))
       forgot_pass.click()

       username_field = self.wait.until(
           EC.visibility_of_element_located((By.NAME, locators.Locators().username_textbox)))
       username_field.send_keys(data.Data().Username4)

       reset = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Locators().reset_btn)))
       reset.click()
       after_url = self.driver.current_url

       try:

           if data.Data().before_url != after_url:
               print("Reset Password link sent successfully")
           elif data.Data().before_url == after_url:
               print("Username Required!!")

       except TimeoutException as e:
           print(e)


   def test_admin_page(self,setup):
       self.driver.get(data.Data().url)
       try:
           username_field = self.wait.until(
               EC.presence_of_element_located((By.NAME, locators.login_page().username_box)))
           username_field.send_keys(data.login().username)

           pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.login_page().password_box)))
           pswrd_field.send_keys(data.login().password)

           button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.login_page().login_btn)))
           button.click()
           admin = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.login_page().admin_click)))
           admin.click()
           actual_title = self.driver.title

           if actual_title == data.login().expected_title:
               print("---------------------Header Validation!!-----------------------")

           ad = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.login_page().ad)))
           li_elements = ad.find_elements(By.TAG_NAME, locators.login_page().li_elements)
           print(len(li_elements))

           for expected_option in data.login().expected_options:
               for option_element in li_elements:
                   if expected_option in option_element.text:
                       print(f"{expected_option} option is displayed.")

       except TimeoutException as e:
              print(e)
   def test_admin_validation(self,setup):
       try:
           self.driver.get(data.Data().url)

           username_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.login_page().username_box)))
           username_field.send_keys(data.login().username)

           pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.login_page().password_box)))
           pswrd_field.send_keys(data.login().password)

           button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.login_page().login_btn)))
           button.click()
           admin = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.login_page().admin_click)))
           admin.click()
           actual_title = self.driver.title
           expected_title = "OrangeHRM"

           if expected_title == actual_title:
              print("---------------------Header Validation!!-----------------------")
           User_Management = self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.login_page().User_Management )))
           if User_Management.is_displayed():
              print("User Management is Displayed!!")
           Job = self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.login_page().Job )))
           if Job.is_displayed():
              print("Job is Displayed!!")
           Organization = self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.login_page().Organization )))
           if Organization.is_displayed():
              print("Organization is Displayed!!")
           Qualifications = self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.login_page().Qualifications)))
           if Qualifications.is_displayed():
              print("Qualifications is Displayed!!")
           Nationalities = self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.login_page().Nationalities )))
           if Nationalities.is_displayed():
              print("Nationalities is Displayed!!")
           Corporate_Branding = self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.login_page().Corporate_Branding)))
           if Corporate_Branding.is_displayed():
              print("Corporate Branding is Displayed!!")
           Configuration = self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.login_page().Configuration )))
           if Configuration.is_displayed():
              print("Configuration is Displayed!!")
           print("All the options are validated and displayed!!")

       except TimeoutException as e:
           print(e)

   def test_main_menu(self,setup):
       try:

           self.driver.get(data.Data().url)

           username_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.login_page().username_box)))
           username_field.send_keys(data.login().username)

           pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.login_page().password_box)))
           pswrd_field.send_keys(data.login().password)

           button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.login_page().login_btn)))
           button.click()

           admin = self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.login_page().admin_click)))
           admin.click()
           menu = self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.login_page().menu)))
           list_elements = menu.find_elements(By.TAG_NAME,locators.login_page().list_elements)
           print(len(list_elements))
           for expected_option in data.login().main_expected_options:
               for option_element in list_elements:
                   if expected_option in option_element.text:
                       print(f"{expected_option} option is displayed.")

           print("All the main menu options are displayed!!")

           # for l in list_elements:
           #     print(l.text + " is displayed ")
           # print("Main menu options are displayed")


       except TimeoutException as e:
           print(e)


   def test_admin_search(self,setup):
       try:
           self.driver.get(data.Data().url)

           username_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.login_page().username_box)))
           username_field.send_keys(data.login().username)

           pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.login_page().password_box)))
           pswrd_field.send_keys(data.login().password)

           button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.login_page().login_btn)))
           button.click()
           search = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search.send_keys(data.login().search)
           admin = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.login_page().admin)))
           if admin.is_displayed():
               print("admin is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(5 * Keys.BACKSPACE)
           search1.send_keys(data.login().search_1)
           admin = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.login_page().admin)))
           if admin.is_displayed():
               print("ADMIN is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(5 * Keys.BACKSPACE)
           search1.send_keys(data.login().search1)
           Pim = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().pim)))
           if Pim.is_displayed():
               print("pim is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(5 * Keys.BACKSPACE)
           search1.send_keys(data.login().search2)
           Pim = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().pim)))
           if Pim.is_displayed():
               print("PIM is displayed!!")
           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(10 * Keys.BACKSPACE)
           search1.send_keys(data.login().search_2)
           leave = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().leave)))
           if leave.is_displayed():
               print("leave is displayed!!")
           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(10 * Keys.BACKSPACE)
           search1.send_keys(data.login().search_3)
           leave = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().leave)))
           if leave.is_displayed():
               print("LEAVE is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(10 * Keys.BACKSPACE)
           search1.send_keys(data.login().search3)
           time = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().time)))
           if time.is_displayed():
               print("time is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(10 * Keys.BACKSPACE)
           search1.send_keys(data.login().search_4)
           time = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().time)))
           if time.is_displayed():
               print("TIME is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys(data.login().search4)
           recruitment = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().recruitment)))
           if recruitment.is_displayed():
               print("recruitment is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(30 * Keys.BACKSPACE)
           search1.send_keys(data.login().search_5)
           recruitment = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().recruitment)))
           if recruitment.is_displayed():
               print("RECRUITMENT is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(30 * Keys.BACKSPACE)
           search1.send_keys(data.login().search5)
           my_info = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().myinfo)))
           if my_info.is_displayed():
               print("my info is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(10 * Keys.BACKSPACE)
           search1.send_keys(data.login().search_6)
           my_info = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().myinfo)))
           if my_info.is_displayed():
               print("MY INFO is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys(data.login().search6)
           performance = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().performance)))
           if performance.is_displayed():
               print("performance is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys(data.login().search7)
           performance = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().performance)))
           if performance.is_displayed():
               print("PERFORMANCE is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys(data.login().search7)
           dashboard = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().dashboard)))
           if dashboard.is_displayed():
               print("dashboard is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys(data.login().search_8)
           dashboard = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().dashboard)))
           if dashboard.is_displayed():
               print("DASHBOARD is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys(data.login().search8)
           directory = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().directory)))
           if directory.is_displayed():
               print("directory is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys(data.login().search_9)
           directory = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().directory)))
           if directory.is_displayed():
               print("DIRECTORY is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys(data.login().search9)
           maintenance = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().maintenance)))
           if maintenance.is_displayed():
               print("maintenance is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys(data.login().search_10)
           maintenance = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().maintenance)))
           if maintenance.is_displayed():
               print("MAINTENANCE is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(15 * Keys.BACKSPACE)
           search1.send_keys(data.login().search10)
           claim = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().claim)))
           if claim.is_displayed():
               print("claim is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(15 * Keys.BACKSPACE)
           search1.send_keys(data.login().search_11)
           claim = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().claim)))
           if claim.is_displayed():
               print("CLAIM is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(15 * Keys.BACKSPACE)
           search1.send_keys(data.login().search11)
           buzz = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().buzz)))
           if buzz.is_displayed():
               print("buzz is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_page().search)))
           search1.send_keys(15 * Keys.BACKSPACE)
           search1.send_keys(data.login().search12)
           buzz = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, locators.login_page().buzz)))
           if buzz.is_displayed():
               print("BUZZ is displayed!!")

           print(" All the main menu options are displayed")
       except TimeoutException as e:
              print(e)