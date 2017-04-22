import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import csv
import sys

# Connect to the database
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Connecting to frackdb

conn = psycopg2.connect(database="frackdb", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor. 

cur = conn.cursor()
#This script can be run for a single table or all the tables
if len(sys.argv) > 1:
    instab = sys.argv[1]
else:
    instab = 'All'

##---------------Transformation - State Stage-----------------------------------
if(instab == 'State' or instab == 'All'):
    cur.execute("INSERT INTO state (state_code, state_name) \
                    SELECT state_code, state_name\
                      FROM state_stage");

    conn.commit()

##---------------Transformation - County Stage -----------------------------------
if(instab == 'County' or instab == 'All'):
    cur.execute("INSERT INTO county (county_no, state_code, county_name) \
             SELECT ROW_NUMBER() OVER (ORDER BY state_code, county_name),\
                    state_code, county_name \
             FROM \
             (SELECT distinct state_code, county_name\
              FROM county_stage) qry");

    conn.commit()

##---------------Transformation - Well_Site_Stage ------------------------------

if(instab == 'Well_Site' or instab == 'All'):
    cur.execute("INSERT INTO well_site (Well_Id,API_No,County_No, \
	                                Well_Name, Operator_Name, Latitude, \
                                    Longitude,Projection) \
                                    SELECT REGEXP_REPLACE(COALESCE(stg.well_id, '0'), '[^0-9]*' ,'0')::integer\
                                   ,stg.API_No,c.County_No, \
	                                stg.Well_Name, stg.Operator_Name, stg.Latitude, \
                                    stg.Longitude,stg.Projection \
              FROM well_site_stage stg \
              left outer JOIN state stn on stg.state_name = stn.state_name \
              left outer JOIN state stc on stg.state_name = stc.state_code \
              left outer JOIN  county c ON c.county_name = stg.county_name and\
              c.state_code = COALESCE(stn.state_code, stc.state_code) ");

    conn.commit()
    
##---------------Transformation - Chemical_Usage_Stage -------------------------
if(instab == 'Chemical_Usage' or instab == 'All'):
    cur.execute("SELECT state_code FROM state")

    rows = cur.fetchall()

    for row in rows:
        print('Inserting Chemical Usage for %s'%(row))
        cur.execute("INSERT INTO chemical_usage (Well_Id,ingredient, trade_name, start_date,\
             end_date,cas_no, supplier,conc_in_additive,conc_in_hff, \
             tot_base_water_vol, tot_base_non_water_vol) \
             SELECT well.Well_Id,stg.ingredientname, stg.tradename, stg.start_date, stg.end_date, stg.cas_no, stg.supplier, \
             CASE stg.pct_HighAdditive WHEN 'NULL' then 0.0\
             ELSE 8.34*cast(stg.tot_base_water_vol as double precision)*cast(stg.pct_HighAdditive as double precision)\
             END,\
             CASE stg.pct_HFJob WHEN 'NULL' then 0.0\
             ELSE 8.34*cast(stg.tot_base_water_vol as double precision)*cast(stg.pct_HFJob as double precision)\
             END,\
             CASE stg.tot_base_water_vol  WHEN 'NULL' THEN 0.0\
             ELSE cast(stg.tot_base_water_vol as double precision)\
             END,\
             CASE stg.tot_base_non_water_vol WHEN 'NULL' THEN 0.0\
             ELSE cast(stg.tot_base_non_water_vol as double precision)\
             END\
             FROM chemical_usage_stage stg\
             LEFT OUTER JOIN state sn on stg.state_name = sn.state_name and \
                              sn.state_code = '%s'\
             LEFT OUTER JOIN state sc on stg.state_name = sc.state_code \
                          and sc.state_code = '%s'\
             LEFT OUTER JOIN county c on stg.County_Name = c.county_name and c.State_Code = COALESCE(sn.state_code, sc.state_code)\
             LEFT OUTER JOIN well_site well on well.API_No = stg.API_no \
                                and well.County_No = c.County_no \
                                and well.Well_Name = stg.Well_name \
                                and well.Operator_Name = stg.Operator_Name \
                                and well.Latitude = stg.Latitude \
                                and well.Longitude = stg.Longitude \
                                and well.Projection = stg.Projection\
              WHERE well_id is not null"%(row[0], row[0]))
        rows_updated = cur.rowcount
        print('Inserted %d rows for %s'%(rows_updated, row))
        conn.commit()
        
        
##---------------Transformation - Chemical_Stage - Alex Yang-----------------------

##---------------Transformation - Earthquake_History_stage - Ted Pham -------------

##---------------Transformation - Water_Body_Stage - Alex Yang-----------------------


conn.close()
