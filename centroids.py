#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def getCentroids():
    '''get all the centroids for the regions'''
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()

    query = "SELECT A.REGION_ID, SDO_GEOM.SDO_CENTROID(A.SHAPE,0.005).SDO_POINT.X,SDO_GEOM.SDO_CENTROID(A.SHAPE,0.005).SDO_POINT.Y FROM S1234874.REGION A;"

    c.execute(query)
    html = {}
    for row in c:
        html[row[0]] = [row[1], row[2]]

    conn.close()
    print(html)
    return html

if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

     testvar = getCentroids()
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)

    

