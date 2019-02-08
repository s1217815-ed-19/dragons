DROP INDEX MIGRATION_IDX;
DELETE FROM USER_SDO_GEOM_METADATA;

INSERT INTO USER_SDO_GEOM_METADATA (
    TABLE_NAME, COLUMN_NAME, DIMINFO, SRID
  ) VALUES (
    'MIGRATION',
    'ROUTE',
    SDO_DIM_ARRAY(
      SDO_DIM_ELEMENT('LONG', -180.0, 180.0, 0.5),
      SDO_DIM_ELEMENT('LAT', -90.0, 90.0, 0.5)
    ),
    8307
  );


SELECT * FROM USER_SDO_GEOM_METADATA
WHERE TABLE_NAME = UPPER('MIGRATION')
AND COLUMN_NAME = UPPER('ROUTE');

CREATE INDEX migration_idx ON migration( route ) INDEXTYPE IS MDSYS.SPATIAL_INDEX;
