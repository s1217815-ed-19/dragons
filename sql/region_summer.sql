DROP TABLE REGION;

CREATE TABLE REGION
(REGION_ID NUMBER(2) PRIMARY KEY,
NAME VARCHAR2(25),
SEASON VARCHAR2(25),
TEMP_MAX NUMBER(4),
TEMP_MIN NUMBER (4),
SHAPE SDO_GEOMETRY);

<<<<<<< HEAD
GRANT SELECT,UPDATE,INSERT,DELETE ON REGION TO s1217815, s1676540;
=======
GRANT ALL PRIVILEGES ON region to s1234874, s1676540;
>>>>>>> ca680605f41f0ecff807ff521b7acac148d32df9
