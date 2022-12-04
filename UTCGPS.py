import numpy as np
import requests

# jd input as jd+fr
# output: diff = difference to be sum to UTC to go from UTC to GPS


def convFromUTCtoGPS(jd):
    dataNavyGPS = requests.get("https://maia.usno.navy.mil/ser7/tai-utc.dat", allow_redirects=True)
    open('tableConversionGPS.dat', 'wb').write(dataNavyGPS.content)
    with open('tableConversionGPS.dat', 'r') as g:
        flag = 0
        counter = 0
        bullTab = np.zeros(41)
        while flag == 0:
            lines = g.readline()
            jdTab = float(lines[17:26])
            bullTab[counter] = float(lines[38:48])
            if jd<jdTab or counter>=40:
                diff = bullTab[counter]
                diffSec = diff-19
                flag = 1

            counter = counter+1
        return diffSec

