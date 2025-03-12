from django.http import JsonResponse
from rest_framework.views import APIView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BruteForceScannerAPIView(APIView):
    def get(self, request, *args, **kwargs):
        url = "https://practicetestautomation.com/practice-test-login/"

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # Keep browser open
        driver = webdriver.Chrome(options=options)

        # Open the login page
        driver.get(url)

        print("➡️ Enter username and password manually in the browser and click Login.")

        for attempt in range(1, 6):  # Allow 5 attempts
            print(f"🔄 Attempt {attempt}: Waiting for user to log in...")

            # Wait dynamically for user to press login (no fixed sleep time)
            while True:
                current_url = driver.current_url

                # If login success (URL changes or logout button appears)
                try:
                    success_message = driver.find_element(By.TAG_NAME, "h1").text
                    if "Congratulations" in success_message or "Logged In Successfully" in success_message:
                        print(f"✅ Login successful on attempt {attempt}!")
                        return JsonResponse({"status": "Login Successful"}, status=200)
                except:
                    pass

                # If error message appears (Login failed)
                try:
                    error_message = driver.find_element(By.ID, "error").text
                    if "invalid" in error_message.lower():
                        print(f"❌ Login failed. Reloading for attempt {attempt + 1}/5...")
                        driver.get(url)  # Reload page
                        break  # Move to next attempt
                except:
                    pass

        print("❌ Login failed after 5 attempts.")
        return JsonResponse({"status": "Login Failed"}, status=401)
