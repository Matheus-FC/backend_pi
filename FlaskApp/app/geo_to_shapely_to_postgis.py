import json
from shapely.geometry import shape, GeometryCollection
import psycopg2
from shapely.geometry import LineString
from shapely import wkb

with open("geojson_file.geojson") as f:
  features = json.load(f)["features"]

conn = psycopg2.connect("dbname='banco' user='postgres' host='localhost' password='postgres'")
curs = conn.cursor()

# Make a Shapely geometry
ls = LineString(GeometryCollection([shape(feature["geometry"]).buffer(0) for feature in features]))

# Send it to PostGIS
curs.execute('CREATE TEMP TABLE my_lines(geom geometry, name text)')
curs.execute(
    'INSERT INTO my_lines(geom, name)'
    'VALUES (ST_SetSRID(%(geom)s::geometry, %(srid)s), %(name)s)',
    {'geom': ls.wkb_hex, 'srid': 4326, 'name': 'First Line'})

conn.commit()  # save data


curs.execute('SELECT name, geom FROM my_lines')
for name, geom_wkb in curs:
    geom = wkb.loads(geom_wkb, hex=True)
    print('{0}: {1}'.format(name, geom.wkt))
