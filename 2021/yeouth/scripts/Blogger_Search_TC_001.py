""" import os
import platform
import random
import re
import shutil
import subprocess
import time
from os import path
 """

import os

import pathlib
import requests
import urllib.request
from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection,get_current_ip

from convert_server_name_linux import convert

def scrape(server_name:str):
        # optional, use this on Linux and if you are not logged in when using nordvpn command
        os.system('nordvpn disconnect')
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
        server_name = quote(server_name.encode('utf8'))
        # declare variable to store the URL to be visited
        base_url=f"https://treeoflife2021.blogspot.com/search?q={server_name}" #"https://nbmartino.wordpress.com/"
        # declare variable to store search term
        #search_term="Moisture"#"YEOUTH Natural Anti Aging Skin Care"
        #-- Pre-Condition--
        # # declare and initialize driver variable
        #options = webdriver.ChromeOptions()
        #options.add_argument('--lang=hi')
        caps = DesiredCapabilities.CHROME
        caps["pageLoadStrategy"] = "normal"



        #PATH = "C:/Users/WIN10/Documents/Yeouth/NordVPN/amazon/drivers/chromedriver.exe"
        PATH = '/usr/bin/chromedriver'
        #driver=webdriver.Chrome(executable_path=PATH)
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

        driver=webdriver.Chrome(options=options,executable_path=PATH,desired_capabilities=caps)
        # browser should be loaded in maximized window
        driver.maximize_window()
        # driver should wait implicitly for a given duration, for the element under consideration to load.
        # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
        #driver.implicitly_wait(3) #10 is in seconds
        # to load a given URL in browser window
        driver.get(base_url)
        # test whether correct URL/ Web Site has been loaded or not
       
        #-- Steps--
        try:
                element_present = EC.presence_of_element_located((By.ID, 'Header1')) 
                WebDriverWait(driver, 2).until(element_present)
        except TimeoutException:
                print("Timed out waiting for page to load")

        assert "Tree of Life" in driver.title


        
        #driver.implicitly_wait(3) #5 is in seconds

        driver.close()

        close_vpn_connection(settings)

""" 
        closeFormBtn = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//a[text()="Contact"]'))
                )

        #closeFormBtn = driver.find_element_by_css_selector('[alt="Close form"]')
        #closeFormBtn = driver.find_element_by_xpath('//button[@alt="Close form"]')

        closeFormBtn.click()
 """




HERE = pathlib.Path(__file__).parent
#server_names_list = [x.lower().strip() for x in open(HERE / "servers" / "names_list.txt", 'r').readlines()]
server_names_list = [x.lower().strip() for x in open(HERE / "servers" / "server_names_formatted_list_by_20s.txt", 'r').readlines()]

#for name in server_names_list:
#        scrape(name)

#scrape('Brazil #66')



for name in server_names_list:
        try:
                print(name)
                scrape(name)
        except:
                print(f'an error occured while connectng to - {name}!')

'''
total = len(server_names_list)
for i in range(832,total):
        name = server_names_list[i]
        try:
                scrape(name)
        except:
                print(f'an error occured while connectng to - {name}!')
                pass
                  '''
# last 3
#total = len(server_names_list)
#for i in range(4,total):
#    scrape(server_names_list[i])
#for i in range(3):
#        scrape(server_names_list[i])

#for i in range(3):
#        scrape("South Africa #100")
os.system('nordvpn disconnect')