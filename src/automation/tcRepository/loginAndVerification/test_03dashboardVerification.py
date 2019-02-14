from automation.framework import baseBrowser
from automation.framework import baseScript
from automation.pageObject import login
from automation.pageObject import dashbord
from automation.pageObject import homePage
#Documentation
#test_scenarion01 method loads browser, logs in to the system by providing credentials,stored in configuration.txt file
#hence in case of change in credentials only configuraton.txt file is modified, and verify loged user name and sign out link.

def test_scenario01():
    baseBrowser.loadbrowser()
    login.forLogin(baseBrowser.USERNAME,baseBrowser.PASSWORD)
    assert True == dashbord.verifyLoginUser(baseBrowser.USER_DISPLAY_NAME)

#After log in, test_scenarion02 method verifies vacation champ logo, header menu, My Profile and Sign out link,
#Dashboard Content, Recent activities and footer.

def test_scenario02():
    print("Verify Logo")
    assert True == dashbord.verifyLogo()
    print("Verify Menu")
    assert True == dashbord.verifyMenu()
    print("Verify User Action")
    assert True == dashbord.verifyUserAction()
    print("Verify Dashboard Content")
    assert True == dashbord.verifyDashboardContent1()
    print("Verify Recent Activity")
    assert True == dashbord.verifyDashboardContent2()
    print("Verify Footer")
    assert True == dashbord.verifyFooter()
    homePage.signOut()


