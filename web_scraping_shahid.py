#!/bin/env python
from typing import Text
from bs4 import BeautifulSoup
import ssl
from time import sleep
import urllib3
import getpass
import requests
import math
import re
import subprocess
import smtplib
import sys
#sys.setdefaultencoding('utf8')
from lxml.etree import tostring
import os
###################################################
print(r'''  _____   _   _   _   _    _   _   _____   
/  ___| | | | | | | / /  | | | | |  _  \  
| |     | | | | | |/ /   | | | | | |_| |  
| |     | | | | | |\ \   | | | | |  _  /  
| |___  | |_| | | | \ \  | |_| | | | \ \  
\_____| \_____/ |_|  \_\ \_____/ |_|  \_\ #Angelous# ''')
print('\n##########################################')
print('\n* Copyright of Angelous in 2021 *')
print('\n* Yemen shield organization     *')
print('\n##########################################')
print('\n want you serach pleases use the link : https://m.shahed4u.dev/?s=')
###################################################
Link_Website = input('Enter link website : ')
r = requests.session()
result = r.get(Link_Website)
src = result.content
soup = BeautifulSoup (src , 'lxml')
#print (soup)
#####################################################
links = []
name  = []
#####################################################
for first_links in soup.find_all('div' ,{'class': 'content-box'}):
    links_films = first_links.find('a')
    films_names = links_films['title']
    films_links = links_films['href']
    #print(films_names)
    links.append(films_links)
    name.append(films_names)
######################################################
def finally_link(s):
    soup = BeautifulSoup (s.content , 'lxml')
    elemet= soup.find_all('div' , {'class':'col-12'})
    server = elemet[1].find("iframe")['src']
    print ('\n[+] is link the film : ')
    print(server)
#####################################################
def get_watch(s):
    soup = BeautifulSoup(s.content , 'lxml')
    #print(soup)
    for watch_film in soup.find_all('div' , {'class' : 'btns'}):
        view_now = watch_film.find('a')
        now_view = view_now['href']
        #print(now_view)
    s = r.get(now_view)
    finally_link(s)
#####################################################
#for x in links:
#    s = r.get(x)
#    get_watch(s)
#####################################################

for num, name in enumerate(name):
    print (str(num).ljust(5)  + str(name)) 
choice = input('\n[+] please enter movie number : ')
mvname = int(choice)
s = r.get(links[mvname])
get_watch(s)

