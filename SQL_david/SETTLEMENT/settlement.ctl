LOAD DATA
INFILE dragonsettlements.csv
BADFILE settlements.bad
REPLACE
INTO TABLE 
SETTLEMENTS
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(SETTLEMENT_ID, NAME)
