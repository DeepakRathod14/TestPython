from email.mime import base

from automation.framework import baseScript
from automation.framework import baseBrowser
from automation.framework import Constant
from automation.framework.baseBrowser import driver


def searchforFlight():
    element = driver.find_element_by_xpath(".//*[@id='flightOneWayFromInput' or @id='flightReturnFromInput']")
    element.send_keys(baseBrowser.DCITY)
    baseScript.timeInterval(3)
    element.send_keys("\t")

    element = driver.find_element_by_xpath(".//*[@name='to']")
    element.send_keys(baseBrowser.ACITY)
    baseScript.timeInterval(3)
    element.send_keys("\t")

    element=driver.find_element_by_xpath(".//*[@id='startOneWay' or @id='start']/input")
    element.send_keys(baseBrowser.DDate)
    baseScript.timeInterval(3)
    element.send_keys("\t")

    if(baseScript.display_element("xpath",".//*[@id='end']/input")):
        element=driver.find_element_by_xpath(".//*[@id='end']/input")
        element.clear()
        element.send_keys(baseBrowser.ADate)
        baseScript.timeInterval(3)
        element.send_keys("\t")

    baseScript.click('xpath',".//*[@class='available-btns']")
    baseScript.timeInterval(2)
    baseScript.waitForElement(".// div[ @class ='row in-page-search-header'] // p[starts-with(text(), '{}')]".format(Constant.FlightSearch_ResultsExpireMsg))

def searchForFlight(DAirport,AAirport,DDate,ADate):
    element= driver.find_element_by_xpath(".//*[@id='flightOneWayFromInput' or @id='flightReturnFromInput']")
    baseScript.sendKeys('xpath',".//*[@id='flightOneWayFromInput' or @id='flightReturnFromInput']",DAirport)
    baseScript.timeInterval(3)
    element.send_keys("\t")

    element = driver.find_element_by_xpath(".//*[@name='to']")
    baseScript.sendKeys('xpath',".//*[@name='to']",AAirport)
    baseScript.timeInterval(3)
    element.send_keys("\t")

    element = driver.find_element_by_xpath(".//*[@id='startOneWay' or @id='start']/input")
    baseScript.sendKeys('xpath',".//*[@id='startOneWay' or @id='start']/input",DDate)
    baseScript.timeInterval(3)
    element.send_keys("\t")

    if (baseScript.display_element("xpath", ".//*[@id='end']/input")):
        element = driver.find_element_by_xpath(".//*[@id='end']/input")
        element.clear()
        baseScript.sendKeys('xpath',".//*[@id='end']/input",ADate)
        baseScript.timeInterval(3)
        element.send_keys("\t")

def clickOnWhatsAvailableNowBtn():
    baseScript.click('xpath', ".//*[@class='available-btns']")
    baseScript.timeInterval(2)
    baseScript.waitForElement(".// div[ @class ='row in-page-search-header'] // p[starts-with(text(), '{}')]".format(Constant.FlightSearch_ResultsExpireMsg))

def navigateBack():
    baseScript.timeInterval(2)
    #baseScript.click('xpath', ".//*[@id='backG']/text/tspan")
    baseScript.driver.back()
    baseScript.waitForElement(".//*[@id='trigger-flight']")

def gotoOneWayForm():
    baseScript.timeInterval(2)
    baseScript.click("xpath",".//*[@id='secondary-tabs']//a[text()='{}']".format(Constant.Dashboard_OneWay))
    baseScript.timeInterval(2)

#=========== ALL VERIFICATION METHODS ARE BELLOW HERE ========================
def verifyReturnDate():
    return baseScript.display_element("ID","end")

def varifyRequiredFieldMsg():
    return baseScript.display_element("xpath",".//div[text()='{}']".format(Constant.RequiredFieldMsg))