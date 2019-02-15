#!/usr/bin/env python3
import cgitb
import cx_Oracle
import folium
import json

cgitb.enable(format='text')
from jinja2 import Environment, FileSystemLoader


#rendering the template
def print_html():
    env = Environment(loader=FileSystemLoader('.'))
    temp = env.get_template('/Templates/dragon_mainpage.html')
    name = "Welcome to Dragons & Where To Find Them"
    print(temp.render(data=json.dumps(name)))

if __name__ == '__main__':
    print_html()
