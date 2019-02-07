INSERT INTO USER_SDO_GEOM_METADATA (
    TABLE_NAME, COLUMN_NAME, DIMINFO, SRID
  ) VALUES (
    'SETTLEMENTS',
    'LOCATION',
    SDO_DIM_ARRAY(
      SDO_DIM_ELEMENT('LONG', -180.0, 180.0, 0.5),
      SDO_DIM_ELEMENT('LAT', -90.0, 90.0, 0.5)
    ),
    8307
  );


SELECT * FROM USER_SDO_GEOM_METADATA
WHERE TABLE_NAME = UPPER('SETTLEMENTS')
AND COLUMN_NAME = UPPER('LOCATION');

CREATE INDEX settlement_idx ON settlements( location ) INDEXTYPE IS MDSYS.SPATIAL_INDEX;
