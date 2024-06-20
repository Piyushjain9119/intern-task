# Python Developer Internship - Web Scraping Task

## Project Description

### Title
Python Developer Internship Web Scraping Task

### Overview
This project involves a Python script designed to perform web scraping using the Selenium library. The primary objective of this task is to scrape data from the TINXSYS website ([TINXSYS](https://tinxsys.com/TinxsysInternetWeb/searchByTin_Inter.jsp)) by entering a TPIN and manually solving a CAPTCHA.

### Task Details
The main steps in this task are:
1. Navigate to the TINXSYS landing page.
2. Input the TPIN.
3. Manually solve the CAPTCHA to maintain the site's integrity.
4. Automate the rest of the data extraction process using the Python script.
5. Present the extracted data in a dictionary format.

   ![image](https://github.com/Piyushjain9119/intern-task/assets/128716173/875edba0-4235-4dcd-ba57-99ae70145a3b)


### Key Features
- **Web Scraping with Selenium:** Utilizes Selenium to automate interactions with the web page and extract data.
- **Manual CAPTCHA Entry:** Ensures the CAPTCHA is entered manually by the user to comply with site integrity requirements.
- **Automated Data Extraction:** Automatically collects the required information after the CAPTCHA is successfully entered.
- **Formatted Output:** Displays the scraped data in a dictionary format for easy readability and further processing.

# OUTPUT OF THE PYTHON SCRIPT 
  
  ![image](https://github.com/Piyushjain9119/intern-task/assets/128716173/9b780453-9bcc-4b20-a448-93923c688d16)


### Instructions
1. Ensure Python and Selenium are installed on your system.
2. Download and install the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome).
3. Open the Python script and update any placeholder values with your specific details.
4. Execute the Python script.
5. When prompted, manually enter the CAPTCHA displayed on the TINXSYS website.
6. The script will continue to scrape the necessary data and display it in a dictionary format.

   ![image](https://github.com/Piyushjain9119/intern-task/assets/128716173/31d995d6-6885-48a9-8ad9-95d16306efcc)


### Notes
- Verify that the WebDriver path is correctly set in the script.
- Replace placeholder values with actual values where necessary.
- CAPTCHA must be entered manually each time the script runs to ensure compliance with site policies.

  ![image](https://github.com/Piyushjain9119/intern-task/assets/128716173/453ceb14-8d88-4bb2-99e0-a574e653b132)
  if the user wants to enter the tpin manually then just uncommet the commented line and comment the above code line


This project aims to provide hands-on experience in web scraping using Selenium, while adhering to ethical guidelines by requiring manual CAPTCHA entry. The final output will be a structured dictionary containing the extracted data.
