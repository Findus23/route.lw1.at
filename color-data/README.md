# Line Colors in Austria

Dataset trying to collect all colors of public transport lines in Austria.

- Mapping GTFS ID to a color (and line color)
- Inspired by https://github.com/Traewelling/line-colors
- I want to avoid creating yet another dataset to be integrated with all others, so I will be using OSM as the data
  source as much as I can.
- If routes don't exist in OSM (yet), I will add the data locally in [`manual-mapping.json`](./manual-mapping.json)
- Main goal is to export the data as [a lua table](../scripts/color-data.lua) that can be read
  by [MOTIS](https://github.com/motis-project/motis)/[transitous](https://transitous.org/)
- Also inspired by and cross-checked with [PTNA](https://ptna.openstreetmap.de/)
- Very WIP so far

## Data-Sources (in decending priority)

### Manually set (`m`)

As some routes don't exist in OSM (yet), I have to store the colors of them locally here. [`manual-mapping.json`](./manual-mapping.json) contains this data together with some sources for the colors and some references to PTNA in case someone wants to create the route in OSM

### Explicit GTFS → color mapping in OSM (`p`)

If a route or route_master relation in OSM has both `gtfs:route_id` and `colour` (and optionally `colour:text`) set, them we can use this color directly.

### Indirect GTFS → OSM relation → color mapping (`j`)

The vast majority of route relations in OSM don't have `gtfs:route_id` set. Nevertheless, we can do the same thing [PTNA](https://ptna.openstreetmap.de/) does to map them to a GTFS route_id: 
The tables in the OSM wiki ([e.g. for VOR](https://wiki.openstreetmap.org/wiki/Austria/Nahverkehr_Ost-Region/Analyse/VOR-Linien)) have CSV files that (in most cases) map GTFS route IDs with tags that (hopefully uniquely) reference one OSM reference that then has color information.

So we can use osmium to [extract](./load_osm.py) all relevant OSM relations from the [OSM dump](../datasets/austria-latest.osm.pbf) into an SQLite table together with the OSM wiki tables and join them in SQL. 

### Hard-coded rules (`r`)

A lot of routes have colors that are easy to determine, even if they are not stored in OSM or anywhere else. E.g. all buses and trams have the same color. So we can check GTFS for all `route_id` that don't have a color yet and check if they are one of these types.

