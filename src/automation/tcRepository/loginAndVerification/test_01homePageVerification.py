from automation.framework import baseBrowser
from automation.framework import baseScript
from automation.pageObject import homePage


#Documentation
#test_scenarion01 method loads browser, verifies vacation champ logo, header menu, Home page Content and footer
def test_scenario01():
    baseBrowser.loadbrowser()
    print("Verify Logo")
    assert True == homePage.verifyLogo()
    print("Verify Menu")
    assert True == homePage.verifyHeaderMenu()
    print("Verify Homepage Content")
    assert True ==homePage.verifyHomepageContent()
    assert True==homePage.verifyFooter()
    baseScript.timeInterval(2)
    #baseBrowser.closebrowser()