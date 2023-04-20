
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection, get_current_ip

from convert_server_name_linux import convert
from pick_server_from_country_linux import pick_a_server

PATH = "/usr/bin/chromedriver"
# "C:\Program Files (x86)\chromedriver.exe"
#PATH = "C:/Users/WIN10/Documents/Yeouth/NordVPN/amazon/drivers/chromedriver.exe"


def searchScipt(country: str):

    settings = initialize_vpn(country)  # starts nordvpn and stuff
    opsys = settings['platform']

    if opsys == 'Windows':
        settings['command'][2] = '-n'  # change -g to -n, server name instead of group or country
        cwd_path = settings.get('cwd_path')  # windows specific
    elif opsys == 'Linux':
        server_name =  pick_a_server(country)#convert(server_name)
        settings["server_to_connect_to"] = server_name

    rotate_VPN(settings)  # actually connect to server


    try:
        #x = datetime.datetime.now()  
        #currentday = x.strftime("%A")
        #days = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday"]
        #for getDay in days:                                       
        #proxies = {
                #"http": "http://api.scraperapi.com/?api_key=c2a88c3b4ad351750d2fe7fd3b24cf6e&country_code=uk",
                #"https": "http://api.scraperapi.com/?api_key=c2a88c3b4ad351750d2fe7fd3b24cf6e&country_code=uk"
            #}

    
        
            #limit = int(sys.argv[3])
        # interval = int(sys.argv[4])
            #country = sys.argv[3]
            #ip = "172.69.35.97:14018"
            #http = 'http://'
            http = 'https://'
            #domain = 'yeouth.com'#sys.argv[1]
            domain = 'treeoflife2021.blogspot.com/search?q=abc'
            item =  'acid'#sys.argv[2]
            
            #PATH="C:\Program Files (x86)\chromedriver.exe"
            PATH = "/usr/bin/chromedriver"
            #country = sys.argv[4]
            #interval =  sys.argv[4]
            #spliter = item.split(",")
            #print("Searching IP Address for "+ country +"...")
                    #print("IP Adress: " + getProxy(country))
                    #print("IP Address: " + r.text)
            caps = DesiredCapabilities.CHROME
            caps["pageLoadStrategy"] = "normal"
            #options = webdriver.ChromeOptions()
            myProxy = "10.0.x.x:yyyy"
            options = webdriver.ChromeOptions()
            options.add_argument('--proxy-server=%s' % myProxy)
            options.add_argument("window-size=1500,1200")
            #options.add_argument("--headless")
            #print(arrItem)
            #option.add_argument("--proxy-server=%s" % proxies )
            #option.add_argument("--headless")
            '''
            option.add_argument("--disable-gpu")
            option.add_argument("--no-sandbox")
            option.add_argument("--allow-insecure-localhost")
            option.add_argument("--log-level=3")
            '''
            #options.add_argument("--headless")
            #options.headless = True
            #options.add_argument("--no-sandbox")
            #options.add_argument("start-maximized")
            #options.add_argument("disable-infobars")
            #options.add_argument("--disable-extensions")

    #option.headless = True
            #option.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"')
                #option.add_argument("C:\\Users\\Acer\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
            #from pyvirtualdisplay import Display
            #display = Display(visible=0, size=(1024, 768))
            #display.start()
            driver = webdriver.Chrome(options=options,executable_path=PATH,desired_capabilities=caps)
                #r = requests.get(http+domain, proxies=proxies, verify=False)
            print("Opening Browser...")
            print("Navigate to " + domain )
            #driver.get(http+domain)
            #driver.get(http+domain)
            driver.get(http+domain)
            driver.implicitly_wait(10)  # 10 is in seconds
            print("Searching for " + item)
            #search = driver.find_element_by_name("q")
            if driver.find_element_by_name("q"):
                search = driver.find_element_by_name("q")
                search.send_keys(item)
                search.send_keys(Keys.RETURN)
            # driver.get("http://api.scraperapi.com/?api_key=c2a88c3b4ad351750d2fe7fd3b24cf6e&&url="+http+domain+"/search?type=product&q="+item+"&country_code=uk")
            elif driver.find_element_by_name("a"):
                search = driver.find_element_by_name("a")
                search.send_keys(item)
                search.send_keys(Keys.RETURN)
            # driver.get("http://api.scraperapi.com/?api_key=c2a88c3b4ad351750d2fe7fd3b24cf6e&&url="+http+domain+"/search?type=product&a="+item+"&country_code=uk")
            elif driver.find_element_by_name("s"):
                search = driver.find_element_by_name("s")
                search.send_keys(item)
                search.send_keys(Keys.RETURN)
                #driver.get("http://api.scraperapi.com/?api_key=c2a88c3b4ad351750d2fe7fd3b24cf6e&&url="+http+domain+"/search?type=product&s="+item+"&country_code=uk")
            elif driver.find_element_by_name("keyword"):
                search = driver.find_element_by_name("keyword")
                search.send_keys(item)
                search.send_keys(Keys.RETURN)
                #driver.get("http://api.scraperapi.com/?api_key=c2a88c3b4ad351750d2fe7fd3b24cf6e&&url="+http+domain+"/search?type=product&keyword="+item+"&country_code=uk")
                #print(driver.current_url)
                #driver.get(http+domain+"/search?type=product&q="+item)
        
            try:
                main = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "quote"))
                )
    
                print(main.text)
                print("Search done!") 
                #print("Next Run after " + sys.argv[4] + " seconds")
                print("Closing Browser...")
                driver.quit()
                close_vpn_connection(settings)
            except:
                
                print("Sorry, no products matched the keyword")
                print("Search done!")
                    #print("Search item will be reflected on analytics")
                print("Closing Browser...")
                driver.quit()
                close_vpn_connection(settings)
                    #print(main.text)
                #print("IP blocked")
            #time.sleep(interval)
            
        
    except Exception as Argument:
        f = open("pythonlog.txt","w")
        f.write(str(Argument))
        f.close()
        close_vpn_connection(settings)

    #close_vpn_connection(settings)

searchScipt('Vietnam')
#searchScipt(sys.argv[3])