__author__ = 'Aaron'
import googlemaps
import xlrd
import json
from datetime import datetime
from operator import itemgetter
# Documentation
'''

  Given a list of tuples (pairs of lat/long), and a list of departure time,
  return a set of lists of formatted travel time and distance information.

  definition:
      -- duration:              total travel time assuming free flow
      -- duration in traffic:   total travel time taking into account real traffic condition

  e.g. [ (40.714224, -73.961452), (41.923237, -75.8721321) ]  and  [ 1484028135, 1484027154, 14840272708 ]

      --- >>>>
      Stylization I:
      departure_time_1484028135 = [ '(40.714224, -73.961452) and (41.923237, -75.8721321)': [ '12 hours 48 mins', '12 hours 30 mins', '1,275 km']  ]
      departure_time_1484027154 = [ '(40.714224, -73.961452) and (41.923237, -75.8721321)': [ '12 hours 35 mins', '12 hours 30 mins', '1,275 km']  ]
      departure_time_1484027208 = [ '(40.714224, -73.961452) and (41.923237, -75.8721321)': [ '12 hours 32 mins', '12 hours 30 mins', '1,275 km']  ]

      Stylization II (implemented):
      return_list  = [ Pair1: {'departure_time':{'time1':{'duration': xxxx, 'duration_in_traffic': xxxx, 'distance': xxxx,'ID':xx, 'Orig':xxx, 'Dest':xxx}
                               'departure_time':{'time2':{'duration': xxxx, 'duration_in_traffic': xxxx, 'distance': xxxx,'ID':xx, 'Orig':xxx, 'Dest':xxx}},

                       Pair2: {'departure_time':{'time1':{'duration': xxxx, 'duration_in_traffic': xxxx, 'distance': xxxx,'ID':xx, 'Orig':xxx, 'Dest':xxx}},
                               'departure_time':{'time2':{'duration': xxxx, 'duration_in_traffic': xxxx, 'distance': xxxx,'ID':xx, 'Orig':xxx, 'Dest':xxx}},
                                                                ................
                       PairN: {'departure_time':{'time1':{'duration': xxxx, 'duration_in_traffic': xxxx, 'distance': xxxx,'ID':xx, 'Orig':xxx, 'Dest':xxx}},
                               'departure_time':{'time2':{'duration': xxxx, 'duration_in_traffic': xxxx, 'distance': xxxx,'ID':xx, 'Orig':xxx, 'Dest':xxx}} ]

'''



def ComputeDistanceAndTime(coordinate_list,departureTime_list,API_key):
    '''
    :param coordinate_list:
    :param departure_time_list:
    :param API_key:
    :return:
    '''

    default_APIKey_distanceMatrix = 'AIzaSyDDr4vVS1ER6QewCcTDGT8FAuQSOLiFbmE'
    default_traffic_model = 'best_guess'
    default_mode = 'driving'

    if API_key == '':
        theKey = default_APIKey_distanceMatrix
    else:
        theKey = API_key

    gmaps_distMatrix = googlemaps.Client(key=theKey)

    # below is a list of dictionary storing all returned information, about duration and distance, etc.
    list_l = []
    ID = 1

    for i in range(0,len(coordinate_list)-1):
        if (i % 2 == 0):
            Orig = str(coordinate_list[i]).strip('()')
            Dest = str(coordinate_list[i + 1]).strip('()')
            # Initiate each object
            Pair = dict()
            Pair['ID'] = [ID]
            ID += 1
            Pair['Orig'] = [Orig]
            Pair['Dest'] = [Dest]
            Pair['Departure_time'] = dict()

            # getting 3 returns for each departure_time for each pair
            for departTime in departureTime_list:
                dist = gmaps_distMatrix.distance_matrix(Orig, Dest,
                                                        departure_time=departTime,
                                                        mode=default_mode,
                                                        traffic_model=default_traffic_model)

            if (dist['rows'][0]['elements'][0]['status'] == 'OK'):
                Pair['Departure_time'][departTime] = {'duration_value':
                                                          dist['rows'][0]['elements'][0]['duration']['value'],
                                                      'duration_text':
                                                          dist['rows'][0]['elements'][0]['duration']['text'],
                                                      'duration_in_traffic_value':
                                                          dist['rows'][0]['elements'][0]['duration_in_traffic']['value'],
                                                      'duration_in_traffic_text':
                                                          dist['rows'][0]['elements'][0]['duration_in_traffic']['text'],
                                                      'distance_value':
                                                          dist['rows'][0]['elements'][0]['distance']['value'],
                                                      'distance_text':
                                                          dist['rows'][0]['elements'][0]['distance']['text']}
            else:
                Pair['Departure_time'][departTime] = {'duration_value':
                                                          'NULL',
                                                      'duration_text':
                                                          'NULL',
                                                      'duration_in_traffic_value':
                                                          'NULL',
                                                      'duration_in_traffic_text':
                                                          'NULL',
                                                      'distance_value':
                                                          'NULL',
                                                      'distance_text':
                                                          'NULL'}

            # add this object to the return_list
            list_l.append(Pair)

    # sort the list by ID
    sorted_list_l = sorted(list_l,key=itemgetter('ID'))

    return sorted_list_l























