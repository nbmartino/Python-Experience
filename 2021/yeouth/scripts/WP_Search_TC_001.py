from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection,get_current_ip


# optional, use this on Linux and if you are not logged in when using nordvpn command

settings = initialize_vpn("Australia")  # starts nordvpn and stuff
opsys = settings['platform']
command = settings['command']
server_to_connect_to = settings["server_to_connect_to"]
cwd_path = settings.get('cwd_path')  # windows specifc

print('opsys={opsys} \ncommand={command} \nserver_to_connect_to{server_to_connect_to} \ncwd_path={cwd_path}')

rotate_VPN(settings)  # actually connect to server

new_ip = get_current_ip()
print("new_ip: " + new_ip)
# YOUR STUFF

# declare variable to store the URL to be visited
base_url="https://nbmartino.wordpress.com/"
# declare variable to store search term
search_term="Moisture"#"YEOUTH Natural Anti Aging Skin Care"
#-- Pre-Condition--
# # declare and initialize driver variable
driver=webdriver.Chrome(executable_path="C:/Users/WIN10/Documents/Yeouth/NordVPN/amazon/drivers/chromedriver.exe")
# browser should be loaded in maximized window
driver.maximize_window()
# driver should wait implicitly for a given duration, for the element under consideration to load.
# to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
driver.implicitly_wait(10) #10 is in seconds
# to load a given URL in browser window
driver.get(base_url)
# test whether correct URL/ Web Site has been loaded or not
assert "YEOUTH" in driver.title
#-- Steps--

# close pop up dialog

closeFormBtn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[text()="Contact"]'))
        )

#closeFormBtn = driver.find_element_by_css_selector('[alt="Close form"]')
#closeFormBtn = driver.find_element_by_xpath('//button[@alt="Close form"]')

closeFormBtn.click()

driver.close()

close_vpn_connection(settings)