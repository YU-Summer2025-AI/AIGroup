#requires a 
# pip install geopy sqlalchemy pandas


from geopy.geocoders import Nominatim
from sqlalchemy import create_engine
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

print(df)


sql_query = text("""
    ALTER TABLE matches
    ADD COLUMN IF NOT EXISTS distance INTEGER;
""")

with engine.begin() as conn:
    result = conn.execute(sql_query)
    print("Column 'distance' added if it did not exist.")

geolocator = Nominatim(user_agent="geoapi")
location = geolocator.geocode("New York, USA")
def location(address):
    try:
        loc = geolocator.geocode(address)
        if loc is not None:
            return(loc.latitude,loc.longitude)
        else:
            return None
    except Exception as e:
        return None

for index, row in df.iterrows():
    parts1 = [str(row['state1']), str(row['country1'])]
    parts1 = [p for p in parts1 if p and p.lower() != 'nan']
    full_address1 = ', '.join(parts1)
    parts2 = [str(row['state2']), str(row['country2'])]
    parts2 = [p for p in parts2 if p and p.lower() != 'nan']
    full_address2 = ', '.join(parts2)
    loc1 = location(full_address1)
    loc2 = location(full_address2)
    distance = None
    if loc1 is not None and loc2 is not None:
        distance = int(round((geodesic(loc1, loc2).kilometers),-2))
    id = row['id']
    print(id,distance)

    sql_query = text("""
        UPDATE matches
        SET distance = :distance
        WHERE id = :id;
    """)

    with engine.begin() as conn:
        result = conn.execute(sql_query, {"distance": distance, "id": id})
        print(f"Rows updated id: {id}")



sql_query = f"""
SELECT distance,matches.id, m.country as country1, m.city as city1,m.state as state1, f.country as country2, f.city as city2, f.state as state2
FROM matches
LEFT JOIN members as m ON matches.male_id = m.id
LEFT JOIN members as f ON matches.female_id = f.id;
"""

with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn,)
print(df)
