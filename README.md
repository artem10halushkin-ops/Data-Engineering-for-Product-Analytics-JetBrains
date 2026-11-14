# Data-Engineering-for-Product-Analytics-JetBrains

metadwh.py
contains the structure for our star schema tables. 
Table Facts assemlbes all the information about the technical usage of the queries by the particular user and the infomration regarding this event. 

Table User contains the import informations about some user. For sake of single source of truth we store such information not in the Facts embeeded, but in other tables like User.

Table 'Dates' stores date in format YYYY-MM-DD. The id of it is distinct and formed buy simple arithmetic operation.
For Example 2026-01-01 -> 20260101 .

Table 'Tables' is used for storing distinguishable tables accordingly.

Table HRDB simulates the database for the information regarding the personla that suppose to exist and from which we take the Team name in one of our task queries for example.


seed.py 
reprents the class for seeding of the created tables Dates for 5 years up on and the the alleged table HR database that has the information about the personal.

etl_pipeline.py
Has a functionality for the extraction, transformation and loading of the daily usage statistics to our meta data warehouse.
Method extract takes the data from the s3 datalake 



queries.sql contains two quiers for the given task that are based on my specific implementaion.
