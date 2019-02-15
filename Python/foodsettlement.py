#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def foodSourceSettlement(settlement):
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()

    #how far is a settlement from food sources
    query = "SELECT A.NAME, B.FOOD_TYPE, SDO_GEOM.SDO_DISTANCE(A.LOCATION, B.LOCATION, .005) FROM S1234874.SETTLEMENTS A, S1234874.FOOD_SOURCE B WHERE A.NAME ='"+settlementfood+"'" 
    
    c.execute(query)
    html = {}
    html["settlement"] = settlementfood
    distances = []
    foodsources = []
    for row in c:
        distances.append(row[2])
        foodsources.append(row[1])

    html["distances"] = distances
    html["foodsources"] = foodsources
    conn.close()
    return html

if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

      #if the form is filled out, get the number, call the function, turn result into a JSON and send back
     if "settlementfood" in form:
         settlementfood =form['settlementfood'].value
     #settlementfood = 'Budapest'
     testvar = foodSourceSettlement(settlementfood)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
        

