#!/usr/bin/env python3
import cgi
import cgitb
import cx_Oracle
import json
cgitb.enable()

def TEMPLATETEMPLATE(x):
    '''get information and put it on that MAP'''

    #with open("/web/s1676540/webmappwd", 'r') as pwf:
        #pwd = pwf.read().strip()
   
    #conn = cx_Oracle.connect(dsn="geosgen", user ="s1676540", password=pwd)
    #c = conn.cursor()

    #query =

    BOB = {'field':x}

    return html

if __name__ == '__main__':
    testvar = TEMPLATETEMPLATE(1)
    BOBBY = json.dumps(BOB, indent=1)
    print(jsonfield)
    
