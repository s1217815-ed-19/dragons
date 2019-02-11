#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def settlementDanger(settlement):
    '''find what regions a settlement is contained in. 
    return information in a JSON'''
    
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()
    
    #is a settlement within a dragon habitat
    query = "SELECT A.REGION_ID, A.NAME, B.SETTLEMENT_ID, B.NAME
FROM S1234874.REGION A, S1234874.SETTLEMENTS B
WHERE SDO_CONTAINS(A.SHAPE, B.LOCATION) = 'TRUE'
AND B.NAME ="+settlement

    c.execute(query)
    html = {}
    for row in c:
        #create a dictionary to store the information
        html["settlement"] = row[1] #settlement name
        html["habitat"] = row[3] #habitat name
        #html[] = row[] #type of dragon
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
     testvar = settlementDanger(settlement)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
        

    
