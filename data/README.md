## Data

Directories storing example input data. They are preprocessed to cover the
extent of Newport, Wales and are only included for the purposes of this this
example repository. For more information about these data, including their
licensing information, see the subsections below.

### Destinations

A subset of supermarkets in and around the Newport area. They were collected
using [Overpass Turbo](https://overpass-turbo.eu/), with the following query:

```overpass
//preamble
[out:json]
[timeout:180]
[bbox: 51.500932, -3.124184, 51.649469, -2.803005];

//query body
nwr["shop"="supermarket"];


//output data formatting
out center;
```

This data was then exported as a GeoJSON file and converted into a parquet
file. During the conversion, the data was cleaned to remove unneeded columns
and to provide a monotonically increasing ID.

See the [Overpass Turbo documentation](https://wiki.openstreetmap.org/wiki/Overpass_turbo) for more information.

### GTFS

A subset of the GTFS data for the Newport area. The data was downloaded from:

1. `data/gtfs/other_modalities.zip` was extracted from the Department for Transport's [Timetable data](https://data.bus-data.dft.gov.uk/account/login/?next=/timetable/download/) server. The data is licenced under the [Open Government License v3.0](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
2. `data/gtfs/train.zip` was extracted from the [Rail Delivery Group data portal](Rail Delivery Group). It is licenced under the [Creative Commons England and Wales Public Licence](https://creativecommons.org/licenses/by/2.0/uk/legalcode.en-gb). The
raw ATOC data was converted into GTFS format using the [UK2GTFS](https://github.com/ITSLeeds/UK2GTFS).

All GTFS was preprocessed (cleaned and filtered) using [`assess-gtfs`](https://github.com/datasciencecampus/assess_gtfs). They cover travel in and around the Newport
area on the 5th March 2024.

### Origins

A set of population-weighted centroids for the Newport area. These were
extracted for the [ONS Open Geography Portal](https://geoportal.statistics.gov.uk/datasets/ons::output-areas-december-2021-ew-population-weighted-centroids-v3/about)
This data source is licenced under the [Open Government License v3.0](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). The raw data
was filtered to the Newport Local Authority area and then exported as a parquet
file.

### OSM

A subset of the OpenStreetMap data for the Newport area. The raw data was
downloaded from [Geofabrik](https://download.geofabrik.de/europe/great-britain/wales.html). OpenStreetMap data is licenced under the [Open Data Commons Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/), and are the
original contributors of the raw data. The raw data was filtered to the Newport area using [Osmosis](https://github.com/openstreetmap/osmosis), and represents a base-map
that aligns with the GTFS filtering outlined above. This filtered data
set adopts the same ODbl licence.
