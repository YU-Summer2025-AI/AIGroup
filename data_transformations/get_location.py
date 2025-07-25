import pandas as pd

city_header = [
    "geonameid",
    "name",
    "asciiname",
    "alternatenames",
    "latitude",
    "longitude",
    "feature class",
    "feature code",
    "country code",
    "cc2",
    "admin1 code",
    "admin2 code",
    "admin3 code",
    "admin4 code",
    "population",
    "elevation",
    "dem",
    "timezone",
    "modification date",
]

cities_df = pd.read_csv(
    "cities500.txt", sep="\t", header=None, names=city_header, encoding="utf-8"
)

country_header = [
    "ISO",
    "ISO3",
    "ISO-Numeric",
    "fips",
    "Country",
    "Capital",
    "Area(in sq km)",
    "Population",
    "Continent",
    "tld",
    "CurrencyCode",
    "CurrencyName",
    "Phone",
    "Postal Code Format",
    "Postal Code Regex",
    "Languages",
    "geonameid",
    "neighbours",
    "EquivalentFipsCode",
]

countries_df = pd.read_csv(
    "countryInfo.txt",
    sep="\t",
    header=None,
    names=country_header,
    comment="#",
    encoding="utf-8",
)
country_map = pd.Series(countries_df.ISO.values, index=countries_df.Country).to_dict()

admin1_header = ["code", "name", "asciiname", "geonameid"]

admin1_df = pd.read_csv(
    "admin1CodesASCII.txt", sep="\t", header=None, names=admin1_header
)
admin1_df[["country code", "admin1 code"]] = admin1_df["code"].str.split(
    ".", expand=True
)


def location(city, state, country):
    country_code = country_map.get(country)
    if not country_code:
        print("Country not found.")
        return None
    if country == "United States":
        state_row = admin1_df[
            (admin1_df["country code"] == country_code)
            & (admin1_df["name"].str.lower() == state.lower())
        ]
        if state_row.empty:
            print(f"State not found, for state {state}")
            return None
        admin1_code = state_row.iloc[0]["admin1 code"]

        cities_with_state = cities_df[
            (cities_df["country code"] == country_code)
            & (cities_df["admin1 code"] == admin1_code)
        ]
        city_data = cities_with_state[
            (cities_with_state["name"].str.lower() == city.lower())
            | (
                cities_with_state["alternatenames"].str.contains(
                    city, case=False, na=False, regex=False
                )
            )
        ]
    else:
        city_data = cities_df[
            (cities_df["country code"] == country_code)
            & (
                (cities_df["name"].str.lower() == city.lower())
                | (
                    cities_df["alternatenames"].str.contains(
                        city, case=False, na=False, regex=False
                    )
                )
            )
        ]
    if not city_data.empty:
        most_populous = city_data.loc[city_data["population"].idxmax()]
        return most_populous["latitude"], most_populous["longitude"]
    else:
        print("No city data.")
        return None
