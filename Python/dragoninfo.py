#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def info_dragon(dragon):
    '''get all of the information about a field and make it into a dictionary '''
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()
    #get info about dragons
    query = "SELECT A.NAME, A.MIGRATION_ID, C.NAME FROM S1217815.DRAGONS A, S1234874.REGION C WHERE A.REGION_SUMMER_ID = C.REGION_ID AND A.NAME ='"+dragon+"'"
    c.execute(query)
    html = {}
    for row in c:
        #Create a dictionary to store information
        
        html["dragon"]= row[0]
        html["route"]= row[1]
        html["region"]= row[2]
       
           
    conn.close()
    return html


if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

     #if the form is filled out, get the number, call the function, turn result into a JSON and send back
     if "dragon" in form:
         dragon=form['dragon'].value
     #dragon = 'Wyvern'
     testvar =  info_dragon(dragon)
     jsonfield = json.dumps(testvar, indent=1)
     print(jsonfield)
