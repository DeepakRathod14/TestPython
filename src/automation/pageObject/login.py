from automation.framework.baseBrowser import driver
from automation.framework import baseScript
from automation.framework import Constant
import time

#to enter username and password
def forLogin(username, password):
    driver.implicitly_wait(10)
    baseScript.click('XPATH', ".//*[@class='trigger-sign-in-modal sign-in']")
    baseScript.sendKeys('XPATH', ".//*[@id='frmLogin']/input[1]", username)
    baseScript.sendKeys('XPATH', ".//*[@id='frmLogin']/input[2]", password)
    time.sleep(1)
    baseScript.click('XPATH', ".//*[@id='frmLogin']/div[4]")
    time.sleep(5)

#for verify validation message
def validation(error_message):
    print("Observe Validation Message")
    time.sleep(2)
    print(".//*[@id='frmLogin']/div[text()='{}']".format(error_message))
    #print(".//*[@id='frmOk']/div[normalize-space(.)='{}']".format(error_message))
    driver.get_screenshot_as_png()
    driver.save_screenshot(Constant.ScreenShotPath)
    return baseScript.display_element('XPATH',".//*[@id='frmLogin']/div[text()='{}']".format(error_message))
    #return baseScript.display_element('xapth',".//*[@id='frmOk']/div[normalize-space(.)='{}']".format(error_message))
