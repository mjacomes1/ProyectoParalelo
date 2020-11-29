import requests
import time
from random import randint
for i in range(38):
    unix = randint(1,100)
    id = randint(1,2) 
    #print(unix)
    r = requests.get('http://192.168.1.13:5000/?name=\"hla'+str(id)+'\"&unix=\"'+str(unix)+'\"&date="rttrh"&symbol="bre"&open="bb"&high="brrg"&low="tbtb"&close="thrth"&volume="bbbb"')
    #r1 = requests.get('http://192.168.1.13:5000/?name=\"mcr'+str(id)+'\"&unix=\"'+str(unix)+'\"&date="rttrh"&symbol="bre"&open="bb"&high="brrg"&low="tbtb"&close="thrth"&volume="bbbb"')
