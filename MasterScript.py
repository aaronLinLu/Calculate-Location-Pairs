__author__ = 'Aaron'
import googlemaps
import json
import xlwt
from datetime import datetime
from ReadCoordinate import ReadCoordinate
from ValidateInput import ValidateInput
from GeocodeAddress import GeocodeAddress
from ComputeDistanceAndTime import ComputeDistanceAndTime
from WriteToExcel import WriteToExcel

startTime = datetime.now()
#  Specify your input excel sheet here
file_location = "C:\\Users\luckylulin\Desktop\Spring 2017\Geography170\FinalProject\GoogleMap_ExcelFiles\Actual10Points.xlsx"
if (ValidateInput(file_location)):
    coord_list = ReadCoordinate(file_location)

print("Coordinate list has " + str(int(len(coord_list)/2)) + " pair(s) of origins-and-destinations.")
print("Coordinate list is ")
print(coord_list)

'''
actual processing
'''
# (1). Geocode (optional)
# enter your Geocode API key here; if left blank (as it is now), it uses Lin's API key as default.
geocode_API_key = ""
#address_list = GeocodeAddress(coord_list,geocode_API_key)


# (2). Get travel time (required)
# enter your DistanceMatrix API key here...
distanceMatrix_API_key = ""
# 1487636888
#departTime_list = ['1496653200','1496664000','1496674800','1496685600','1496696400']
# June 5th, 9 am, 12 pm, 3 pm, 6 pm, 9 pm....
departTime_list = ['1496739600']
TimeAndDistanceList = ComputeDistanceAndTime(coord_list,departTime_list,distanceMatrix_API_key)


# (3). Write to an Excel SpreadSheet
print("The returned TimeAndDistanceList by Google API is: ")
for ele in TimeAndDistanceList:
    print(ele)

WriteToExcel(fileName=file_location,returnList=TimeAndDistanceList,departureTimeList=departTime_list)

endTime = datetime.now()
print("\nIt takes this much time " + str(endTime-startTime) + " to complete the task.")
print("Success!")
