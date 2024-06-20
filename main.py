from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
import requests


browser = webdriver.Chrome()
browser.get("https://tinxsys.com/TinxsysInternetWeb/searchByTin_Inter.jsp")


tin_number = browser.find_element(By.ID, "tinNumberId")
tin_number.send_keys('09137500718')
# tin_numberI = input("enter the tin number")



captcha_id = browser.find_element(By.ID, "captchaText")
captcha = input("provide the captcha")

captcha_id.send_keys(captcha)



search_button = browser.find_element(By.CLASS_NAME, "button")

search_button.click()

browser.get(f"https://tinxsys.com/TinxsysInternetWeb/dealerControllerServlet?tinNumber=09137500718&answer={captcha}&searchBy=TIN&backPage=searchByTin_Inter.jsp")


tin_number1 = browser.find_element(By.CLASS_NAME, "tdWhite")
tbody_elements = browser.find_elements(By.TAG_NAME,"tbody")
tbody_main = tbody_elements[2]

tr_elements = tbody_main.find_elements(By.TAG_NAME,"tr")

info = []
for tr in tr_elements:
        # Find all td elements with class 'tdWhite' inside the tr
        td_elements = tr.find_elements(By.CSS_SELECTOR,"td.tdWhite")
        
        # Loop through each td element with class 'tdWhite'
        for td in td_elements:
            # Extract text from td element
            td_text = td.text
            info.append(td_text)
            
name = ['tin_number','cst_number','dealer_name','dealer_address','state_name','pan_number','registration_date','valid_upto','registration_status']


original_data = dict(zip(name,info))
print(original_data)