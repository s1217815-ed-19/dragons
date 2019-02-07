/*Distance between two settlements (points), result in metres*/
SElECT SDO_GEOM.SDO_DISTANCE(A.LOCATION, B.LOCATION, 0.005)
   FROM s1234874.SETTLEMENTS A, s1234874.SETTLEMENTS B
   WHERE A.NAME = 'London' AND B.NAME = 'Mexico City';

/*Topological intersection between two regions (polygons)*/
SELECT SDO_GEOM.SDO_INTERSECTION(A.SHAPE, B.SHAPE, 0.005)
  FROM S1234874.REGION A, S1234874.REGION B
  WHERE A.NAME = 'Hungary' AND B.NAME = 'Romania';

/*Is there a relationship between regions (polygons)*/
SELECT SDO_GEOM.RELATE(A.SHAPE, 'anyinteract', B.SHAPE, 0.005)
  FROM S1234874.REGION A, S1234874.REGION B
  WHERE A.NAME = 'Hungary' AND B.NAME = 'Romania';

/*Return region (polygon) area, not sure what the units are */
SELECT A.NAME, SDO_GEOM.SDO_AREA(A.SHAPE, 0.005)
  FROM s1234874.REGION A
  WHERE A.NAME = 'Hungary';

/*Distance between two regions*/
/*          DOESNT WORK
SELECT SDO_GEOM.SDO_DISTANCE(A.SHAPE, B.SHAPE, 0.005)
  FROM S1234874.REGION A, S1234874.REGION B
  WHERE A.NAME = 'England' AND B.NAME = 'Mexico';*/

SELECT A.NAME, B.NAME
  FROM S1234874.REGION A, S1234874.SETTLEMENTS B
  WHERE SDO_RELATE(A.SHAPE, B.LOCATION,
    'MASK=ANYINTERACT QUERYTYPE=WINDOW') = 'TRUE'
  ORDER BY A.NAME;
