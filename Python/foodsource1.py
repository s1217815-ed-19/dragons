#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def foodSourceInside(foodSource):
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()
    
   #is a food source within a dragon habitat
   query = "SELECT A.REGION_ID, A.NAME
FROM S1234874.REGION A, S1234874.FOOD_SOURCE B
WHERE SDO_CONTAINS(A.SHAPE, B.LOCATION) = 'TRUE'
AND B.FOOD_TYPE = (SELECT FOOD_TYPE_ID FROM S1217815.FOOD_TYPE WHERE CLASS = '" +foodSource+"');" 
   
    c.execute(query)
    html = {}
    for row in c:
        html["habitat"] = row[1]

    conn.close()
    return html

if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

      #if the form is filled out, get the number, call the function, turn result into a JSON and send back
     if "foodSource" in form:
         foodSource =form['foodSource'].value
     testvar = foodSourceInside(foodSource)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
        
