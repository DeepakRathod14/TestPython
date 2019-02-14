from automation.framework import baseBrowser
from automation.pageObject import login
from automation.pageObject import homePage
from automation.framework import Constant
import  time
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

# Documentation test_validlogin method loads browser, logs in to the system by providing credentials,stored in configuration.txt file
#hence in case of change in credentials only configuraton.txt file is modified, and if user login  successful then verify sign out link.

def test_validlogin():
    baseBrowser.loadbrowser()
    print("------Scenario-1--------")
    print("Steps")
    print("1.Enter valid user name and password")
    login.forLogin(baseBrowser.USERNAME,baseBrowser.PASSWORD)
    print("2.Verify Login User Name")
    time.sleep(5)
    element=homePage.loginUserName(baseBrowser.USER_DISPLAY_NAME)
    if (element):
        print("3.User Login Successful - Pass")
    else:
       print("4.fail")
       assert element == False
    homePage.signOut()

# Documentation test_Invalidlogin method try to login in to the system by providing wrong username,
# if user name is wrong than verify error message, take a screen shot and save it into the directory.

def test_Invalidlogin():
    print("------Scenario-2--------")
    time.sleep(2)
    print("Steps")
    print("1.Enter Invalid user name and password")
    login.forLogin("rgarcia", baseBrowser.PASSWORD)
    print("2.Verify Username and Password")
    element = login.validation(Constant.LoginValidationMsg)
    time.sleep(2)
    if (element):
        print("3.PASS")
    else:
        print("3.User Login Unsuccessful - FAIL")
        assert element == False




