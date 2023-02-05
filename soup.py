from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import StaleElementReferenceException
import traceback

# Start the WebDriver and load the page
driver = webdriver.Firefox()
driver.get("https://nclottery.com/cash5-past-draws")

# Select the "Month" dropdown
month_dropdown = Select(driver.find_element("id", "ctl00_MainContent_ddlMonth"))

# Select the "Year" dropdown
year_dropdown = Select(driver.find_element("id", "ctl00_MainContent_ddlYear"))

# Find the "Submit" button
submit_button = driver.find_element("id", "ctl00_MainContent_btnSearch")

years = [year for year in range(2007, 2024)]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(years)

for month in months:

    for year in years:

        try:

            # Select the "Month" dropdown
            month_dropdown = Select(driver.find_element("id", "ctl00_MainContent_ddlMonth"))

            # Select the "Year" dropdown
            year_dropdown = Select(driver.find_element("id", "ctl00_MainContent_ddlYear"))

            # Find the "Submit" button
            submit_button = driver.find_element("id", "ctl00_MainContent_btnSearch")

            month_dropdown.select_by_value(str(month))
            year_dropdown.select_by_value(str(year))

        except Exception as err:
            print(traceback.format_exc())

        try:
            submit_button = driver.find_element('id', "ctl00_MainContent_btnSearch")
            submit_button.click()
        except StaleElementReferenceException as err:
            print(err)

            submit_button = driver.find_element('id', "ctl00_MainContent_btnSearch")
            submit_button.click()

        time.sleep(5)
        with open(f"C:\\Users\\jer43\\OneDrive\\Desktop\\cash_5\\{month}_{year}.html", "w") as file:
            file.write(driver.page_source)

# Quit the WebDriver
driver.quit()