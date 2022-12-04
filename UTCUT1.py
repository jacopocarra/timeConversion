import numpy as np
import requests

# input: jd (julian day) and fr(fraction of julian day)
# output: diff = difference to be sum to UTC to go from UTC to UT1

def convFromUTCtoUT1(jd, fr):
    j2000 = 2451545.0
    dataNavy = requests.get("https://maia.usno.navy.mil/ser7/finals2000A.daily", allow_redirects=True)
    open('tableConversion.dat', 'wb').write(dataNavy.content)
    with open('tableConversion.dat', 'r') as f:
        fl = 0
        while fl == 0:
            line = f.readline()[0:-1]
            JDTab = (float(line[7:15]))
            bullTab = float(line[58:68])
            jdInput = np.floor(jd+fr-2400000.5)
            if JDTab==jdInput:
                diff = bullTab
                
                fl = 1
    f.close()
    return diff
            
