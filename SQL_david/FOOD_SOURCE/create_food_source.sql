DROP TABLE FOOD_SOURCE;

CREATE TABLE FOOD_SOURCE
(FOOD_SOURCE_ID NUMBER(2),
FOOD_TYPE NUMBER(2),
LOCATION MDSYS.SDO_GEOMETRY,
PRIMARY KEY (FOOD_SOURCE_ID),
FOREIGN KEY (FOOD_TYPE) REFERENCES s1217815.FOOD_TYPE(FOOD_TYPE_ID));

GRANT SELECT,UPDATE,INSERT,DELETE ON FOOD_SOURCE TO s1217815,s1676540;