INSERT INTO USER_SDO_GEOM_METADATA
  (TABLE_NAME,
    COLUMN_NAME,
    DIMINFO,
    SRID)
  VALUES (
  'S1217815.FOOD_SOURCE',
  'LOCATION',
  SDO_DIM_ARRAY(
    SDO_DIM_ELEMENT('X', -180.0, 180.0, 0.00000005),
    SDO_DIM_ELEMENT('Y', -90.0, 90.0, 0.00000005)),
  8307
  );

INSERT INTO USER_SDO_GEOM_METADATA
  (TABLE_NAME,
    COLUMN_NAME,
    DIMINFO,
    SRID)
  VALUES (
    'S1217815.MIGRATION',
    'ROUTE',
    SDO_DIM_ARRAY(
      SDO_DIM_ELEMENT('LONG', -180.0, 180.0, 0.5),
      SDO_DIM_ELEMENT('LAT', -90.0, 90.0, 0.5)),
    8307
  );

INSERT INTO USER_SDO_GEOM_METADATA
  (TABLE_NAME,
    COLUMN_NAME,
    DIMINFO,
    SRID)
  VALUES (
    'S1217815.REGION',
    'AREA',
    SDO_DIM_ARRAY(
      SDO_DIM_ELEMENT('X', -180.0, 180.0, 0.5),
      SDO_DIM_ELEMENT('Y', -90.0, 90.0, 0.5)),
    8307
  );

INSERT INTO USER_SDO_GEOM_METADATA
  (TABLE_NAME,
    COLUMN_NAME,
    DIMINFO,
    SRID)
  VALUES (
    'S1217815.SETTLEMENTS',
    'LOCATION',
    SDO_DIM_ARRAY(
      SDO_DIM_ELEMENT('X', -180.0, 180.0, 0.5),
      SDO_DIM_ELEMENT('Y', -90.0, 90.0, 0.5)),
    8307
  );



CREATE INDEX MIGRATION_IDX
ON S1217815.MIGRATION(ROUTE)
INDEXTYPE IS MDSYS.SPATIAL_INDEX;

CREATE INDEX REGION_IDX
ON S1217815.REGION(AREA)
INDEXTYPE IS MDSYS.SPATIAL_INDEX;

CREATE INDEX SETTLEMENT_IDX
ON S1217815.SETTLEMENTS(LOCATION)
INDEXTYPE IS MDSYS.SPATIAL_INDEX;

CREATE INDEX FOODSOURCE_IDX
ON S1217815.FOOD_SOURCE(LOCATION)
INDEXTYPE IS MDSYS.SPATIAL_INDEX;
