from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pprint

# Set up the Selenium WebDriver (you might need to adjust the path to your driver)

def find_button(url):
    # Load the page
    try:
        driver = webdriver.Chrome()

        driver.get(url)

        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Define a regex pattern to match "submit" or "apply" in links
        link_pattern = re.compile(r'(submit|apply)', re.IGNORECASE)

        # Search for links that have an A or Button tag
        links = driver.find_elements(By.XPATH, '//*[name()="a" or name()="button"]')

        # Filter the links to only those that match the pattern
        for link in links:
            if link_pattern.search(link.text):
                return link

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

# def find_button(link, driver):
#     for i in range(0, 3):
#         if link.tag_name == 'a' or link.tag_name == 'button':
#             return link
#         else:
#             link = driver.find_element(By.XPATH, f'//{link.tag_name}[text()="{link.text}"]/..')

