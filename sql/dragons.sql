DROP TABLE DRAGONS;

CREATE TABLE DRAGONS
(DRAGON_ID NUMBER(2),
NAME VARCHAR2(25),
REGION_ID NUMBER(2),
TYPE_ID NUMBER(2),
MIGRATION_ID NUMBER(2),
PRIMARY KEY (DRAGON_ID,NAME));
REM FOREIGN KEY (REGION_ID) REFERENCES REGION(REGION_ID),
REM FOREIGN KEY (TYPE_ID) REFERENCES DRAGON_TYPE(TYPE_ID),
REM FOREIGN KEY (MIGRATION_ID) REFERENCES MIGRATION(MIGRATION_ID));

grant select,update,insert,delete on DRAGONS to s1234874, s1676540;
