.. _lbl-BrailsTransportation:

BRAILS - Transportation
------

This tool dialog creates a transportation asset inventory from the US Department of Transportation's `National Bridge Inventory (NBI) <https://geo.dot.gov/mapping/rest/services/NTAD/National_Bridge_Inventory/MapServer>`_, the `National Tunnel Inventory (NTI) <https://geo.dot.gov/mapping/rest/services/NTAD/National_Tunnel_Inventory/MapServer>`_, and the US Census Bureau's `TIGERweb roadway inventory <https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Transportation/MapServer>`_.

The output of the inventory is four GeoJSON files. Each contains the asset information of the bridges, tunnels, roads, and railroads in the user-specified region. BRAILS also outputs a JSON file in the format described in :numref:`lblTransportationInputOption1`, which contains all information in the GeoJSON files.
