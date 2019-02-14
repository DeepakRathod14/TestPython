from automation.framework import baseScript
from automation.framework.baseBrowser import driver
from automation.framework import Constant

def loginUserName(loginusername):
    username = baseScript.display_element("XPATH", ".//*[@class='name ng-binding' and text()='{}']".format(loginusername))
    return username

def signOut():
    baseScript.click("XPATH", ".//div[starts-with(@class,'profile-block')]")
    baseScript.timeInterval(3)
    baseScript.click("XPATH",".//*[@id='logoutForm']/a[text()='{}']" .format(Constant.Banner_SignOut))

def verifyLogo():
    return baseScript.display_element("xpath","././/div[@class='logo']//img [@src='/Content/assets/img/site-logo.png']")

def verifyHeaderMenu():
    about = baseScript.display_element("xpath",".//ul[@class='nav-left']//a[normalize-space(.)='{}']".format(Constant.Home_About))
    list = baseScript.display_element("xpath",".//ul[@class='nav-left']//a[normalize-space(.)='{}']".format(Constant.Home_List))
    news = baseScript.display_element("xpath", ".//ul[@class='nav-left']//a[normalize-space(.)='{}']".format(Constant.Home_News))
    register=baseScript.display_element("xpath",".//ul[@class='nav-right']//a[normalize-space(.)='{}']".format(Constant.Home_Register))
    request = baseScript.display_element("xpath",".//ul[@class='nav-right']//a[normalize-space(.)='{}']".format(Constant.Home_RequestAnInvite))
    signIn = baseScript.display_element("xpath",".//ul[@class='nav-right']//a[normalize-space(.)='{}']".format(Constant.Banner_SignIn))
    if about and list and news and register and request and signIn:
        return True
    else:
        return False
def verifyHomepageContent():
    baseScript.timeInterval(2)
    heading = baseScript.display_element("xpath", ".//h1[text()='Welcome to VacationChamp']")
    flight = baseScript.display_element("xpath",".//*[contains(@id,'flight')]")
    baseScript.timeInterval(2)
    hotel =  baseScript.display_element("xpath",".//*[contains(@id,'hotel')]")
    baseScript.timeInterval(2)
    rent = baseScript.display_element("xpath",".//*[contains(@id,'rental')]")
    baseScript.timeInterval(2)
    car = baseScript.display_element("xpath",".//*[contains(@class,'car ')]")
    driver.execute_script("window.scrollBy(0,500);")
    title = baseScript.display_element("xpath", ".//*[@id='about']/h1")
    baseScript.timeInterval(2)
    first = baseScript.display_element("xpath", ".//*[@id='about']//h2[text()='{}']".format(Constant.Home_RightProductRightTime))
    baseScript.timeInterval(2)
    second =baseScript.display_element("xpath",".//*[@id='about']//h2[text()='{}']".format(Constant.Home_TheSearchIsOver))
    baseScript.timeInterval(2)
    driver.execute_script("window.scrollBy(0,500);")
    third =baseScript.display_element("xpath",".//*[@id='about']//h2[text()='{}']".format(Constant.Home_EveryAspectOfYourTripIsHere))
    baseScript.timeInterval(2)
    forth =baseScript.display_element("xpath",".//*[@id='about']//h2[text()='{}']".format(Constant.Home_DontEmailLinksShareInspiration))
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    if heading and flight and hotel and rent and car and title and first and second and third and forth:
        return True
    else:
        return False

def verifyFooter():
    return baseScript.display_element("xpath",".//footer[@class='global-footer purple']")
    baseScript.timeInterval(2)

