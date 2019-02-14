from xlrd import open_workbook
import xlwt
import xlsxwriter
def readExcelFile(filename):
    wb = open_workbook(filename)
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols
        items = []
        for row in range(1, number_of_rows):
            values = []
            for col in range(number_of_columns):
                value = (sheet.cell(row, col).value)
                values.append(value)
            items.append(values)
    return  items

def writeExcelFile(filename, sheetName, records):
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet(sheetName)
        line = 1
        for record in records:
            colomn = 0
            for row in record:
                bold = workbook.add_format({'bold': True})
                worksheet.write(line, colomn, row)
                worksheet.write('A1','Flight Price',bold)
                worksheet.write('B1','Airline Feature', bold)
                worksheet.write('C1','First Flight Name', bold)
                worksheet.write('D1','First Departure Airport',bold)
                worksheet.write('E1','Depature Time',bold)
                worksheet.write('F1','First Arrival Airport',bold)
                worksheet.write('G1','Arrival Time',bold)
                worksheet.write('H1','Flight Type',bold)
                worksheet.write('I1', 'Seat Class', bold)
                worksheet.write('J1','Second Flight Name', bold)
                worksheet.write('K1', 'Second Departure Airport', bold)
                worksheet.write('L1', 'Depature Time', bold)
                worksheet.write('M1', 'Second Arrival Airport', bold)
                worksheet.write('N1', 'Arrival Time', bold)
                worksheet.write('O1', 'Flight Type', bold)
                worksheet.write('P1', 'Seat Class', bold)
                colomn += 1
            line += 1
        workbook.close()


