import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO,format="%(asctime)s:%(levelname)s->%(message)s")
x=1
y=2
z=x+y
logging.info("x={} y={} z={}".format(x,y,z))
