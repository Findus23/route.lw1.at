SELECT name, colour, colour_text, pt.gtfs_route_id
from osm_routes as o
         join main.ptna_table pt on o.operator = pt.operator and o.ref = pt.ref
where dataset == "vor"
  and colour not null;
