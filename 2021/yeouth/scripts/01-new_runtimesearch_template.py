
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys

from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection, get_current_ip
from convert_server_name_linux import convert
from pick_server_from_country_linux import pick_a_server
PATH = "/var/www/html/chromedriver"
# PATH="C:\Program Files (x86)\chromedriver.exe"
# PATH = "C:/Users/WIN10/Documents/Yeouth/NordVPN/amazon/drivers/chromedriver.exe"


def searchScipt(country: str):

    try:

        settings = initialize_vpn(country)  # starts nordvpn and stuff
        opsys = settings['platform']

        if opsys == 'Windows':
           # change -g to -n, server name instead of group or country
           settings['command'][2] = '-n'
           cwd_path = settings.get('cwd_path')  # windows specific
        elif opsys == 'Linux':
           server_name = pick_a_server(country)  # convert(server_name)
           settings["server_to_connect_to"] = server_name

        rotate_VPN(settings)  # actually connect to server
        http = 'http://'
        domain = sys.argv[1]
        item = sys.argv[2]
        # domain = "treeoflife2021.blogspot.com"
        # item = "Test namin"
        caps = DesiredCapabilities.CHROME
        caps["pageLoadStrategy"] = "normal"
        option = webdriver.ChromeOptions()
        option.add_argument("window-size=1500,1200")
        option.add_argument("--headless")
        option.add_argument("--disable-gpu")
        option.add_argument("--no-sandbox")
        option.add_argument("--allow-insecure-localhost")
        option.add_argument("--log-level=3")
        driver = webdriver.Chrome(
        options=option, executable_path=PATH, desired_capabilities=caps)

        print("Opening Browser...")
        print("Navigate to " + domain)
        driver.get(http+domain)

        print("Searching for " + item)
        if driver.find_element_by_name("q"):
            search = driver.find_element_by_name("q")
            search.send_keys(item)
            search.send_keys(Keys.RETURN)

        elif driver.find_element_by_name("a"):
            search = driver.find_element_by_name("a")
            search.send_keys(item)
            search.send_keys(Keys.RETURN)

        elif driver.find_element_by_name("s"):
            search = driver.find_element_by_name("s")
            search.send_keys(item)
            search.send_keys(Keys.RETURN)

        elif driver.find_element_by_name("keyword"):
            search = driver.find_element_by_name("keyword")
            search.send_keys(item)
            search.send_keys(Keys.RETURN)

        try:
            main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "quote"))
            )

            print(main.text)
            print("Search done!")
            print("Next Run after " + sys.argv[4] + " seconds")
            print("Closing Browser...")
            driver.quit()
            close_vpn_connection(settings)
        except:

            print("Sorry, no products matched the keyword")
            print("Search done!")
            print("Closing Browser...")
            driver.quit()
            close_vpn_connection(settings)


    except Exception as Argument:
        f = open("pythonlog.txt","w")
        f.write(str(Argument))
        f.close()
        close_vpn_connection(settings)


#searchScipt(sys.argv[3])
searchScipt("Australia #520")
