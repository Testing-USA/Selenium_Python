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
    default_Clicked_Rd = driver.find_element(By.ID, "product_550")
    print("By default radio button is clicked: " , default_Clicked_Rd.is_enabled())
    Hotel_Booking = driver.find_element(By.ID, "product_551")
    Hotel_Booking.click()
    First_Name = driver.find_element(By.XPATH, '//input[@id="travname"]')
    First_Name.send_keys("Testing")
    Last_Name = driver.find_element(By.CSS_SELECTOR, "[placeholder='last name as on passport']")
    Last_Name.send_keys("Selenium")
    Order_Notes = driver.find_element(By.ID, "order_comments")
    Order_Notes.send_keys("We are doing selenium testing")

    dob = driver.find_element(By.ID, "dob")
    dob.click()
    month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
    month.click()
    select_month = Select(month)
    select_month.select_by_visible_text("Nov")
    year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
    year.click()
    select_year = Select(year)
    select_year.select_by_visible_text("2001")
    date = driver.find_element(By.CSS_SELECTOR, '[data-date="22"]')
    date.click()

    Male_rd = driver.find_element(By.ID, "sex_1")
    Female_rd = driver.find_element(By.ID, "sex_2")
    #by default both radio buttons are not selected
    print("Male is not selected: ", not Male_rd.is_selected())
    print("Female is not selected: ", not Female_rd.is_selected())

    Male_rd.click()
    print("Male is selected: ", Male_rd.is_enabled())
    #by default Add more passengers checkbox is not selected
    add_passengers = driver.find_element(By.ID, "addmorepax")
    print("Add more passengers checkbox is not selected: ", not add_passengers.is_selected())
    add_passengers.click()
    print("Add more passengers checkbox is selected: ",add_passengers.is_selected())
    add_passengers_dropdown = driver.find_element(By.ID, "select2-addpaxno-container")
    add_passengers_dropdown.click()
    One_Pass = driver.find_element(By.XPATH, '//li[contains(text(), "add 1 more passenger (100%)")]')
    One_Pass.click()

    sec_pas_Fname = driver.find_element(By.ID, "travname2")
    sec_pas_Fname.send_keys("Pyhton")
    sec_pas_Lname = driver.find_element(By.ID, "travname2")
    sec_pas_Lname.send_keys("Lan")
    
    dob2 = driver.find_element(By.ID, "dob2")
    dob2.click()
    month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
    month.click()
    select_month = Select(month)
    select_month.select_by_visible_text("Sep")
    year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
    year.click()
    select_year = Select(year)
    select_year.select_by_visible_text("2021")
    date = driver.find_element(By.CSS_SELECTOR, '[data-date="20"]')
    date.click()


    Male_rd2 = driver.find_element(By.ID, "sex2_1")
    Female_rd2 = driver.find_element(By.ID, "sex2_2")
    #by default both radio buttons are not selected
    print("Male is not selected: ", not Male_rd2.is_selected())
    print("Female is not selected: ", not Female_rd2.is_selected())
    Female_rd2.click()
    print("Male is selected: ", Female_rd2.is_enabled())

    Passenger_Type = driver.find_element(By.ID, "select2-paxtype2-container")
    Passenger_Type.click()
    pass_type = driver.find_element(By.XPATH, '//li[text()="Child"]')
    pass_type.click()

    trip_type1 = driver.find_element(By.ID, "traveltype_1")
    trip_type2= driver.find_element(By.ID, "traveltype_2")
    print("one way trip radio button is selected", trip_type1.is_selected())
    print("two way trip radio button is not selected", not trip_type2.is_selected())

    from_city = driver.find_element(By.ID, "fromcity")
    from_city.send_keys("Lhr")
    from_city = driver.find_element(By.ID, "tocity")
    from_city.send_keys("Isl")

    Dep_date = driver.find_element(By.ID, "departon")
    Dep_date.click()
    month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
    month.click()
    select_month = Select(month)
    select_month.select_by_visible_text("Sep")
    year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
    year.click()
    select_year = Select(year)
    select_year.select_by_visible_text("2023")
    date = driver.find_element(By.CSS_SELECTOR, '[data-date="27"]')
    date.click()
    add_info = driver.find_element(By.ID, "notes")
    add_info.send_keys("Child is infant")

    purpose_selected_close = driver.find_element(By.XPATH, '(//span[@class="select2-selection__clear"])[3]')
    purpose_selected_close.click()
    purpose = driver.find_element(By.XPATH, '//li[text()="Prank a friend"]')
    purpose.click()
    DD_method = driver.find_element(By.ID, "deliverymethod_3")
    DD_method.click()

    phone = driver.find_element(By.ID, "billing_phone")
    phone.send_keys("+1 12345")
    email = driver.find_element(By.ID, "billing_email")
    email.send_keys("testing@gmail.com")
    country_dropdown = driver.find_element(By.ID, "select2-billing_country-container")
    country_dropdown.click()
    select_country = driver.find_element(By.XPATH, '//li[text()="United States (US)"]')
    select_country.click()
    House_detail = driver.find_element(By.ID, "billing_address_1")
    House_detail.send_keys("St # 102")
    Appartment = driver.find_element(By.ID, "billing_address_2")
    Appartment.send_keys("Appartment # 302")
    city = driver.find_element(By.ID, "billing_city")
    city.send_keys("Testing1122")
    state_dropdown = driver.find_element(By.ID, "select2-billing_state-container")
    state_dropdown.click()
    select_state = driver.find_element(By.XPATH, '//li[text()="California"]')
    select_state.click()
    postal_code = driver.find_element(By.ID, "billing_postcode")
    postal_code.send_keys("90080")
    proceed_pay = driver.find_element(By.ID, "place_order")
    proceed_pay.click()
    paypal = driver.find_element(By.CLASS_NAME, "logo")
    if paypal.is_displayed():
        print("PayPal logo is visible")
    else:
        print("PayPal logo is not visible")