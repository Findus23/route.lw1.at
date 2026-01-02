# Wiener Linien GTFS-RT proxy

This is a very basic server converting the [Wiener Linien realtime API](https://www.data.gv.at/datasets/cfba4373-a654-3e0b-80f8-348738169f95) ([`www.wienerlinien.at/ogd_realtime/trafficInfoList`](https://www.wienerlinien.at/ogd_realtime/trafficInfoList)) into a GTFS-RT URL that Motis can read.

It is quite simple for now (only matching alerts to related lines), but it should be enough for warnings to show up in routes in Motis.

To keep load on the Wiener Linien server minimal, the data is cached for 5min. 
