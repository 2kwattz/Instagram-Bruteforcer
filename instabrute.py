import pyfiglet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

banner = pyfiglet.figlet_format("Instagram Bruteforcer")
print(banner)
print("For Educational Purpose Only. Author : Roshan Bhatia IG @2kwattz\n")
time.sleep(1)
print("Please enter account's username")
username = input()

def startBruteforce(driver):
    try:
        driver.get(f"https://www.instagram.com/accounts/login/")
        time.sleep(3)

        loginpage_source = driver.page_source
        soup = BeautifulSoup(loginpage_source, 'html.parser')
# For Testing Purpose
        with open('soup_content.txt', 'w', encoding='utf-8') as file:
            file.write(str(soup))
            print("Content saved to 'soup_content.txt' successfully.")
    
        loginForm = soup.find(id='loginForm')
        if loginForm:
            time.sleep(4)
        wordlist_option = int(input("Enter 1 for custom wordlist. 2 for default wordlist\n"))
        if wordlist_option == 1:
            wordlistPath = input("Enter path to the wordlist")
            print("Under Development")
        elif wordlist_option == 2:
            print("Under Development")
        # Proceed with further processing
    except:
        time.sleep(4)
        print("No form found on the webpage.")

def beginAttack():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)  # Assuming you have Chrome WebDriver installed.

    # Setting up user agent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")


    driver.get(f"https://www.instagram.com/{username}")

    if "Sorry, this page isn't available." in driver.page_source:
        status_code = 404
        print(f"\033[91mHTTP Request Failed. Status : {status_code} USER NOT FOUND!\n \033[0m")
        print(f"The Instagram account '{username}' does not exist.") 
    else:
        status_code = 200
        print(f"\033[92mHTTP Request Successful. Status : {status_code} OK! USER LOCKED (GIMME TONE) \033[0m")
        print(f"Instagram account '{username}' found")
        startBruteforce(driver)
    
    driver.quit()

beginAttack()
