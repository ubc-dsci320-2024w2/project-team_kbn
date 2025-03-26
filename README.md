# Group KBN - Vancouver Trees

## Website URL
![https://ubc-dsci320-2024w2.github.io/project-team_kbn/]https://ubc-dsci320-2024w2.github.io/project-team_kbn/

## Describe your dataset in about 150-200 words

The [Public Tree Dataset](https://opendata.vancouver.ca/explore/dataset/public-trees/information/?disjunctive.neighbourhood_name&disjunctive.on_street&disjunctive.species_name&disjunctive.common_name), maintained by the Vancouver Board of Parks and Recreation, provides detailed information on public trees across Vancouver, including their location, species, size, planting date, and geographic coordinates. Updated daily on weekdays, the dataset supports the city’s Healthy City Strategy by managing the urban forest to improve physical and mental well-being while delivering environmental benefits such as cleaner air, carbon sequestration, and climate resilience. For this analysis, we used data last modified on March 4th, 2025, and enriched it by integrating external databases. We added the **FAMILY_NAME** column, mapping tree genera to their families using the [Global Biodiversity Information Facility (GBIF)](https://www.gbif.org/), and the **HAS_POLLEN** column, indicating pollen production based on the [Palynological Database (PalDat)](https://www.paldat.org/). To address missing neighborhood data, we utilized the [Overpass API](https://www.openstreetmap.org), an open-source tool developed by Geofabrik GmbH, to retrieve geographical boundaries for areas like Stanley Park and West Point Grey. Additionally, we incorporated the [Local Area Boundary dataset](https://opendata.vancouver.ca/explore/dataset/local-area-boundary/information/?disjunctive.name) from the City of Vancouver’s Open Data Portal to refine neighborhood assignments further. All external data usage complies with licensing terms (CC BY for GBIF and non-commercial use for PalDat), ensuring proper attribution and adherence to non-commercial purposes.


## Describe your topic/interest in about 150-200 words

Our goal is to optimize tree placement and management in Vancouver to enhance sustainability and recreational benefits. The primary focus is on understanding how tree species' growth patterns, physical traits, and spatial distribution affect their sustainability in urban environments. 

For sustainability, we examine the relationship between tree height, diameter, and their suitability for urban spaces, as well as how these traits vary across different neighborhoods and urban settings. From a recreational perspective, the Vancouver tree dataset helps identify ideal locations for spring picnics. We look at tree density for shaded picnic spots, the diversity of tree species for visually engaging environments, and the pollen levels to accommodate those with allergies. These factors are crucial for planning picnic-friendly areas that maximize comfort and enjoyment. Lastly, in terms of planting, we focus on tree species' distribution across neighborhoods, comparing planted trees to naturally grown ones to assess urban planting practices. We also investigate the age distribution of trees to ensure future tree coverage and healthy ecosystem regeneration, aiding better long-term environmental planning.

## Team Members

- Person 1: Brianna Zhou, exploring how different tree species and their physical traits influence their substanability.
- Person 2: Kaylee Li, on a mission to find the perfect picnic spot for the upcoming spring using this dataset.
- Person 3: Nicholas Tam, planning to target the distribution of trees by various factors.

## Package requirements

- `altair`
- `pre-commit`
- `pandas`
- `pygbif`
- `requests`
- `beautifulsoup4`

## References

- City of Vancouver. (2025). Public trees [Data set]. City of Vancouver Open Data Portal. Retrieved March 4, 2025, from https://opendata.vancouver.ca/explore/dataset/public-trees/information/?disjunctive.neighbourhood_name&disjunctive.on_street&disjunctive.species_name&disjunctive.common_name
- City of Vancouver. (2025). Local area boundary [Data set]. City of Vancouver Open Data Portal. Retrieved March 17, 2025, from
https://opendata.vancouver.ca/explore/dataset/local-area-boundary/information/?disjunctive.name
- GBIF.org. (2025). Global Biodiversity Information Facility [Data set]. GBIF Secretariat. https://www.gbif.org
- OpenStreetMap contributors. (2025). Overpass API [Software]. OpenStreetMap Foundation. https://www.openstreetmap.org
- PalDat. (n.d.). Palynological database [Database]. https://www.paldat.org
