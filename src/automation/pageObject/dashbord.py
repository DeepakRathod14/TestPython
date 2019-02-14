import profile
from automation.framework.baseBrowser import driver
from automation.framework import baseScript
from automation.framework import Constant

import time

def performAction(actionName):
    baseScript.timeInterval(2)
    baseScript.click("xpath", ".//*[contains(@id,'{}')]".format(actionName))
    baseScript.timeInterval(1)
    baseScript.waitForElement(".//*[@id='secondary-tabs']//a[text()='{}']".format(Constant.Dashboard_OneWay))

def verifyLogo():
    return baseScript.display_element("xpath",".//a[@alt='Go to home page']/img[@src='/Content/assets/img/Logo.png']")

def verifyMenu():
    mytrip = baseScript.display_element("xpath",".//ul[@class='nav-left']//a[normalize-space(.)='{}']".format(Constant.Dashboard_MyTrips))
    inbox = baseScript.display_element("xpath", ".//ul[@class='nav-left']//a[normalize-space(.)='{}']".format(Constant.Dashboard_Inbox))
    collection = baseScript.display_element("xpath", ".//ul[@class='nav-left']//a[normalize-space(.)='{}']".format(Constant.Dashboard_Collections))
    profile = baseScript.display_element("xpath", ".//ul[@class='nav-left']//a[normalize-space(.)='{}']".format(Constant.Dashboard_Profile))
    if mytrip and inbox and collection and profile:
        return True
    else:
        return False

def verifyLoginUser(username):
    #return baseScript.display_element("xpath",".//div[@class='profile-block']//p{}".format(username))
    return baseScript.display_element("xpath",".//div[@class='profile-block']//p[text()='{}']".format(username))
def verifyUserAction():
    baseScript.click("xpath",".//div[@class='profile-block']")
    myProfile=baseScript.display_element("xpath",".//div[@class='dropdown profile ng-isolate-scope']//a[normalize-space(.)='{}']".format(Constant.Banner_MyProfile))
    baseScript.timeInterval(2)
    singout = baseScript.display_element("xpath",".//div[@class='dropdown profile ng-isolate-scope']//a[normalize-space(.)='{}']".format(Constant.Banner_SignOut))
    baseScript.timeInterval(2)
    baseScript.click("xpath", ".//div[@class='profile-block active']")
    if(myProfile and singout):
        return True
    else:
        return False

def verifyDashboardContent1():
    baseScript.timeInterval(2)
    heading = baseScript.display_element("xpath", ".//h1[text()='Welcome to VacationChamp']")
    flight = baseScript.display_element("xpath",".//*[contains(@id,'flight')]")
    baseScript.timeInterval(2)
    hotel =  baseScript.display_element("xpath",".//*[contains(@id,'hotel')]")
    baseScript.timeInterval(2)
    rent = baseScript.display_element("xpath",".//*[contains(@id,'rental')]")
    baseScript.timeInterval(2)
    car = baseScript.display_element("xpath",".//*[contains(@class,'car ')]")
    commingSoon = baseScript.display_element("xpath",".//div[starts-with(@class,'option car')]//div[normalize-space(.)='Coming Soon']")
    baseScript.timeInterval(1)
    if heading and flight and hotel and rent and car and commingSoon:
        return True
    else:
        return False

def verifyDashboardContent2():
      #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      driver.execute_script("window.scrollBy(0,500);")
      baseScript.timeInterval(2)
      title= baseScript.display_element("xpath",".//section[@class='recent-activity bg-blurple ng-scope']//div[@class='title']")
      #driver.execute_script("window.scrollIntoView();", ".//section[@class='recent-activity bg-blurple ng-scope']//div[@class='title']")
      baseScript.timeInterval(2)
      instantBooking=baseScript.display_element("xpath",".//*[@class='spaced-out blurple' and text()='{}']".format(Constant.Dashboard_InstantBookings))
      baseScript.timeInterval(2)
      recentSearch=baseScript.display_element("xpath",".//*[@class='spaced-out blurple' and text()='{}']".format(Constant.Dashboard_RecentSearches))
      driver.execute_script("window.scrollBy(0,500);")
      baseScript.timeInterval(2)
      continousSearch = baseScript.display_element("xpath", ".//*[@class='medium blurple' and text()='{}']".format(Constant.Dashboard_ContinuousSearches))
      baseScript.timeInterval(2)
      myRequest = baseScript.display_element("xpath", ".//*[@class='spaced-out blurple' and text()='{}']".format(Constant.Dashboard_MyRequests))
      baseScript.timeInterval(2)
      saveCollection = baseScript.display_element("xpath", ".//*[@class='medium blurple' and text()='{}']".format(Constant.Dashboard_RecentlySavedToCollections))
      baseScript.timeInterval(2)
      recentBooking = baseScript.display_element("xpath", ".//*[@class='medium blurple' and text()='{}']".format(Constant.Dashboard_RecentBookings))
      driver.execute_script("window.scrollBy(0,500);")
      if title and instantBooking  and recentSearch and continousSearch and myRequest and saveCollection and recentBooking:
          return True
      else:
          return False

def verifyFooter():
     baseScript.timeInterval(2)
     return baseScript.display_element("xpath",".//*[@class='global-footer']")

