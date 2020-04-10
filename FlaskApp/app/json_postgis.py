import urllib.request
import pandas as pd

class JSONtoPostGIS:
    def __init__(self):
        self.json_source = ''
        self.df = pd.DataFrame()

    def set_source(self, json_source):
        self.json_source = json_source
    
    def read_json(self):
        data = urllib.request.urlopen(self.json_source).read()
        self.df = pd.read_json(data)
        return self.df

if __name__=='main':
    JSON_URL = 'url do arquivo .json'
    jtp = JSONtoPostGIS()
    jtp.set_source(JSON_URL)
    jtp.read_json()
    print(jtp.df.head())

def create_gdf(self, type, longitude='longitude', latitude='latitude', geom_col='geom'):
    self.geom_col = geom_col
    if type == 'point':
        self.df[geom_col] = list(zip(self.df[logitude], self.df[latitude]))
        self.df[geom_col] = self.df[geom_col].apply(Point)
    self.gdf = gpd.GeoDataFrame(self.df, geometry=geom_col)

def drop_columns(self, columns_to_drop):
    if not isinstance(columns_to_drop, list):
        raise TypeError('columns_to_drop tem que ser uma list')
    for column in columns_to_drop:
        self.gdf = self.gdf.drop([columns_to_drop], axis=1)

def transform_to_wkt(self):
    self.gdf[self.geom_col] = self.gdf[self.geom_col].apply(create_wkt_element)

def to_postgis(self,type,engine,table_name, schema, if_exists='append'):
    self.gdf.sql{table_name, engine, schema=schema, if_exists=if_exists, index=False, dtype={self.geom_col: Geometry(type, srid:4326)}}

def create_wkt_element(geom):
    return WTKElement(geom.wkt, srid=4326)