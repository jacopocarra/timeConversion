# timeConversion
In UTCUT1.py the difference of seconds to transform time from UTC to UT1 is computed. It wants the julian day and the fractional julian day as input.
It downloads automatically the table of the daily difference between UTC and UT1 from "https://maia.usno.navy.mil/ser7/finals2000A.daily" and reads through it to find the julian day it is and find the associated difference of seconds.
In UTCGPS.py the difference of seconds to transform time from UTC to GPS is computed. It wants jd as sum of the julian day and fractional julian day as input.
It downloads automatically the table of leap seconds from "https://maia.usno.navy.mil/ser7/tai-utc.dat" and finds the leap seconds to be added to UTC in order to have GPS time.
# Example UTCUT1
~~~
jd = 2459917.5
fr = 0.53197969
diff = convFromUTCtoUT1(jd, fr)
diff = -0.0208342
~~~
# Example UTCGPS
~~~
jd = 2459917.5
fr = 0.53197969
jd = jd+fr
diff = convFromUTCtoGPS(jd)
diff = 18
~~~
