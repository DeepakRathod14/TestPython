from automation.framework.baseBrowser import driver
import time

def highlight(element):
    driver.execute_script("arguments[0].style.border='2px solid green'", element)

def timeInterval(second):
    time.sleep(second)

#For display an element
def display_element(ele,ele_value):
    try:
        element = detect_element(ele, ele_value)
        return element.is_displayed()
    except Exception as e:
        print(e)
    return False

#For finding Element
def detect_element(ele,ele_value):
    try:
        if ele == 'XPATH' or 'xpath' or 'Xpath':
            element = driver.find_element_by_xpath(ele_value)
        elif ele == 'ID' or 'id' or 'Id':
            element = driver.find_elements_by_id(ele_value)
        elif ele == 'NAME' or 'Name' or 'name':
            element = driver.find_element_by_name(ele_value)
        elif ele == 'CSS' or 'css' or 'Css':
            element = driver.find_element_by_css_selector(ele_value)
        elif ele == 'CLASS NAME' or 'class name' or 'Class name':
            element = driver.find_element_by_class_name(ele_value)
        else:
            print(ele, "ele not found")
        highlight(element)
    except Exception as e:
        print(e)
    return element

def click(ele,ele_value):
    element = detect_element(ele,ele_value)
    element.click()

#to send value in element
def sendKeys(ele,ele_value,value):
    try:
        element = detect_element(ele, ele_value)
        highlight(element)
        element.send_keys(value)
    except Exception as e:
        print(e)
def getText(ele,ele_val):
    element = detect_element(ele, ele_val)
    if element != None:
        return element.text
    else:
        return None

def waitForElement(ele_Val):
    for i in range(0,200):
        try:
            driver.find_element_by_xpath(ele_Val).is_displayed()
            timeInterval(1)
            break
        except Exception as e:
            print(e)
            timeInterval(1)

