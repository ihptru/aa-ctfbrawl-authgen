#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tournament Authorities file generator
# Made for an Armagetron Advanced CTF Tournament (CTF BRAWL)
# It's completely free to use
# Usage: ./scriptname.py link_to_wiki_page

import sys
import urllib.request
import re

def usage():
    print("Usage:\t"+sys.argv[0]+" link_to_wiki_page\nEx:\t"+sys.argv[0]+" http://wiki.armagetronad.org/index.php?title=CTF_BRAWL")

def parse(url):
    try:
        data = urllib.request.urlopen(url).read().decode('utf-8')
    except:
        print("url seems being incorrect")
        exit()
    content = ""
    tournament = re.findall("The <font.*\"><b>(.*)</b></font> will be played on .*, (.*).*, (.*)!<br />", data)
    content += "# "+tournament[0][0]+" | "+tournament[0][1]+", "+tournament[0][2]+"\n\n"    #ex: CTF BRAWL 14 | March 10th, 2012

    content += "#### team leaders ####\n"
    leaders = re.findall("<span.*>\((.*)\)</span><span", data)
    for record in leaders:
        team = record.split(",")
        for t in team:
            content += "USER_LEVEL " + t.strip() + " 7\n"
        content += "\n"

    content += "#### admins ####\n"
    admins = re.findall(".*<.*>\((.*)\)</span.*", data.split('id="Admins"')[1].split('id="Super_Leaders"')[0])
    for admin in admins:
        content += "USER_LEVEL " + admin + " 1\n"
    content += "\n"

    content += "#### super leaders ####\n"
    superleaders = re.findall(".*<.*>\((.*)\)</span.*", data.split('id="Super_Leaders"')[1].split('id="Brackets"')[0])
    for superleader in superleaders:
        content += "USER_LEVEL " + superleader + " 7\n"
    content += "\n"

    print(content)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        parse(sys.argv[1])
    else:
        usage()
        exit()
