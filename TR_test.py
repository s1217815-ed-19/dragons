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

class RegionZonePolygon(PointSeqs):
    
    def __init__(self,zone_id,name,season,temp_max,temp_min,ar_x=[],ar_y=[]):
        self.id = zone_id
        self.name = name
        self.season = season
        self.temp_max = temp_max
        self.temp_min = temp_min
        c_point = len(ar_x)
        for i in range(c_point):
            self.append(Point(ar_x[i],ar_y[i]))
            
    def toGeoJson(self):
        return {'type' : 'Feature',
                'properties' : {
                        'zone_id' : self.id,'name' : self.name.values[0],'season' : self.season.values[0],'temp_max' : str(self.temp_max.values[0]),'temp_min' : str(self.temp_min.values[0])
                        },
                'geometry':{
                        'type' : 'Polygon',
                        'coordinates' : [self.coorArrToGeoJson()]
                        }}

def getRegionZonePolyJson(cs):
    '''    print (df.groupby('zone_id'))
    generate GeoJson for zones
    '''
    list_rec = []
    for row in cs:
        list_rec.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
        
    df = pd.DataFrame(list_rec, columns = ['zone_id','name','season','temp_max','temp_min','x','y'])
    xs_list = []
    ys_list = []
    name_list = []
    season_list = []
    temp_max_list=[]
    temp_min_list=[]
    zoneid_list = []
    for zone_id, pt in df.groupby('zone_id'):
        zoneid_list.append(zone_id)
        xs_list.append(pt.x)
        ys_list.append(pt.y) 
        name_list.append(pt.name)
        season_list.append(pt.season)
        temp_max_list.append(pt.temp_max)
        temp_min_list.append(pt.temp_min)
    #print (temp_min_list)
    zones_json_list = []

    for i in range(len(zoneid_list)):
        zones_json_list.append(RegionZonePolygon(zoneid_list[i],name_list[i],season_list[i],temp_max_list[i],temp_min_list[i],np.array(xs_list[i]),np.array(ys_list[i])).toGeoJson())

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
c2=connection.cursor()
c3 = connection.cursor()
c2.execute("select c.settlement_id, t.X, t.Y from s1234874.settlements c, TABLE(SDO_UTIL.GETVERTICES(c.location)) t")
c.execute("select c.region_id, c.name, c.season, c.temp_max, c.temp_min, t.x, t.y from s1234874.region c, table(sdo_util.getvertices(c.shape)) t")
c3.execute("select c.migration_id, t.X, t.Y from s1234874.migration c, TABLE(SDO_UTIL.GETVERTICES(c.route)) t")

jsonPoly = getRegionZonePolyJson(c)

print (jsonPoly)
jsonPtsMigration = getStartPtsJson(c3)
#print (jsonPtsMigration)
jsonPtsSettlements = getStartPtsJson(c2)
#print (jsonPtsSettlements)

#SELECT D.DRAGON_ID, D.NAME,A.REGION_ID,A.NAME,A.SEASON, SDO_GEOM.SDO_CENTROID(A.SHAPE,0.005).SDO_POINT.X X_COORD,SDO_GEOM.SDO_CENTROID(A.SHAPE,0.005).SDO_POINT.Y Y_COORD FROM S1234874.REGION A, S1217815.DRAGONS D WHERE A.REGION_ID = D.REGION_SUMMER_ID;

SELECT A._NAME DRAGON, B.NAME REGION, C.DIET, D.WINGSPAN, E.CLASS, F.COLOUR, G.FIRE, G.NOTES FROM S1217815.DRAGONS A, S1234874.REGION B, S1217815.DIET C, S1217815.WINGSPAN D, S1217815.WEIGHT_CLASS E, S1217815.COLOUR F, S1217815.DRAGON_TYPE G WHERE A.TYPE_ID = G.TYPE_ID AND B.REGION_ID = A.REGION_SUMMER_ID AND G.DIET_ID = C.DIET_ID AND D.WINGSPAN_ID = G.WINGSPAN_ID AND E.WEIGHT_ID = G.WEIGHT_ID AND F.COLOUR_ID = G.COLOUR_ID;    
