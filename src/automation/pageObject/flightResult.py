from automation.framework import baseScript
from selenium import webdriver
from automation.framework.baseScript import driver
from automation.framework.FileReadHelper import writeExcelFile
from automation.framework import Constant

def GetFlightResults(StartingDiv):
    grid =[]
    size = len(driver.find_elements_by_xpath(".//*[@class='card ng-scope']"))
    print(size)
    for x in range(StartingDiv,size):
        rows=[]
        price = baseScript.getText("xpath",".//*[@class='card ng-scope'][{}]//div[starts-with(@class,'card-price-point')]/p".format(x))
        #price = price+baseScript.getText("xpath.//*[@class='card ng-scope'][{}]//div[starts-with(@class,'card-price-point')]/sup".format(x))
        AirlineFeature = baseScript.getText("xpath",".//*[@class='card ng-scope'][{}]//div[starts-with(@class,'card-feature')]/a".format(x))
        FirstFlightName = baseScript.getText("xpath","html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[1]/div[1]/p".format(x,size))
        FirstDepartureAirport = baseScript.getText("Xpath","html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[1]/div[2]/div[1]/p[1]".format(x,size))
        DepartureTime1 = baseScript.getText('Xpath',"html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[1]/div[2]/div[1]/p[2]".format(x,size))
        FirstArrivalAirport = baseScript.getText("Xpath","html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[1]/div[2]/div[2]/p[1]".format(x,size))
        ArrivalTime1 = baseScript.getText('Xpath',"html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[1]/div[2]/div[2]/p[2]".format(x,size))
        FlightType1=baseScript.getText('XPath',"html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[1]/div[2]/div[3]/p[1]/ng-pluralize".format(x,size))
        SeatClass1=baseScript.getText('xpath',"html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[1]/div[2]/div[3]/p[2]".format(x,size))
        SecondFlightName = baseScript.getText("xpath","html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[2]/div[1]/p".format(x,size))
        SecondDepartureAirport=baseScript.getText('xpath',"html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[2]/div[2]/div[1]/p[1]".format(x,size))
        DepartureTime2=baseScript.getText('xpath',"html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[2]/div[2]/div[1]/p[2]".format(x,size))
        SecondArrivalAirport=baseScript.getText('xpath',"html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[2]/div[2]/div[2]/p[1]".format(x,size))
        ArrivalTime2=baseScript.getText('xpath',"html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[2]/div[2]/div[2]/p[2]".format(x,size))
        FlightType2=baseScript.getText('xpath',"html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[2]/div[2]/div[3]/p[1]/ng-pluralize".format(x,size))
        SeatClass2=baseScript.getText('xpath',"html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[2]/div[2]/div[3]/p[2]".format(x,size))
       #value2 = baseScript.getText("xpath","html/body/div[5]/div[2]/div/div/div[1]/div[1]/div[4]/div/div[{}]/div[2]/div[3]/div[2]".format(x,size))

        print("*******************************")
        print("Price Of Flights -",price)
        print("Airline Feature -",AirlineFeature)
        print("First Flight Name -",FirstFlightName)
        print("First Depature Airport -",FirstDepartureAirport)
        print("Departure Time -",DepartureTime1)
        print("First Arrival Airport -",FirstArrivalAirport)
        print("Arrival Time -",ArrivalTime1)
        print("Flight Type -",FlightType1)
        print("Seat Class -",SeatClass1)
        print("Second Flight Name -",SecondFlightName)
        print("Second Depature Airport -", SecondDepartureAirport)
        print("Departure Time -", DepartureTime2)
        print("Second Arrival Airport -", SecondArrivalAirport)
        print("Arrival Time -", ArrivalTime1)
        print("Flight Type -", FlightType2)
        print("Seat Class -", SeatClass2)

        rows.append(price)
        rows.append(AirlineFeature)
        rows.append(FirstFlightName)
        rows.append(FirstDepartureAirport)
        rows.append(DepartureTime1)
        rows.append(FirstArrivalAirport)
        rows.append(ArrivalTime1)
        rows.append(FlightType1)
        rows.append(SeatClass1)
        rows.append(SecondFlightName)
        rows.append(SecondDepartureAirport)
        rows.append(DepartureTime2)
        rows.append(SecondArrivalAirport)
        rows.append(ArrivalTime2)
        rows.append(FlightType2)
        rows.append(SeatClass2)
        grid.append(rows)
    writeExcelFile("{}","Flight Data".format(Constant.FlightSearchResultFile),grid)

