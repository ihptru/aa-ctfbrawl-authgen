#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tournament Authorities file generator
# Made for an Armagetron Advanced CTF Tournament
# It's completely free to use
# Usage: ./scriptname.py link_to_wiki_page

import sys
import urllib.request
import re

def usage():
    print("Usage:\t"+sys.argv[0]+" link_to_wiki_page\nEx:\t"+sys.argv[0]+" http://wiki.armagetronad.org/index.php?title=CTFtourney")

def parse(url):
    try:
        data = urllib.request.urlopen(url).read().decode('utf-8')
    except:
        print("url seems being incorrect")
        exit()
    content = ""
    tournament = re.findall("The <font.*\">(.*)</font> will be", data)
    content += "# "+tournament[0].strip('<b>').strip('</b>')+"\n\n"

    data = re.findall("<span.*>\((.*)\)</span><span", data)
    for record in data:
        team = record.split(",")
        for t in team:
            content += "USER_LEVEL " + t.strip() + " 7\n"
        content += "\n"
    admins = input("Enter admins, all in same line, comma separated (admin@forums, admin1@forums): ")
    if admins.strip() != "":
        content += "#admins: \n"
        for admin in admins.split(","):
            content += "USER_LEVEL " + admin.strip() + " 1\n"

    print(content)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        parse(sys.argv[1])
    else:
        usage()
        exit()
