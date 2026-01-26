-- based on https://github.com/public-transport/transitous/blob/main/scripts/de-DELFI.lua
-- SPDX-FileCopyrightText: 2025 Felix Gündling, Volker Krause <vkrause@kde.org>, Lukas Winkler
-- SPDX-License-Identifier: AGPL-3.0-or-later


local colors_by_id = require 'scripts.color-data'
local route_type_map = require 'scripts.train_mapping'


function process_route(route)
    local agency_name = route:get_agency():get_name()
    local route_name = route:get_short_name()
    local route_id = route:get_id()
    local original_route_color = route:get_color()
    local original_route_text_color = route:get_text_color()
    if (original_route_color ~= 0 or original_route_text_color ~= 0) then

    else
        if colors_by_id[route_id] then
            local color = colors_by_id[route_id]
            route:set_color(color.color)
            route:set_text_color(color.text_color)
        end
    end

    -- also apply data from train_mapping.lua
    -- https://github.com/public-transport/transitous/blob/main/scripts/at.lua
    for _,m in ipairs(route_type_map) do
        if route:get_route_type() == m[1] and route:get_short_name():sub(1, #m[2]) == m[2] then
            route:set_clasz(m[3])
            route:set_route_type(m[4])
            break
        end
    end

end
