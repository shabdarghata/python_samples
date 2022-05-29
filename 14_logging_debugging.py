#To debug in command line -> python3 -pdb 14_logging_debugging.py
#On pdb prompt, 
# list is to list code with line numbers
# n is go to next line, 
# s is step through 
# break <line number> is to add a break point. Just break without line number is to list all break points.
# c is continue until next breakpoint
# p <variable> is print variable value
# q is quit

import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO,format="%(asctime)s:%(levelname)s->%(message)s")
x=1
y=2
z=x+y
logging.info("x={} y={} z={}".format(x,y,z))
