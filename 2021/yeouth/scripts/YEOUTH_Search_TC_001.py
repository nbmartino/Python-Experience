import pathlib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection,get_current_ip

from convert_server_name_linux import convert

PATH = '/usr/bin/chromedriver'

def scrape(server_name:str):
    # optional, use this on Linux and if you are not logged in when using nordvpn command


    settings = initialize_vpn(server_name)  # starts nordvpn and stuff
    opsys = settings['platform']
    print(f'opsys: {opsys}')
    if opsys == 'Windows':
        settings['command'][2] = '-n'  # change -g to -n, server name instead of group or country
    elif opsys == 'Linux':
        server_name = convert(server_name)
        settings["server_to_connect_to"] = server_name
    command = settings['command']
    server_to_connect_to = settings["server_to_connect_to"]
    cwd_path = settings.get('cwd_path')  # windows specifc

    print(f'opsys={opsys} \ncommand={command} \nserver_to_connect_to={server_to_connect_to} \ncwd_path={cwd_path}')

    rotate_VPN(settings)  # actually connect to server

    
    new_ip = get_current_ip()
    
    print("new_ip: " + new_ip)
    # YOUR STUFF

    # declare variable to store the URL to be visited
    base_url="http://yeouth.com"
    # declare variable to store search term
    search_term=server_name#"YEOUTH Natural Anti Aging Skin Care"
    #-- Pre-Condition--
    # # declare and initialize driver variable
    #driver=webdriver.Chrome(executable_path="C:/Users/WIN10/Documents/Yeouth/NordVPN/amazon/drivers/chromedriver.exe")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options,executable_path = PATH)

    # browser should be loaded in maximized window
    #driver.maximize_window()
    # driver should wait implicitly for a given duration, for the element under consideration to load.
    # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
    driver.implicitly_wait(3) #10 is in seconds
    # to load a given URL in browser window
    driver.get(base_url)
    # test whether correct URL/ Web Site has been loaded or not
    assert "YEOUTH" in driver.title
    #-- Steps--

    # close pop up dialog

    closeFormBtn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//button[@alt="Close form"]'))
            )

    #closeFormBtn = driver.find_element_by_css_selector('[alt="Close form"]')
    #closeFormBtn = driver.find_element_by_xpath('//button[@alt="Close form"]')

    closeFormBtn.click()

    # to enter search term, we need to locate the search textbox
    searchTextBox=driver.find_element_by_class_name("search_box")
    # to clear any text in the search textbox
    searchTextBox.clear()
    # to enter the search term in the search textbox via send_keys() function
    searchTextBox.send_keys(search_term)
    # to search for the entered search term
    searchTextBox.send_keys(Keys.RETURN)
    # to verify if the search results page loaded
    print(f"{search_term} - YEOUTH")
    assert f"{search_term} - YEOUTH" in driver.title
    # to verify if the search results page contains any results or no results were found.
    assert "No results found." not in driver.page_source
    #-- Post-Condition--

    driver.implicitly_wait(3) #3 is in seconds

    # to close the browser
    driver.close()

    close_vpn_connection(settings)

HERE = pathlib.Path(__file__).parent
server_names_list = [x.lower().strip() for x in open(HERE / "servers" / "names_list.txt", 'r').readlines()]

scrape('argentina #33')
#for name in server_names_list:
#ls
# scrape(name)
#for i in range(16,len(server_names_list)):
#       scrape(server_names_list[i])
#for i in range(3):
#       scrape(server_names_list[i])