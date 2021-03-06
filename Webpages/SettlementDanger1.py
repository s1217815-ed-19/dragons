#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json

cgitb.enable(format='text')
from jinja2 import Environment, FileSystemLoader

def settlementDanger(settlementdang):
    '''find what regions a settlement is contained in.
    return information in a JSON'''


    conn = cx_Oracle.connect("student/train@geosgen")
    c = conn.cursor()

    #is a settlement within a dragon habitat
    query = "SELECT A.REGION_ID, A.NAME, B.SETTLEMENT_ID, B.NAME FROM S1234874.REGION A, S1234874.SETTLEMENTS B WHERE SDO_CONTAINS(A.SHAPE, B.LOCATION) = 'TRUE' AND B.NAME ='"+settlementdang+"'"

    c.execute(query)
    html = {}
    html["settlement"] = settlement
    #habitat = []
    for row in c:
        #habitat = habitat.append(row[3])
        html["habitat"] = row[1]
        #print(habitat)
    #create a dictionary to store the information
    #html["habitat"] = habitat #habitat name

    conn.close()
    return html

if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

      #if the form is filled out, get the number, call the function, turn result into a JSON and send back
     #if "settlementdang" in form:
         #settlementdang =form['settlementdang'].value
     settlementdang = 'Budapest'
     testvar = settlementDanger(settlementdang)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
