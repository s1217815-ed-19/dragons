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
    #Relational join between Fields and Crops while bringing them in
    query = "SELECT * FROM DRAGONS WHERE DRAGONS.SUMMER = SUMMERREGION.ID AND DRAGONS.WINTER = WINTERREGION.ID AND DRAGON.TYPE = DRAGONTYPE.ID AND DRAGON.ID=" + dragon 
    c.execute(query)
    html = {}
    for row in c:
        #Create a dictionary to store information
        
        html["dragon"]= row[0]
        html["diet"]= row[5]
        html["colour"]= row[6]
        html["fire"]=row[9]
        html["weight"] = row[]
        html["wingspan"] = row[]
        html["summer"] = row[]
        html["winter"] = row[]
           
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
         testvar =  info_dragon(dragon)
         jsonfield = json.dumps(testvar, indent=1)
         print(jsonfield)
