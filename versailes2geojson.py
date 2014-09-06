import pandas as pd
import json

# read in original data
csv = pd.read_csv("versaille_stock.csv", sep="\t")

# fetch properties, remove Long and Lat
props = list(csv.columns.values)
props = [p for p in props if p not in ["Longitude",
                                       "Latitude"]]

geojson = []
for row in csv.iterrows():
    accession = row[1]
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [accession["Latitude"],
                            accession["Longitude"]]
        }
    }
    # automatically populate accession properties
    feature_props = {p: accession[p] for p in props}
    feature["properties"] = feature_props
    geojson.append(feature)

with open("accession_locations.json", "w") as f:
    json.dump(geojson, f)
