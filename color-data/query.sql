-- SPDX-FileCopyrightText: 2025 Lukas Winkler
-- SPDX-FileContributor: Lukas Winkler
--
-- SPDX-License-Identifier: CC0-1.0

SELECT name, colour, colour_text, pt.gtfs_route_id
from osm_routes as o
         join main.ptna_table pt on o.operator = pt.operator and o.ref = pt.ref
where dataset == "vor"
  and colour not null;


SELECT o.name,
       o.ref,
       o.colour,
       o.colour_text,
       pt.gtfs_route_id,
       o.rel_id
FROM osm_routes AS o
         JOIN main.ptna_table AS pt
              ON (pt.operator IS NULL OR o.operator = pt.operator)
                  AND (pt.ref IS NULL OR o.ref = pt.ref)
                  AND (pt."from" IS NULL OR o."from" = pt."from")
WHERE o.colour IS NOT NULL and pt.gtfs_route_id is not null;


SELECT o.name,
       o.ref,
       o.colour,
       o.colour_text,
       pt.gtfs_route_id,
       o.rel_id,gtfs_routes.route_type
FROM osm_routes AS o
         JOIN main.ptna_table AS pt
              ON (pt.operator IS NULL OR o.operator = pt.operator)
                  AND (pt.ref IS NULL OR o.ref = pt.ref)
                  AND (pt."from" IS NULL OR o."from" = pt."from")
        join gtfs_routes on gtfs_routes.route_id == pt.gtfs_route_id
WHERE o.colour IS NULL and gtfs_routes.route_type!=3;
