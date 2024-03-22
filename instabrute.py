import pyfiglet
import requests
import time
from bs4 import BeautifulSoup

banner = pyfiglet.figlet_format("Instagram Bruteforcer")
print(banner)
print("For Educational Purpose Only. Author : Roshan Bhatia IG @2kwattz\n")
time.sleep(2)
print("Please enter account's username")
username = input()

accountData = {
    'username': username,
    'source': f"https://www.instagram.com/{username}"
}


def beginAttack():

    # Login Page URL
    loginPage = 'https://www.instagram.com/accounts/login/'

    # Sending HTTPS Request
    response = requests.get(loginPage)

    # Confirming Response Code
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(
            f"\033[92mHTTP Request Successful. Status : {response.status_code} OK! \033[0m")
        loginForm = soup.find('form')

        if loginForm:
            # Extracting Action Attribute
            formAction = loginForm.get('action')

            # Extract input fields and their names
            inputFields = loginForm.find_all('input')

            # Proceed with further processing
        else:
            print("No form found on the webpage.")
            # Extracting  Action Attribute

    else:
        print("Failed to fetch data")


beginAttack()
