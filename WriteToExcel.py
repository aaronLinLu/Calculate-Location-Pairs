__author__ = 'Aaron'
import googlemaps
import xlrd
import json
import xlwt
from datetime import datetime

def WriteToExcel(fileName,returnList,departureTimeList):
    # <1> Output Path Preparation
    book = xlwt.Workbook()
    sheet = book.add_sheet('Sheet_1')
    outputExcel = ""

    for num in range(0, fileName.count('\\')+1):
        if num != fileName.count('\\'):
            outputExcel += fileName.split('\\')[num] + "\\"
        else:
            newName = fileName.split('\\')[num].split('.')[0]
    outputExcel += "Output_" + newName + ".xls"

    # <2>. Some Initialization of default variables
    departTimeNum = len(returnList[0]['Departure_time'])

    headerRow = 0
    columnFields = ['ID', 'Orig', 'Dest']
    repeatList = ['Departure_time',
                  'duration_in_traffic_value', 'duration_in_traffic_text',
                  'duration_value', 'duration_text',
                  'distance_value', 'distance_text']
    TOTALFIELDS = len(columnFields) + (len(repeatList) * departTimeNum)

    # <3>. Populating Header Row
    for pos in range(0, len(columnFields)):
        sheet.write(headerRow, pos, columnFields[pos])
    for times in range(0, departTimeNum):
        for item in range(0, len(repeatList)):
            sheet.write(headerRow, item + len(columnFields) + times * len(repeatList), repeatList[item])

    # <4>. Processing Each DepartureTime return
    BaseColList = []
    for i in range(0,departTimeNum):
        # Base Column = 3, 10, 17....
        BaseColList.append(len(columnFields) + len(repeatList) * i)


    for ele in returnList:
        Row = int(ele['ID'][0])
        for eachCol in range(0, TOTALFIELDS):
            # Populating Fields of ID, and
            # the coordinate pairs of Origins and Destinations
            if eachCol < len(columnFields):
                sheet.write(Row, eachCol, ele[columnFields[eachCol]][0])
            for steps in BaseColList:
                if eachCol == steps:
                    pos = int((steps-3)/7)
                    sheet.write(Row,eachCol,departureTimeList[pos])
                    # Inserting returned value one by one, using departTime as key
                    for eachField in range(1,len(repeatList)):
                        sheet.write(Row,eachCol + eachField,
                                    ele['Departure_time'][departureTimeList[pos]][repeatList[eachField]])

    book.save(outputExcel)
    return















