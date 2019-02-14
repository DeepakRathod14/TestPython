from automation.framework import baseBrowser
from automation.pageObject import login
from automation.pageObject import dashbord
from automation.pageObject import searchFlight
from automation.framework import baseScript

#Documentation
#Automated By : Shivangi
#Search Flight : TC003
def test_scenario01():
    print("Scenario 01 : Verify action to click on Back link or icon")
    print("Load Browser successfully")
    baseScript.timeInterval(10)
    baseBrowser.loadbrowser()
    print("Precondition : User should be logged In and on the Dashboard Page.")
    login.forLogin(baseBrowser.USERNAME,baseBrowser.PASSWORD)
    print("Steps: ")
    print("=======================")
    print("1.Click on Flight navigation icon")
    dashbord.performAction("flight")
    print("2.Click on Back link or icon")
    searchFlight.navigateBack()
    baseBrowser.expectedResult()
    expectedResult = dashbord.verifyDashboardContent1()
    if(expectedResult):
        print("PASS")
    else:
        print("FAIL")
        print("User is not redirected back to the Home Page.")
        assert True == expectedResult
    print("User is redirected back to the Home Page.")

def test_scenario02():
    print("Verify action on clicking Single Trip")
    print("Load Browser successfully")
    print("Precondition : User should be logged In and on the Dashboard Page.")
    print("Steps: ")
    print("=======================")
    print("1.Click on Flight navigation icon")
    dashbord.performAction("flight")
    print("2. Click the 'Single Trip' link")
    searchFlight.gotoOneWayForm()
    expectedResult = searchFlight.verifyReturnDate()
    baseBrowser.expectedResult()
    if(expectedResult):
        print("FAIL")
        print("The link is not redirect to the Single trip form")
        assert False==expectedResult
    print("PASS")
    print("The link is redirect to the Single trip form")

def test_scenario03():
    print("Verify mandatory field")
    print("Load Browser successfully")
    print("Precondition : User should be logged In and on the Home page.")
    print("Steps: ")
    print("=======================")
    print("1.Click on Flight navigation icon")
    #dashbord.performAction("flight")
    print("2. Click the 'Single Trip' link")
    searchFlight.gotoOneWayForm()
    print("3.  Focus on 'Departure City'' and then press Tab without entering any value")
    searchFlight.searchForFlight(" "," "," "," ")
    expectedResult = searchFlight.varifyRequiredFieldMsg()
    baseBrowser.expectedResult()
    if(expectedResult):
        print("PASS")
        print("The Searchbox is show red highlight as a mandatory field")
    else:
        print("FAIL")
        print("The link is not redirect to the Single trip form")
        assert False==expectedResult

