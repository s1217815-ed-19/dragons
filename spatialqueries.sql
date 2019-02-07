--intersect migration routes
DECLARE @VARROUTE
SELECT
@VARROUTE = ROUTE
FROM S1217815.MIGRATION
WHERE MIGRATION_ID = PYTHONVAR;

SELECT SDO_GEOM.SDO_INTERSECTION(VARROUTE,
(SELECT ROUTE FROM S1217815.MIGRATION),.005);


DECLARE @N TABLE(
C int,
D SDO_GEOMETRY)
INSERT INTO @N (C, D)
SELECT MIGRATION_ID, ROUTE
FROM S1217815.MIGRATION
WHERE MIGRATION_ID = PYTHONVARIABLE
SELECT A.MIGRATION_ID, A.NAME
FROM S1217815.MIGRATION A, @N B
WHERE SDO_RELATE(A.ROUTE, B.D, 'MASK = OVERLAPBDYDISJOINT') = 'TRUE'
AND A.MIGRATION_ID = VARIABLE;


DEF ROUTE2 = PYTHONVVV
SELECT A.MIGRATION_ID, A.NAME,
SDO_GEOM.RELATE(A.ROUTE, &ROUTE2, 'MASK = OVERLAPBDYDISJOINT') = 'TRUE'
FROM S1217815.MIGRATION A
WHERE A.MIGRATION_ID = VARIABLE;
UNDEFINE ROUTE2

--migration and region intersect
SELECT SDO_GEOM.SDO_INTERSECTION(A.ROUTE,B.SHAPE,.005)
FROM S1234784.MIGRATION A, S1234784.REGION B
WHERE A.MIGRATION_ID = VAR1 AND B.REGION_ID = VAR2;

SELECT A.MIGRATION_ID, B.REGION_ID
FROM S1234874.MIGRATION A, S1234874.REGION B
WHERE SDO_RELATE(A.ROUTE, B.SHAPE, 'MASK = OVERLAPBYDISJOINT') = 'TRUE'
AND A.MIGRATION_ID = 3 AND B.REGION_ID = 3;

--distance between settlements and food sources
SELECT SDO_GEOM.SDO_DISTANCE(A.LOCATION, B.LOCATION, .005)
FROM S1217815.SETTLEMENTS A, S1217815.FOODSOURCE B
WHERE A.SETTLEMENT_ID = VAR1 AND B.SOURCE_ID = VAR2;


-- distance between two habitats
DECLARE @HAB1 SDO_GEOMETRY
SELECT
@HAB1 = AREA
FROM S1217815.MIGRATION
WHERE MIGRATION_ID = PYTHONVAR1;
DECLARE @HAB2 SDO_GEOMETRY
SELECT
@HAB2 = AREA
FROM S1217815.MIGRATION
WHERE MIGRATION_ID = PYTHONVAR2;
SELECT SDO_GEOM.SDO_DISTANCE(@HAB1, @HAB2, .005) FROM S1217815.REGION;

--is a settlement in a region?
SELECT A.REGION_ID, A.NAME, B.SETTLEMENT_ID, B.NAME
FROM S1234784.REGION A, S1234784.SETTLEMENTS B
WHERE SDO_CONTAINS(A.AREA, B.LOCATION) = 'TRUE'
AND B.SETTLEMENT_ID = VARC;

-- is a food source within a region
SELECT A.REGION_ID, A.NAME, B.SOURCE_ID
FROM S1234784.REGION A, S1234784.FOOD_SOURCE B
WHERE SDO_CONTAINS(A.AREA, B.LOCATION) = 'TRUE'
AND B.SOURCE_ID = VARE;


SELECT A.NAME, B.NAME
FROM REGION A, REGION B
WHERE A.NAME = 'Hungary' AND B.NAME = 'Romania';

SELECT A.NAME, B.NAME
FROM MIGRATION A, MIGRATION B
WHERE A.MIGRATION_ID = PYVAR AND SDO_RELATE(A.ROUTE, B.ROUTE, 'MASK = OVERLAPBDYDISJOINT') = 'TRUE';

1234874 david is awesome
region
settlements

--user in region
SELECT A.REGION_ID, A.NAME
FROM S1234874.REGION A
WHERE SDO_CONTAINS(A.SHAPE,
SDO_GEOMETRY(2001, 8307, SDO_POINT_TYPE(-133,62, NULL), NULL, NULL)) = 'TRUE';
