DROP TABLE REGION_WINTER;

CREATE TABLE REGION_WINTER
(REGION_WINTER_ID NUMBER(2),
NAME VARCHAR2(25),
AREA (GEOGRAPHY),
TEMP_MAX NUMBER(4),
TEMP_MIN NUMBER (4),
PRIMARY KEY (REGION_WINTER_ID, NAME));
