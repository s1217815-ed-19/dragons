LOAD DATA
INFILE 
dragonfoodtype.csv
REPLACE
INTO TABLE 
s1217815.FOOD_TYPE
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(FOOD_TYPE_ID, CLASS)