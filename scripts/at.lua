local colors = {
	["Wiener Linien GmbH & Co KG"] = {
		["U1"] = { color = 0xE20613,text_color = 0xffffff },
		["U2"] = { color = 0xA762A4,text_color = 0xffffff },
		["U3"] = { color = 0xEF7C00,text_color = 0xffffff },
		["U4"] = { color = 0x029540,text_color = 0xffffff },
		["U5"] = { color = 0x3F8D95,text_color = 0xffffff },
		["U6"] = { color = 0x9C6830,text_color = 0xffffff },
	},
	["OEBB Personenverkehr AG Kundenservice"] = {
		["S1"] = { color = 0xF387A1,text_color = 0xffffff },
		["S45"] = { color = 0xBBD975,text_color = 0xffffff },
	}
}

function process_route(route)
	local agency_name = route:get_agency():get_name()
	local route_name = route:get_short_name()
	local original_route_color = route:get_color()
	local original_route_text_color = route:get_text_color()
	if (original_route_color == 0 or original_route_text_color == 0) and colors[agency_name] and colors[agency_name][route_name] then
        	local color = colors[agency_name][route_name]
        	route:set_color(color.color)
        	route:set_text_color(color.text_color)
	end
	if (original_route_color == 0 or original_route_text_color == 0) then
		if (agency_name == "Wiener Linien GmbH & Co KG") then
			if (route_name:sub(1, 1) == "N") then
				route:set_color(0x1B1464)
				route:set_text_color(0xFEF23F)
			end

		end


	end
end
