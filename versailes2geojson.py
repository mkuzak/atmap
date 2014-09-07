import pandas as pd
import geojson
from geojson import FeatureCollection, Feature, Point

# read in original data
csv = pd.read_csv("versaille_stock.csv", sep="\t")

# fetch properties, remove Long and Lat
props = list(csv.columns.values)
props = [p for p in props if p not in ["Longitude",
                                       "Latitude"]]

features = []
for row in csv.iterrows():
    accession = row[1]
    lat = accession["Latitude"]
    lon = accession["Longitude"]
    # automatically populate accession properties
    feature_props = {p: accession[p] for p in props}

    f = Feature(
            geometry = Point((lat,lon))
        )

    features.append(f)

fc = FeatureCollection(features)

with open("accession_locations.json", "w") as fh:
    geojson.dump(fc, fh)