LOAD DATA
INFILE 
dragontypes.csv
REPLACE
INTO TABLE 
s1217815.DRAGONS
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(DRAGON_ID, NAME, REGION_ID, TYPE_ID, MIGRATION_ID)