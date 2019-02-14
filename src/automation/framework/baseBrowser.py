from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from automation.framework import Constant
import os, os.path
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\Sanelib Solutions\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})

driver = webdriver.Chrome(Constant.ChromeDriverPath)
#driver = webdriver.PhantomJS(Constant.PhantomDriverPath)

URL=""
USERNAME=""
PASSWORD=""
DCITY=""
ACITY=""
USER_DISPLAY_NAME=""

def loadbrowser():
    loadConfiguration()
    print("Load Browser")
    driver.maximize_window()
    driver.get(URL)
    driver.set_page_load_timeout(20)

def loadConfiguration():
    global URL
    global USERNAME
    global PASSWORD
    global DCITY
    global ACITY
    global USER_DISPLAY_NAME
    global DDate
    global ADate

    #with open(os.path.join(os.getcwd(),'automation',"configure.txt"))as file:
    with open(Constant.ConfigurationFile) as file:
        print(file.name)
        for line in file.readlines():
            configuration = line.split("=")
            if configuration[0] == Constant.Browser:
                  print("Load browser - Chrome" )
            elif configuration[0]==Constant.Url:
                URL = configuration[1].rstrip()
                print("Current URL -" ,URL)
            elif configuration[0]==Constant.Username:
                USERNAME=configuration[1].rstrip()
                print("Username -" , USERNAME)
            elif configuration[0]==Constant.Password:
                PASSWORD = configuration[1].rstrip()
                print("Password -",PASSWORD)
            elif configuration[0] == Constant.UserDisaplyName:
                USER_DISPLAY_NAME = configuration[1].rstrip()
                print("USER_DISPLAY_NAME -", USER_DISPLAY_NAME)
            elif configuration[0]==Constant.DCITY:
                DCITY=configuration[1].rstrip()
                print("Departure Airport - ", DCITY)
            elif configuration[0]==Constant.ACITY:
                ACITY=configuration[1].rstrip()
                print("Arrival Airport - ", ACITY)
            elif configuration[0]==Constant.DepartureDate:
                DDate=configuration[1].rstrip()
                print("Departure Date - ", DDate)
            elif configuration[0]==Constant.ArrivalDate:
                ADate=configuration[1].rstrip()
                print("Arrival Date - ", ADate)

def closebrowser():
    driver.quit()

def expectedResult():
    print("============================")
    print("Expected Result")
    print("============================")