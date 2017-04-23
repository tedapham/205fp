

pip install git+git://github.com/usgs/neicmap.git
pip install git+git://github.com/usgs/neicio.git

pip install git+git://github.com/usgs/libcomcat.git

pip install numpy
pip install scipy
pip install pandas
pip install reverse_geocoder


# get quake data for 2013 -2016
"""
getcsv.py -b -125.0011 24.9493 -66.9326 49.5904 -s 2013-01-01 -e 2014-01-01 > 2013.csv
getcsv.py -b -125.0011 24.9493 -66.9326 49.5904 -s 2014-01-01 -e 2015-01-01 > 2014.csv
getcsv.py -b -125.0011 24.9493 -66.9326 49.5904 -s 2015-01-01 -e 2016-01-01 > 2015.csv
getcsv.py -b -125.0011 24.9493 -66.9326 49.5904 -s 2016-01-01 -e 2017-01-01 > 2016.csv
getcsv.py -b -125 24.6 -65 50 -s 2016-01-01 -e 2017-01-01 > 2016.csv
"""
# Get quake data for 2013-march 2017

getcsv.py -b -125 24.6 -65 50 -s 2014-01-01 -e 2017-04-01 > quake_data.csv


"""
# display quakedata for continental US

getcsv.py -b -125 24.6 -65 50 -s 2017-01-01 -e 2017-01-02


"""
"""
display earthquakes within certain radius of a well

getcsv.py -r lat lon radius -s 2017-01-01 -e 2017-01-02

-s start time YYYY-MM-DD
-e end time YYYY-MM-DD

"""

# display quakedata for continental US
