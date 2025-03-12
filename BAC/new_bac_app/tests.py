# import requests
#
# url = "https://practicetestautomation.com/practice-test-login/"
# data = {
#     "username": "student",
#     "password": "Password123"
# }
#
# response = requests.post(url, data=data)
#
# print("Response Status Code:", response.status_code)
# print("Response Length:", len(response.text))
# print("Response Headers:", response.headers)
# print("Response Text Preview:", response.text[:500])  # Print first 500 characters

from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the login page
driver.get("https://practicetestautomation.com/practice-test-login/")


# Get page source
print(driver.page_source[:500])

# Close browser
driver.quit()
