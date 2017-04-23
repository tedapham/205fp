#Sample code snippets for working with psycopg

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import csv
import sys

# Connect to the database
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Create the Database

try:
    # CREATE DATABASE can't run inside a transaction
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS  frackdb")
    cur.execute("CREATE DATABASE frackdb")
    cur.close()
    conn.close()
except:
    print "Could not create frackdb"

#Connecting to tcount

conn = psycopg2.connect(database="frackdb", user="postgres", password="pass", host="localhost", port="5432")


if len(sys.argv) > 1:
    instab = sys.argv[1]
else:
    instab = 'All'

#Create a Table
#The first step is to create a cursor. 

cur = conn.cursor()

if (instab == 'All' or instab == 'State'):
    ##--------------State-------------------
    cur.execute('''DROP TABLE IF EXISTS  State_Stage; ''')
    cur.execute('''DROP TABLE IF EXISTS  State; ''')
    cur.execute('''CREATE TABLE State_Stage
                    (       
                       State_Code           VARCHAR(2) NOT NULL,
                       State_Name           VARCHAR(255) NULL
                    ); ''')

    conn.commit()

    cur.execute('''CREATE TABLE State
                    (       
                       State_Code           VARCHAR(2) NOT NULL,
                       State_Name           VARCHAR(255) NULL,
                       PRIMARY KEY (State_Code)
                    ); ''')

    conn.commit()

if( instab == 'All' or instab == 'County'):
    ##--------------County-------------------
    
    cur.execute('''DROP TABLE IF EXISTS  County_stage; ''')
    cur.execute('''DROP TABLE IF EXISTS  County; ''')

    cur.execute('''CREATE TABLE County_Stage
                    (
                        County_Name          VARCHAR(255) NULL,
                        State_Code           VARCHAR(2) NULL
                    );''')

    conn.commit()

    cur.execute('''CREATE TABLE County
                    (
                        County_no            INTEGER NOT NULL,
                        County_Name          VARCHAR(255) NULL,
                        State_Code           VARCHAR(2) NULL,
                        PRIMARY KEY (County_no)
                    );''')

    conn.commit()

if (instab == 'All' or instab == 'Chemical_Toxicity'):
    ##---------------------Chemical Toxicity-----------------------
    cur.execute('''DROP TABLE IF EXISTS  Chemical_Toxicity_Stage; ''')
    cur.execute('''DROP TABLE IF EXISTS  Chemical_Toxicity; ''')
    cur.execute('''CREATE TABLE Chemical_Toxicity_Stage
                    (
                        CAS_No               VARCHAR(255) NOT NULL,
                        TOXICITY             VARCHAR(255) NULL,
                        Chemical_Name        VARCHAR(255) NULL,
                        Substance_Type       VARCHAR(255) NULL,
                        Substance_Note       VARCHAR(255) NULL,
                        Chemical_Formula     VARCHAR(255) NULL,
                        Mol_Weight           VARCHAR(255) NULL
                    );''')

    conn.commit()

    cur.execute('''CREATE TABLE Chemical_Toxicity
                    (
                        CAS_No               VARCHAR(50) NOT NULL,
                        TOXICITY             VARCHAR(255) NULL,
                        Chemical_Name        VARCHAR(255) NULL,
                        Substance_Type       VARCHAR(255) NULL,
                        Substance_Note       VARCHAR(255) NULL,
                        Chemical_Formula     VARCHAR(255) NULL,
                        Mol_Weight           FLOAT NULL
                    );''')

    conn.commit()

if (instab == 'All' or instab == 'Chemical_Usage'):
##--------------Chemical Usage-------------------
    cur.execute('''DROP TABLE IF EXISTS  Chemical_Usage_Stage; ''')
    cur.execute('''DROP TABLE IF EXISTS  Chemical_Usage; ''')
    cur.execute('''CREATE TABLE Chemical_Usage_Stage
                    (
                        api_no                  VARCHAR(255), 
                        Well_Name               VARCHAR(255), 
                        Latitude                VARCHAR(255), 
                        Longitude               VARCHAR(255), 
                        Projection              VARCHAR(255),
                        State_No                VARCHAR(255),
                        State_Name              VARCHAR(255), 
                        County_No               VARCHAR(255), 
                        County_Name             VARCHAR(255),
                        Operator_Name           VARCHAR(255), 
                        Start_Date              VARCHAR(255), 
                        End_Date                VARCHAR(255), 
                        TradeName               VARCHAR(255), 
                        Supplier                VARCHAR(255),
                        CAS_No                  VARCHAR(255), 
                        IngredientName          VARCHAR(255), 
                        Tot_Base_Water_Vol      VARCHAR(255),
                        Tot_Base_Non_Water_Vol  VARCHAR(255),
                        pct_HighAdditive        VARCHAR(255), 
                        pct_HFJob               VARCHAR(255)
                        );''')

    conn.commit()

    cur.execute('''CREATE TABLE Chemical_Usage
                    (
                        Well_Id              INTEGER NOT NULL,
                        Ingredient           VARCHAR(255) ,
                        Trade_Name           VARCHAR(255) ,
                        End_Date             VARCHAR(255) ,
                        CAS_No               VARCHAR(255) ,
                        Supplier             VARCHAR(255) ,
                        conc_in_Additive     VARCHAR(255) ,
                        conc_in_HFF          VARCHAR(255) ,
                        tot_Base_Water_vol   VARCHAR(255) ,
                        tot_Base_Non_Water_vol VARCHAR(255) ,
                        Start_Date          VARCHAR(255)
                        );''')

    conn.commit()


if (instab == 'All' or instab == 'Earthquake_History'):
##-------------------------Earthquake-------------------
    cur.execute('''DROP TABLE IF EXISTS  Local_Earthquake; ''')
    cur.execute('''DROP TABLE IF EXISTS  Earthquake_History_stage; ''')
    cur.execute('''DROP TABLE IF EXISTS  Earthquake_History; ''')
    ##Place holder for Earthquake_History_Stage - Ted Pham
    cur.execute('''CREATE TABLE Earthquake_History_Stage
                    (
                        Quake_Id             VARCHAR(255) NOT NULL,
                        Quake_Datetime       VARCHAR(255) NULL,
                        Latitude             VARCHAR(255) NULL,
                        Longitude            VARCHAR(255) NULL,
                        Depth                VARCHAR(255) NULL,
                        Magnitude            VARCHAR(255) NULL,
                        Event_Type           VARCHAR(255) NULL,
                        State                VARCHAR(5) NULL,
                        County               VARCHAR(255) NULL,
                        PRIMARY KEY (Quake_Id)
                    );''')

    conn.commit()

    cur.execute('''CREATE TABLE Earthquake_History
                    (
                        Quake_Id             INTEGER NOT NULL,
                        Quake_Datetime       DATE NULL,
                        Magnitude            FLOAT NULL,
                        Latitude             VARCHAR(255) NULL,
                        Longitude            VARCHAR(255) NULL,
                        State_Code           VARCHAR(2) NULL,
                        PRIMARY KEY (Quake_Id)
                    );''')

    conn.commit()

    cur.execute('''CREATE TABLE Local_Earthquake
                    (
                        Well_Id              INTEGER NOT NULL,
                        Quake_Id             INTEGER NOT NULL,
                        Distance             FLOAT NULL,
                        PRIMARY KEY (Well_Id,Quake_Id)
                    ); ''')

    conn.commit()


##-------------------------Water Body-------------------

##Place holder for Water_Body_Stage - Alex Yang
if (instab == 'All' or instab == 'Water_Body'):
    cur.execute('''DROP TABLE IF EXISTS  Local_Water_Body; ''')
    cur.execute('''DROP TABLE IF EXISTS  Water_Body_stage; ''')
    cur.execute('''DROP TABLE IF EXISTS  Water_Body; ''')
    cur.execute('''CREATE TABLE Water_Body_Stage
                (
                    Water_Body_Id        VARCHAR(255) NOT NULL,
                    Station_Name         VARCHAR(255) NULL,
                    Latitude             VARCHAR(255) NULL,
                    Longitude            VARCHAR(255) NULL,
                    coord_datum          VARCHAR(8),
                    drain_area_va        VARCHAR(255) NULL,
                    aquifier_cd          VARCHAR(255) NULL,
                    well_depth           VARCHAR(255) NULL,
                    site_type            text NULL,
                    State                VARCHAR(2) NULL,
                    County               VARCHAR(255) NULL,
                    Size                 VARCHAR(2) NULL
                ); ''')
    
    cur.execute('''CREATE TABLE Local_Water_Body
                    (
                        Water_Body_Id        INTEGER NOT NULL,
                        Well_Id              INTEGER NOT NULL,
                        Distance             FLOAT NULL,
                        PRIMARY KEY (Water_Body_Id,Well_Id)
                    );''')

    conn.commit()

    cur.execute('''CREATE TABLE Water_Body
                    (
                        Water_Body_Id        INTEGER NOT NULL,
                        Water_Body_Name      VARCHAR(255) NULL,
                        Latitude             VARCHAR(255) NULL,
                        Longitude            VARCHAR(255) NULL,
                        State_Code           VARCHAR(2) NULL,
                        PRIMARY KEY (Water_Body_Id)
                    ); ''')

    conn.commit()

if (instab == 'All' or instab == 'Well_Site'):
    ##----------------------Well Site -----------------------------
    cur.execute('''DROP TABLE IF EXISTS  Well_Site_Stage; ''')
    cur.execute('''DROP TABLE IF EXISTS  Well_Site; ''')
    cur.execute('''CREATE TABLE Well_Site_Stage
                    (
                        Well_Id              VARCHAR(255) NULL,
                        API_no               VARCHAR(255) NULL,
                        Well_Name            VARCHAR(255) NULL,
                        Operator_Name        VARCHAR(255) NULL,
                        Latitude             VARCHAR(255) NULL,
                        Longitude            VARCHAR(255) NULL,
                        Projection           VARCHAR(255) NULL,
                        State_No             INTEGER NULL,
                        State_Name           VARCHAR(255) NULL,
                        County_no            INTEGER NULL,
                        County_Name          VARCHAR(255) NULL
                    );''')

    conn.commit()

    cur.execute('''CREATE TABLE Well_Site
                    (
                        Well_Id              INTEGER NOT NULL,
                        API_no               VARCHAR(255) NULL,
                        Well_Name            VARCHAR(255) NULL,
                        Operator_Name        VARCHAR(255) NULL,
                        Latitude             VARCHAR(255) NULL,
                        Longitude            VARCHAR(255) NULL,
                        Projection           VARCHAR(255) NULL,
                        County_no            INTEGER NULL,
                        PRIMARY KEY (Well_Id)
                    );''')

    conn.commit()

##-----------------Load Staging Tables-----------------------
##----------------Load State Stage ------------------------
if (instab == 'All' or instab == 'State'):
    csv_state = csv.reader(file('state.csv'))

    print('Populating States ....')
    for row in csv_state:
        cur.execute("INSERT into state_stage (state_code, state_name) VALUES \
                    (%s, %s);", (row[0], row[1]))
        conn.commit()

##----------------Load County Stage ------------------------
if (instab == 'All' or instab == 'County'):
    csv_county = csv.reader(file('county_state.csv'))

    print('Populating Counties ....')
    for row in csv_county:
        cur.execute("INSERT into county_stage (state_code, county_name) VALUES \
                    (%s, %s);", (row[0], row[1]))
        conn.commit()

##----------------Load Well Site Stage ------------------------
if (instab == 'All' or instab == 'Well_Site'):
    csv_wellsite = csv.reader(file('well_site.csv'))

    print('Populating Well Sites ....')
    for row in csv_wellsite:
        cur.execute("INSERT into well_site_stage (well_id, api_no, Well_Name, Latitude, \
                    Longitude, Projection, State_No,State_Name, County_No, \
                    County_Name,Operator_Name  ) VALUES \
                    (%s, %s, %s, %s,%s, %s, %s,%s, %s,%s,%s);", 
                    (row[0], row[1],row[2], row[3],row[4], row[5],row[6], row[7],row[8], row[9], row[10]))

    conn.commit()

##----------------Load Chemical Usage Stage ------------------------
if (instab == 'All' or instab == 'Chemical Usage'):
    csv_chemusage = csv.reader(file('chemical_usage.csv'))

    print('Populating Chemical Usage ....')
    for row in csv_chemusage:
        cur.execute("INSERT into chemical_usage_stage (api_no, Well_Name, Latitude, \
                    Longitude, Projection, State_No,State_Name, County_No, \
                    County_Name,Operator_Name, Start_Date, End_Date,TradeName,Supplier,\
                    CAS_No, IngredientName, Tot_Base_Water_Vol,Tot_Base_Non_Water_Vol,\
                    pct_HighAdditive, pct_HFJob  ) VALUES \
                    (%s, %s, %s,%s, %s, %s,%s, %s,%s,%s, %s, %s,%s,%s,%s, \
                    %s,%s,%s,%s,%s);", (row[0], row[1],row[2], row[3],row[4], row[5],row[6], row[7],row[8], row[9],row[10], row[11],row[12], row[13],row[14], row[15],row[16], row[17],row[18], row[19]))


    conn.commit()

##----------------Load Chemical_Toxicity_Stage -Placeholder - Alex Yang----------------------
if (instab == 'All' or instab == 'Chemical_Toxicity'):
    csv_chem_toxicity = csv.reader(file('toxcast.csv'))
    print('Populating Chemical Toxicity ....')

    for row in csv_chem_toxicity:
        cur.execute("INSERT into Chemical_toxicity_stage (CAS_no, TOXICITY, Chemical_name, \
                    Substance_type, Chemical_Formula, Mol_Weight ) VALUES \
                    (%s, %s,%s, %s, %s,%s);", (row[0], row[1],row[2], row[3],row[4], row[5] ))


##-------------------------Earthquake-------------------
if (instab == 'All' or instab == 'Earthquake_History'):
##----------------Load Earthquake_History_Stage -Placeholder - Ted Pham-------------

    csv_quake = csv.reader(file('quake_data_clean.csv'))

    print('Populating Quake History ....')
    for row in csv_quake:
        cur.execute("INSERT into Earthquake_history_Stage (Quake_Id, Quake_Datetime, Latitude, Longitude, \
                    Depth, Magnitude,Event_Type, State, County) VALUES \
                    (%s, %s, %s, %s,%s, %s, %s,%s,%s);", 
                    (row[0], row[1],row[2], row[3],row[4], row[5],row[6], row[7], row[8]))
    conn.commit()

if (instab == 'All' or instab == 'Water_Body'):
##----------------Load Water_Body_Stage -Placeholder - Alex Yang--------------------
    #csv.register_dialect('pipes', delimiter='|')
    csv_water_sites = csv.reader(file('water_data.csv'))
    #csv_water_sites = csv.reader(file('water_data.csv'), dialect='pipes')

    print('Populating water sites ....')
    for row in csv_water_sites:
        cur.execute("INSERT into Water_Body_Stage (Water_Body_Id, \
                    Latitude,Longitude, \
                    coord_datum, drain_area_va, aquifier_cd, well_depth,\
                     State, County, Size) VALUES \
             (%s,  %s,%s, %s,%s, %s,%s,%s, %s,%s, %s);" % (row[0], row[2], row[3],row[4], 
             row[5],row[6], row[7],row[8], row[9],row[10], row[11]))
    conn.commit()

print('Completed creation and load of staging tables')
conn.close()


