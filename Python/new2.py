#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
cgitb.enable()

def add_dragon(newX, newY, newID):
    '''allow user to add a dragon siting'''
    with open("/web/s1676540/webmappwd", 'r') as pwf:
        pwd = pwf.read().strip()
   
    conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    c = conn.cursor()
    query = "INSERT INTO S1676540.NEWDRAGON VALUES (" + str(newID) + ", SDO_GEOMETRY(2001, 8307, SDO_POINT_TYPE(" +newX + "," + newY +", NULL), NULL, NULL))"
    c.execute(query)
   
    conn.close()


if __name__ == '__main__':
    #allows retrieval of the values input in the html form
     form = cgi.FieldStorage()
     print("Content-Type: application/json")
     print("\n")

     #if the form is filled out, get the numbers and call the function to add
     if "newX" in form:
         newX=form['newX'].value
     if "newY" in form:
         newY=form['newY'].value
     if "newID"in form:
         newID =form['newID'].value
     #newX = '1'
     #newY = '1'
     #newID = '1'
     testvar = add_dragon(newX, newY, newID)

