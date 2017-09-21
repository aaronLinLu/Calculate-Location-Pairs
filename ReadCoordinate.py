__author__ = 'Aaron'
import googlemaps
import xlrd
import json
from datetime import datetime

'''
   it should read pairs of coordinates ---> list of pairs of coordinates
   e.g.
   list = [(x1,y1),(x2,y2),(x3,y3),(x4,y4)...]
   this list always has even number of elements
'''

def ReadCoordinate(file_location):
    '''

    :param file_location:
    :return:
    '''

    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(0)

    list = []

    if (sheet.cell_value(0,0) == 'Long1' or
        sheet.cell_value(0,0) == 'long1' or
        sheet.cell_value(0,0) == 'long' or
        sheet.cell_value(0,0) == 'Long' or
        sheet.cell_value(0,0) == 'lon' or
        sheet.cell_value(0,0) == 'Lon' or
        'o' in sheet.cell_value(0,0)):


        for row in range(1, sheet.nrows):
            tup1 = (sheet.cell_value(row, 1), sheet.cell_value(row, 0))
            list.append(tup1)
            tup2 = (sheet.cell_value(row, 3), sheet.cell_value(row, 2))
            list.append(tup2)

    else:
        for row in range(1, sheet.nrows):
            tup1 = (sheet.cell_value(row, 0), sheet.cell_value(row, 1))
            list.append(tup1)
            tup2 = (sheet.cell_value(row, 2), sheet.cell_value(row, 3))
            list.append(tup2)

    return list



