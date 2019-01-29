#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def settlementDanger(settlement):
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()
    query = "" #is a settlement withing a dragon habitat
    c.execute(query)
    html = {}
    for row in c:
        #create a dictionary to store the information
        html["settlement"] = row[] #settlement name
        html["habitat"] = row[] #habitat name
        html["dragon"] = row[] #type of dragon
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
        

    
