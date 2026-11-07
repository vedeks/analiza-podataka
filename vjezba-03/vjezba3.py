import pandas as pd
import plotly.express as px

df = pd.read_csv("ufo_sightings.csv")

required_columns = {"datetime", "country", "shape", "latitude", "longitude"}
missing_columns = required_columns.difference(df.columns)
if missing_columns:
    raise ValueError(
        f"CSV file is missing required columns: {', '.join(sorted(missing_columns))}"
    )

df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")
df = df.dropna(subset=["datetime"]).copy()
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["hour"] = df["datetime"].dt.hour

yearly_sightings = df.groupby("year").size().reset_index(name="sightings")
fig_year = px.bar(
    yearly_sightings,
    x="year",
    y="sightings",
    title="UFO sightings by year",
    labels={"year": "Year", "sightings": "Number of sightings"},
)
fig_year.show()

country_sightings = (
    df["country"].dropna().value_counts().head(10).rename_axis("country")
    .reset_index(name="sightings")
)
fig_country = px.bar(
    country_sightings,
    x="country",
    y="sightings",
    title="Top 10 countries by UFO sightings",
    labels={"country": "Country", "sightings": "Number of sightings"},
)
fig_country.show()

shape_sightings = (
    df["shape"].dropna().value_counts().head(10).rename_axis("shape")
    .reset_index(name="sightings")
)
fig_shape = px.bar(
    shape_sightings,
    x="shape",
    y="sightings",
    title="Top 10 most common UFO shapes",
    labels={"shape": "Shape", "sightings": "Number of sightings"},
)
fig_shape.show()

df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
map_data = df.dropna(subset=["latitude", "longitude"]).copy()
map_data = map_data[
    map_data["latitude"].between(-90, 90)
    & map_data["longitude"].between(-180, 180)
]

fig_map = px.scatter_geo(
    map_data,
    lat="latitude",
    lon="longitude",
    hover_data=["country", "shape", "datetime"],
    title="World map of UFO sightings",
    projection="natural earth",
)
fig_map.show()
