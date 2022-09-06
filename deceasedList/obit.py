#!/usr/bin/python3
# Build Obtiaries Page for esyray.com
# Created: 2017-12-19

import os
import sys
import time
import datetime
from datetime import date
import calendar
import shutil

###############################################
#### LOGGING CLASS SETTINGS (py25+, py30+) ####
###############################################
#### also will work with py23, py24 without 'encoding' arg
#
# Change bewteen INFO and DEBUG 2 places to change between logging levels
#
import logging
import logging.handlers
f = logging.Formatter(fmt='%(levelname)s:%(name)s: %(message)s '
    '(%(asctime)s; %(filename)s:%(lineno)d)',
    datefmt="%Y-%m-%d %H:%M:%S")
handlers = [
    logging.handlers.RotatingFileHandler('rotated.log', encoding='utf8',
        maxBytes=100000, backupCount=1),
    logging.StreamHandler()
]
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
for h in handlers:
    pass
    h.setFormatter(f)
    h.setLevel(logging.DEBUG)
    root_logger.addHandler(h)
##############################
#### END LOGGING SETTINGS ####
##############################

##############################################################

os.system("clear")

def buildObitEntry(obitInfo):
    logging.debug("buildObitEntry.obitInfo: %s", obitInfo[2])
    obitOut.write("<tr>\n")
    obitLine = "<td>" + obitInfo[0] + "</td>\n"
    obitOut.write(obitLine)
    obitLine = "<td>" + obitInfo[1] + "</td>\n"
    obitOut.write(obitLine)
    obitLine = "<td><a href=\"" + obitInfo[2] + "\">" + obitInfo[2] + "</a></td>\n"
    obitOut.write(obitLine)
    obitOut.write("</tr>\n")
    return

logging.debug( "****Starting***")
obitIn = open('./Deaths - Deceased.tsv','r')
obitOut = open('./obit.html','w')

for line in obitIn:
    obitInParsed = line.split("\t")
#    print(line)
    if("http" in obitInParsed[2]):
#        logging.debug("***** Main: Found Obit *********")
        buildObitEntry(obitInParsed)
obitIn.close()
obitOut.close()
logging.debug("***The end***")
