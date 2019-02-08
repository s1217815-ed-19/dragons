#import cgi
#import cgitb
import pandas as pd
import pyproj
import cx_Oracle
import json
import numpy as np
#cgitb.enable()

class Point:
    def __init__(self,r_x,r_y):
        self.x = r_x
        self.y = r_y

    def toLatLon(self):
        wgs84=pyproj.Proj("+init=EPSG:4326")
        map_proj = pyproj.Proj("+init=EPSG:4326")
        lon,lat = pyproj.transform(map_proj,wgs84, self.x, self.y)
        self.x = lon
        self.y = lat

    def getLatLon(self):
     #   self.toLatLon()
        return [self.x,self.y]
    
    def coorToGeoJson(self):
        return {'type' : 'Point',
                'coordinates':[self.x,self.y]}


class StartPoint(Point):
    def __init__(self,r_id,r_x,r_y):
        self.id = r_id
        self.x = r_x
        self.y = r_y
        
    def toGeoJson(self):
        return {'type' : 'Feature',
                'properties' : {
                        'start_id' : self.id
                        },
                'geometry':self.coorToGeoJson()}

class PointSeqs(list):
    def __init__(self,ar_x=[],ar_y=[]):
        c_point = len(ar_x)
        for i in range(c_point):
            self.append(Point(i,ar_x[i],ar_y[i]))
        
    def coorArrToGeoJson(self):
        coor_list = []
        for pt in self:
            coor_list.append(pt.getLatLon())
        return coor_list

class ZonePolygon(PointSeqs):
    
    def __init__(self,zone_id,ar_x=[],ar_y=[]):
        self.id = zone_id
        c_point = len(ar_x)
        for i in range(c_point):
            self.append(Point(ar_x[i],ar_y[i]))
            
    def toGeoJson(self):
        return {'type' : 'Feature',
                'properties' : {
                        'zone_id' : self.id
                        },
                'geometry':{
                        'type' : 'Polygon',
                        'coordinates' : [self.coorArrToGeoJson()]
                        }}

def getZonePolyJson(cs):
    '''
    generate GeoJson for zones
    '''
    list_rec = []
    for row in cs:
        list_rec.append([row[0],row[1],row[2]])
        
    df = pd.DataFrame(list_rec, columns = ['zone_id','x','y'])
    xs_list = []
    ys_list = []
    zoneid_list = []
    for zone_id, pt in df.groupby('zone_id'):
        zoneid_list.append(zone_id)
        xs_list.append(pt.x)
        ys_list.append(pt.y)
        
    zones_json_list = []
    for i in range(len(zoneid_list)):
        zones_json_list.append(ZonePolygon(zoneid_list[i],np.array(xs_list[i]),np.array(ys_list[i])).toGeoJson())

    return json.dumps(zones_json_list)

def getStartPtsJson(cs):
    '''
    generate GeoJson for startpoints
    '''
    points_json_list = []
    for pt in cs:
        stpt = StartPoint(pt[0],pt[1],pt[2])
        stpt.toLatLon()
        points_json_list.append(stpt.toGeoJson())

    return json.dumps(points_json_list)

connection = cx_Oracle.connect("s1217815/Jaya435@geosgen")
#typeObj = connection.gettype("SDO_GEOMETRY")
c= connection.cursor()
c2 = connection.cursor()
c2.execute("select c.region_id, t.X, t.Y from s1234874.region c, TABLE(SDO_UTIL.GETVERTICES(c.shape)) t")
c.execute("select c.region_id, t.x, t.y from s1234874.region c, table(sdo_util.getvertices(c.shape)) t")

jsonPoly = getZonePolyJson(c)
print (jsonPoly)
jsonPts = getStartPtsJson(c2)
print (jsonPts)
