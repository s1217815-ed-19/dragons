DROP TABLE COLOUR;

CREATE TABLE COLOUR
(COLOUR_ID NUMBER(2),
COLOUR VARCHAR2(15),
PRIMARY KEY (COLOUR_ID));

GRANT SELECT, UPDATE, INSERT, DELETE ON COLOUR TO s1234874, s1676540;