#Sample code snippets for working with psycopg

import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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

#Create a Table
#The first step is to create a cursor. 

cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Company; ''')
cur.execute('''DROP TABLE IF EXISTS  Chemical; ''')
cur.execute('''DROP TABLE IF EXISTS  Chemical_Usage; ''')
cur.execute('''DROP TABLE IF EXISTS  Local_Water_Body; ''')
cur.execute('''DROP TABLE IF EXISTS  Water_Body; ''')
cur.execute('''DROP TABLE IF EXISTS  Local_Earthquake; ''')
cur.execute('''DROP TABLE IF EXISTS  Earthquake_History; ''')
cur.execute('''DROP TABLE IF EXISTS  Well_Site; ''')
cur.execute('''DROP TABLE IF EXISTS  State; ''')

cur.execute('''CREATE TABLE Chemical
            (
	           CAS_No               VARCHAR(50) NOT NULL,
	           Chemical_Name        VARCHAR(255) NULL,
	           PRIMARY KEY (CAS_No)
            );''')

cur.execute('''CREATE TABLE Chemical_Usage
                (
	               Well_Id              VARCHAR(50) NOT NULL,
	               Ingredient           VARCHAR(255) NOT NULL,
	               Trade_Name           VARCHAR(255) NOT NULL,
	               CAS_No               VARCHAR(50) NOT NULL,
	               Company_Id           VARCHAR(255) NULL,
	               conc_in_Additive     double precision NULL,
	               conc_in_HFF          double precision NULL,
	               PRIMARY KEY (Well_Id,Ingredient,Trade_Name, conc_in_HFF)
                );''')

cur.execute('''CREATE TABLE Company
                (
	               Company_Id           VARCHAR(50) NOT NULL,
	               Company_Name         VARCHAR(255) NULL,
	               PRIMARY KEY (Company_Id)
                ); ''')

cur.execute('''CREATE TABLE Earthquake_History
                (
	               Quake_Id             INTEGER NOT NULL,
	               Quake_Datetime       DATE NULL,
	               Magnitude            VARCHAR(255) NULL,
	               Latitude             VARCHAR(255) NULL,
	               Longitude            VARCHAR(255) NULL,
	               State_Code           VARCHAR(2) NULL,
	               PRIMARY KEY (Quake_Id)
                ); ''')
            
cur.execute('''CREATE TABLE Local_Earthquake
                (
	               Well_Id              VARCHAR(255) NOT NULL,
	               Quake_Id             INTEGER NOT NULL,
	               Distance             NUMERIC(6,2) NULL,
	               PRIMARY KEY (Well_Id,Quake_Id)
                ); ''')
            
cur.execute('''CREATE TABLE Local_Water_Body
                (
	               Water_Body_Id        VARCHAR(50) NOT NULL,
	               Well_Id              VARCHAR(50) NOT NULL,
	               Distance             NUMERIC(6,2) NULL,
	               PRIMARY KEY (Water_Body_Id,Well_Id)
                   ); ''')

cur.execute('''CREATE TABLE State
                (       
	               State_Code           VARCHAR(2) NOT NULL,
	               State_Name           VARCHAR(255) NULL,
	               PRIMARY KEY (State_Code)
                ); ''')

cur.execute('''CREATE TABLE Water_Body
                (
	               Water_Body_Id        VARCHAR(50) NOT NULL,
	               Water_Body_Name      VARCHAR(255) NULL,
	               Latitude             VARCHAR(255) NULL,
	               Longitude            VARCHAR(255) NULL,
	               State_Code           VARCHAR(2) NULL,
	               PRIMARY KEY (Water_Body_Id)
                ); ''')

cur.execute('''CREATE TABLE Well_Site
                (
	               Well_Id              VARCHAR(50) NOT NULL,
	               API_No               VARCHAR(255) NULL,
	               State_Code           VARCHAR(2) NULL,
	               County_No            VARCHAR(255) NULL,
	               Well_Name            VARCHAR(255) NULL,
	               Operator_Name        VARCHAR(255) NULL,
	               Latitude             VARCHAR(255) NULL,
	               Longitude            VARCHAR(255) NULL,
	               Projection           VARCHAR(255) NULL,
	               tot_Base_Water_vol   double precision NULL,
	               tot_Base_Non_Water_vol double precision NULL,
	               Start_Date           DATE NULL,
	               End_Date             DATE NULL,
	               PRIMARY KEY (Well_Id)
                ); ''')

cur.execute('''DROP TABLE IF EXISTS well_site_stage; ''')

dfmeta = pd.read_excel('fracfocus.xlsx',sheetname='2017metadata')

dfmeta.columns = [c.lower() for c in dfmeta.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:pass@localhost:5432/frackdb')

dfmeta.to_sql("well_site_stage", engine)

cur.execute('''DROP TABLE IF EXISTS chemical_usage_stage; ''')

dfusage = pd.read_excel('fracfocus.xlsx',sheetname='2017')

dfusage.columns = [c.lower() for c in dfusage.columns] #postgres doesn't like capitals or spaces

dfusage.to_sql("chemical_usage_stage", engine)

#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query, 
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows. 

cur = conn.cursor()

#Insert
cur.execute("INSERT INTO well_site (Well_Id,API_No,State_Code,County_No, \
	                                Well_Name, Operator_Name, Latitude, \
                                    Longitude,Projection,tot_Base_Water_vol,\
	                                tot_Base_Non_Water_vol,Start_Date,End_Date) \
             SELECT \"unique well identifier\", \"api number\", \"state\", \"county\", \"well name\", \"operator clean\",  \"latitude\", \"longitude\", \"lat/long projection\", \"water in gallons\", \"tvd\", \"start date\", \"end date\" \
              FROM well_site_stage");

conn.commit()

cur.execute("INSERT INTO chemical_usage (Well_Id,ingredient, trade_name, \
                                               cas_no, company_id,conc_in_additive, \
                                               conc_in_hff) \
             SELECT \"unique well identifier\", \"ingredient\", \"trade name\", \"cas/hmirc\", \"supplier\", \
             CAST(\"concentration in additive\" AS double precision),\
             CAST(\"concentration in hff\" AS double precision) \
             FROM chemical_usage_stage");

#cur.execute("INSERT INTO chemical_usage () \
#             SELECT  ");

conn.commit()

conn.close()

