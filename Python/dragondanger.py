#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def dragonDanger(xcoord,ycoord):
    '''get all of the information about a field and make it into a dictionary '''
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()
    query = "SELECT A.REGION_ID, A.NAME FROM S1234874.REGION A WHERE SDO_CONTAINS(A.SHAPE, SDO_GEOMETRY(2001, 8307, SDO_POINT_TYPE("+xcoord+","+ycoord+", NULL), NULL, NULL)) = 'TRUE'"
    c.execute(query)
    html = {}
    for row in c:
        #Create a dictionary to store information
        html["region"]= row[1]
        
    conn.close()
    return html


if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

     #if the form is filled out, get the number, call the function, turn result into a JSON and send back
     if "xcoord" in form:
         xcoord=form['xcoord'].value
     if "ycoord" in form:
         ycoord=form['ycoord'].value
     #coord = '19'
     #coord = '47'
     testvar = dragonDanger(xcoord, ycoord)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
