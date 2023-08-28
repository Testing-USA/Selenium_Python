import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_Date():
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=ops)
    driver.implicitly_wait(3)
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    dob_calender = driver.find_element(By.ID, "dob")
    dob_calender.click()
    month_dropdown = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
    month_dropdown.click()
    select_month = Select(month_dropdown)
    select_month.select_by_visible_text("Sep")
    year_dropdown = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
    year_dropdown.click()
    select_year = Select(year_dropdown)
    select_year.select_by_visible_text("2001")
    select_date = driver.find_element(By.XPATH, '//a[@data-date="17"]')
    select_date.click()