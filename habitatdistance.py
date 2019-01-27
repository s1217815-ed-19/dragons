#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def habitatDistance(habitat1, habitat2):
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()
    query = "" #how far are the centroids of two habitats from each other
    c.execute(query)
    html = {}
    for row in c:
        html["habitat1"] = row[]
        html["habitat2"] = row[]
        html["distance"] = row[]

    conn.close()
    return html

if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

     #if the form is filled out, get the number, call the function, turn result into a JSON and send back
     if "habitat1" in form:
         habitat1 =form['habitat1'].value
     if "habitat2" in form:
         habitat2 = form.['habitat2'].value
     testvar = habitatDistance(habitat1, habitat2)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
