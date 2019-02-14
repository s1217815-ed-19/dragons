#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def routeIntersect(route):
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()
    
    #what migration routes intersect with the selected one
    query = "SELECT A.MIGRATION_ID, B.MIGRATION_ID
FROM S1234874.MIGRATION A, S1234874.MIGRATION B
WHERE A.MIGRATION_ID =
(SELECT MIGRATION_ID FROM S1217815.DRAGONS WHERE NAME = '" +route+"')
AND SDO_RELATE(A.ROUTE, B.ROUTE, 'MASK = TOUCH') = 'TRUE';" 
    
    c.execute(query)
    html = {}
    html["route"] = route
    intersectingRoutes = []
    for row in c:
        intersectingRoutes = intersectingRoutes.append(row[1])
        
    html["intersectingRoutes"] = intersectingRoutes

    conn.close()
    return html

if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

      #if the form is filled out, get the number, call the function, turn result into a JSON and send back
     if "dragonroute" in form:
         dragonroute =form['dragonroute'].value
     testvar = routeIntersect(settlement)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
        
