__author__ = 'Aaron'
import googlemaps
import xlrd
import json
from datetime import datetime
# Documentation
'''
   The input excel sheet should have the format:

   Long1  Lat1  Long2  Lat2      ---- header row
    y1     x1    y2     x2
    y3     x3    y4     x4
   ....

Also, all latitude value should be in range (-90,90), and longitude value in range (-180,180).
Otherwise the script will prompt the user with error message.

'''

def ValidateInput(file_location):
    '''

    :param file_location:
    :return:
    '''

    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(0)
    if (sheet.ncols == 4):
        header_row = []
        for col in range(sheet.ncols):
            header_row.append(sheet.cell_value(0,col))
        if (len(header_row) == len(set(header_row))): # then fields in the header row are unique
            GoodHeader = True
            pass
        else:
            GoodHeader = False
            print("Fields in the header row are not unique; please double check them.")

    '''
      should add codes to check lat-/long-
    '''
    GoodLong = True
    GoodLat = True

    for col in range(sheet.ncols):
        if ('o' in sheet.cell_value(0,col)): # consider this column has longitude data
            for row in range(1,sheet.nrows):
                if ( sheet.cell_value(row,col) > 180 or sheet.cell_value(row,col) < -180):
                    GoodLong = False
        elif ('a' in sheet.cell_value(0,col)):     # consider this column has latitude data
            for row in range(1,sheet.nrows):
                if ( sheet.cell_value(row,col) > 90 or sheet.cell_value(row,col) < -90):
                    GoodLat = False

    if (GoodLat and GoodLong):
        pass
    elif (not GoodLat):
        print("Some latitude data are invalid.")
    elif (not GoodLong):
        print("Some longitude data are invalid.")

    return (GoodHeader and GoodLong and GoodLat)











