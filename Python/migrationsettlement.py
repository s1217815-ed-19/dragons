#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def migrationSettlement(settlement):
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()

    #how far is a settlement from a migration route
    query = "SELECT A.NAME, B.MIGRATION_ID, SDO_GEOM.SDO_DISTANCE(A.LOCATION, B.ROUTE, .005) FROM S1234874.SETTLEMENTS A, S1234874.MIGRATION B WHERE A.NAME='" +settlement+"'"
    c.execute(query)
    html = {}
    html["settlement"] = settlement
    distances = []
    route = []
    for row in c:
        distances.append(row[2])
        route.append(row[1])
        
    html["distances"] = distances
    html["route"] = route


    conn.close()
    return html

if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

      #if the form is filled out, get the number, call the function, turn result into a JSON and send back
     if "settlement" in form:
         settlement =form['settlement'].value
     #settlement = 'Budapest'
     testvar = migrationSettlement(settlement)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
        
