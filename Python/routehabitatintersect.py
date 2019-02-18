#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json

cgitb.enable(format='text')



def routeHabitatIntersect(dragonroute2):
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()

    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()

    #do a habitat and migration route intersect
    query = "S" + "ELECT A.NAME, B.MIGRATION_ID FROM S1234874.REGION A, S1234874.MIGRATION B WHERE B.MIGRATION_ID =(SELECT MIGRATION_ID FROM S1217815.DRAGONS WHERE NAME = '" +dragonroute2+"') AND SDO_RELATE(A.SHAPE, B.ROUTE, 'MASK = ANYINTERACT') = 'TRUE'"

    c.execute(query)
    html = {}
    html["route"] = dragonroute2
    habname = []
    for row in c:
        habname.append(row[0])
        #habname = [row[0]]
        #print(habname)
    html["HabitatName"] = habname

    conn.close()
    return html

if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

     #if the form is filled out, get the number, call the function, turn result into a JSON and send back
     if "dragonroute2" in form:
         dragonroute2 =form['dragonroute2'].value
     #route = 'Wyvern'
     testvar = routeHabitatIntersect(dragonroute2)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
