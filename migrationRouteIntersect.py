#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def routeIntersect(settlement):
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()
    query = "" #what migration routes intersect with the selected one
    c.execute(query)
    html = {}
    for row in c:
        html["route"] = row[]
        html["intersectingRoutes"] = #array

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
        
