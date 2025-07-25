from sqlalchemy import create_engine
from get_location import location
import pandas as pd
from geopy.distance import geodesic
from sqlalchemy import text

engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/SYAS")

sql_query = f"""
SELECT matches.id, m.country as country1, m.city as city1,m.state as state1, f.country as country2, f.city as city2, f.state as state2
FROM matches
LEFT JOIN members as m ON matches.male_id = m.id
LEFT JOIN members as f ON matches.female_id = f.id;
"""

with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn)

location_cache = {}


def get_cached_location(city, state, country):
    country = "United States" if country == "USA" else country
    cache_key = (city, state, country)
    if cache_key in location_cache:
        return location_cache[cache_key]
    coords = location(city, state, country)
    location_cache[cache_key] = coords
    return coords


count = 0


def calc_distance(row):
    global count
    count += 1
    print(count)
    parts1 = [
        str(row["city1"]),
        str(row["state1"]),
        "United States" if str(row["country1"]) == "USA" else str(row["country1"]),
    ]
    parts1 = [p for p in parts1 if p and p.lower() != "nan"]
    parts2 = [
        str(row["city2"]),
        str(row["state2"]),
        "United States" if str(row["country2"]) == "USA" else str(row["country2"]),
    ]
    parts2 = [p for p in parts2 if p and p.lower() != "nan"]
    if len(parts1) != 3 or len(parts2) != 3:
        return None
    loc1 = get_cached_location(*parts1)
    loc2 = get_cached_location(*parts2)
    if loc1 is not None and loc2 is not None:
        distance = int(round((geodesic(loc1, loc2).kilometers), 0))
        print(f"distance between {parts1[0]} and {parts2[0]} is {distance}")
        return distance
    else:
        print("Not found")
        return None


print("Calculating distances")
df["distance"] = df.apply(calc_distance, axis=1)
final_df = df[["id", "distance"]].copy()
final_df.to_csv("match_distances.csv", index=False, na_rep="NULL")
