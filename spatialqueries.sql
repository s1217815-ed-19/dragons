#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def routeHabitatIntersect(route, habitat):
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()
    query = "" #do a habitat and migration route intersect
    c.execute(query)
    html = {}
    for row in c:
        html["intersect"] = row[0]

    conn.close()
    return html

if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

     #if the form is filled out, get the number, call the function, turn result into a JSON and send back
     if "dragonroute" in form:
         route =form['dragonroute'].value
     if "habitat3" in form:
         habitat = form.['habitat3'].value
     testvar = routehabitatIntersect(route, habitat)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
