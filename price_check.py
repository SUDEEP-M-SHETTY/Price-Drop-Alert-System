import os
import time
import subprocess
import requests
from bs4 import BeautifulSoup
from plyer import notification
from sys import platform

def notify_linux(message):
    """Function to display notifications on Linux."""
    subprocess.Popen(['notify-send', message])

def notify_mac(title, text):
    """Function to display notifications on macOS."""
    os.system('osascript -e \'display notification "{}" with title "{}"\''.format(text, title))

def notify_windows(title, message):
    """Function to display notifications on Windows."""
    notification.notify(title=title, message=message, app_icon=None, timeout=10)

def price_check(url, min_price):
    """Function to check price drop below a certain amount after every 1800 secs.
    Enter the complete URL followed by an integer valued price,
    below which the user will be notified.
    """
    try:
        res = requests.get(url, timeout=5)
        content = BeautifulSoup(res.content, "html.parser")
        price_div = content.find('div', attrs={"class": "Nx9bqj CxhGGd"}).text
        price = int((price_div.replace(",", ""))[1:])
        if price <= min_price:
            if platform == "darwin":
                notify_mac(TITLE, MESSAGE)
            elif platform == "linux" or platform == "linux2":
                notify_linux(MESSAGE)
            elif platform == "win32":
                notify_windows(TITLE, MESSAGE)
            exit()  # Exit the script after notification
        else:
            print("Price still not below minimum price. Checking again after 30 mins")
            time.sleep(1800)
            price_check(url, min_price)
    except Exception as e:
        print(f"Error: {e}")
        print("Retrying...")
        time.sleep(1800)
        price_check(url, min_price)

if __name__ == "__main__":
    URL = input("Enter the complete link for the product to be monitored:\n")
    MIN_PRICE = int(input("Enter the minimum price to get notified for price drop:\n"))
    MESSAGE = "Price has dropped below the minimum price."
    TITLE = "Price Drop Alert"

    price_check(URL, MIN_PRICE)
