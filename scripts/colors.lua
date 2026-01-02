-- based on https://github.com/public-transport/transitous/blob/main/scripts/de-DELFI.lua
-- SPDX-FileCopyrightText: 2025 Felix Gündling, Lukas Winkler
-- SPDX-License-Identifier: AGPL-3.0-or-later


local colors_by_id = require 'scripts.color-data'


function process_route(route)
    local agency_name = route:get_agency():get_name()
    local route_name = route:get_short_name()
    local route_id = route:get_id()
    local original_route_color = route:get_color()
    local original_route_text_color = route:get_text_color()
    if (original_route_color ~= 0 or original_route_text_color ~= 0) then
       return
    end
    if colors_by_id[route_id] then
        print("found")
        print(route_name)
        local color = colors_by_id[route_id]
        route:set_color(color.color)
        route:set_text_color(color.text_color)
    end

end
