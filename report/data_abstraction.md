## Data Abstraction 

| Attribute Name | Attribute Type | Data Semantics | Cardinality |
| -------- | ------- | ------- | ------- |
| TREE_ID | Quantitative | Tree identification number; primary key | 181476 |
| CIVIC_NUMBER | Categorical | Street address of the site at which the tree is associated with  | 8338 |
| STD_STREET | Categorical | Street name of the site at which the tree is associated with  | 814 |
| GENUS_NAME | Categorical | Genus name of the tree | 169 |
| SPECIES_NAME | Categorical | Species name of the tree | 539 |
| CULTIVAR_NAME | Categorical | Cultivar name of the tree | 1070 |
| COMMON_NAME | Categorical | Common name of the tree | 1297 |
| ON_STREET_BLOCK | Categorical | The street block at which the tree is physically located on | 189 |
| ON_STREET | Categorical | The name of the street on which the tree is physically located | 822 |
| NEIGHBOURHOOD_NAME | Categorical | City’s defined local area in which the tree is located | 23 |
| STREET_SIDE_NAME | Categorical | The street side on which the tree is physically located | 6 |
| HEIGHT_RANGE_ID | Ordinal | Height range of the tree for every 10 feet | 9 |
| HEIGHT_RANGE | Ordinal | Height range of the tree measured in feet | 9 |
| DIAMETER | Quantitative | Diameter of tree at breast height in inches | 490 |
| DATE_PLANTED | Date | Planted date of new tree | 4571 |
| Geom | Geographic point | Spatial representation indicating the location of the tree | 181348 |
| geo_point_2d | Categorical | Location of the tree in 2D | 181348 |
| LATITUDE | Quantitative | Latitude of a tree’s location | 181344 |
| LONGITUDE | Quantitative | Longitude of a tree’s location | 181343 |
| NOMENCLATURE | Categorical | Combination of GENUS_NAME and SPECIES_NAME | 701 |
| ON_ADDRESS | Categorical | Combination of ON_STREET_BLOCK, ON_STREET, NEIGHBOURHOOD_NAME, STREET_SIDE_NAME | 19267 |
| FAMILY_NAME | Categorical | Family name of the tree | 57 |
| HAS_POLLEN | Boolean | Whether tree is known to produce pollen | 2 |
