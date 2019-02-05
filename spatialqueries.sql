SELECT SDO_GEOM.SDO_INTERSECTION(VARROUTE,
(SELECT ROUTE FROM S1217815.MIGRATION),.005) FROM S1217815.MIGRATION;

SELECT A.MIGRATION_ID, A.NAME
FROM S1217815.MIGRATION A
WHERE SDO_RELATE(A.ROUTE, A.ROUTE, MASK = OVERLAPBDYDISJOINT) = 'TRUE';

SELECT SDO_GEOM.SDO_INTERSECTION(ROUTE,HABITAT,.005) FROM S1217815.MIGRATION, S1217815.REGION;

SELECT A.MIGRATION_ID, A.NAME, B.REGION_ID, B.NAME
FROM S1217815.MIGRATION A, S1217815.REGION B
WHERE SDO_RELATE(A.ROUTE, B.LOCATION, MASK = OVERLAPBDYDISJOINT) = 'TRUE';

SELECT SDO_GEOM.SDO_DISTANCE(SETTLEMENT, FOODSOURCE, .005) FROM S1217815.SETTLEMENTS, S1217815.FOODSOURCE;

SELECT SDO_GEOM.SDO_DISTANCE(SETTLEMENT, ROUTE, .005) FROM S1217815.SETTLEMENTS, S1217815.MIGRATION;

SELECT SDO_GEOM.SDO_DISTANCE(HABITAT1, HABITAT2, .005) FROM S1217815.REGION;

SELECT A.REGION_ID, A.NAME, B.SETTLEMENT_ID, B.NAME
FROM S1217815.REGION A, S1217815.SETTLEMENTS B
WHERE SDO_CONTAINS(A.AREA, B.LOCATION) = 'TRUE';

SELECT A.REGION_ID, A.NAME
FROM S1217815.REGION A
WHERE SDO_CONTAINS(A.AREA, VARLOC) = 'TRUE';

SELECT A.REGION_ID, A.NAME, B.FOOD_SOURCE_ID, B.NAME
FROM S1217815.REGION A, S1217815.FOOD_SOURCE B
WHERE SDO_CONTAINS(A.AREA, B.LOCATION) = 'TRUE';