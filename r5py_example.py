# %%
import datetime
import folium
import geopandas as gpd
import pandas as pd
import warnings

from r5py import TransportMode, TransportNetwork, TravelTimeMatrixComputer

# %%
# runtime parameters
origins = "data/origins/pwcs.parquet"
destinations = "data/destinations/supermarkets.parquet"
osm = "data/osm/newport.osm.pbf"
gtfs = ["data/gtfs/rail.zip", "data/gtfs/other_modalities.zip"]

# travel time configuration
departure = datetime.datetime(2024, 3, 5, 8, 0, 0)
transport_modes = [TransportMode.TRANSIT]
travel_time_window = 60  # in minutes
max_travel_time = 45  # in minutes
speed_walking = 4.5  # in km/h
speed_cycling = 15.0  # in km/h

# %%
# read and preprocess origins
origins_gdf = gpd.read_parquet(origins)
origins_gdf = origins_gdf.rename(columns={"OA21CD": "id"})
origins_gdf = origins_gdf.to_crs("EPSG:4326")

# %%
# read and preprocess destinations
destinations_gdf = gpd.read_parquet(destinations)

# %%
# gtfs is optional
transport_network = TransportNetwork(osm, gtfs)

# %%
# build the travel time matrix computer
tt_computer = TravelTimeMatrixComputer(
    transport_network,
    origins=origins_gdf,
    destinations=destinations_gdf,
    departure=departure,
    transport_modes=transport_modes,
    max_time=datetime.timedelta(minutes=max_travel_time),
    departure_time_window=datetime.timedelta(minutes=travel_time_window),
    speed_walking=speed_walking,
    speed_cycling=speed_cycling,
)

# %%
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=FutureWarning)
    tt_df = tt_computer.compute_travel_times()

# %%
tt_df.head()

# %%


def plot_tts_to_destination(
    dest_id: int,
    travel_times: pd.DataFrame,
    origins: gpd.GeoDataFrame,
    destinations: gpd.GeoDataFrame,
) -> folium.Map:
    """Helper function to visualise the travel times.

    Use the hover tooptip for more information. Origins are color coded by the
    median travel time to the destination requested. The destination is marked
    with a red flag. Grey origins indicate that there are no travel times to
    the destination (destination is too remote for the modality). These will
    display the travel time as `null` in the tooltip.

    Parameters
    ----------
    dest_id : int
        Destination ID.
    travel_times : pd.DataFrame
        Travel times output.
    origins : gpd.GeoDataFrame
        Origins geodataframe.
    destinations : gpd.GeoDataFrame
        Destinations geodataframe.

    Returns
    -------
    folium.Map
        Map of travel times to destination requested.

    Raises
    ------
    ValueError
        When:
        - the destination does not exist.
        - there are no travel times to the destination (destination is too
        remote for the modality).
    """
    # raise an error if the destination ID is not in the travel times
    if dest_id not in tt_df["to_id"].unique():
        raise ValueError(f"Destination ID {dest_id} not found")

    # filter the travel times to the destination
    plot_df = travel_times[travel_times["to_id"] == dest_id].copy()

    # raise an error if there are no travel times to the destination
    # handles case where the destination is unreachable
    if all(plot_df["travel_time"].isna()):
        raise ValueError(f"No travel times to destination ID {dest_id}")

    # join on the geometry data
    plot_gdf = origins.merge(
        plot_df,
        left_on="id",
        right_on="from_id",
    ).drop(columns=["id"])

    # visualise the travel times
    m = plot_gdf.explore(
        "travel_time",
        tiles="CartoDB positron",
        legend_kwds={"caption": "Median travel time (minutes)"},
    )

    # add the destination marker
    destination = destinations[destinations["id"] == dest_id][["geometry", "id"]]
    m = destination.explore(
        marker_type="marker",
        marker_kwds={
            "icon": folium.Icon(
                color="red",
                prefix="fa",
                icon="flag-checkered",
            )
        },
        m=m,
    )

    return m


supermarket_id = 6
plot_tts_to_destination(supermarket_id, tt_df, origins_gdf, destinations_gdf)

# %%
