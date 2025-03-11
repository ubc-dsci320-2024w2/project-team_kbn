# Title

## Introduction

## About the Data

### Data Abstraction

| Attribute Name | Attribute Type | Data Semantics | Cardinality |
| -------- | ------- | ------- | ------- |
| TREE_ID | Categorical | Tree identification number; primary key | 181476 |
| CIVIC_NUMBER | Categorical | Street address of the site at which the tree is associated with | 8338 |
| STD_STREET | Categorical | Street name of the site at which the tree is associated with | 814 |
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

### EDA: Sustainability

### EDA: Picnic

### EDA: Planting

#### Count of each `SPECIES_NAME` that have been planted

- `Planted_Count` for each species is derived by counting the number of rows with `DATE_PLANTED` filled for each tree species.
- `Proportion_Planted` derived from dividing `Planted_Count` by the total number of the given species.
- Would ideally want a reasonably large `Total_Count` value (at least 300) to mitigate the risk of having too few samples of each species to effectively measure and compare characteristics.
- Would also want `Proportion_Planted` to be within certain range of values (between 0.33 and 0.67) to mitigate the possibility that the obtained properties of planted trees are by random chance, and ensure that there are plenty of both planted and non-planted trees to compare against each other.
- Applied log-transform to `Total_Count` to make colored value range easier to interpret.
- Greater values of `Total_Count` generally provide less extreme values of `Proportion_Planted`.

#### Scatterplot of `LATITUDE` against `LONGITUDE`

- Distribution of data points along axes of latitude and longitude.
- Provides an estimated "map" of the areas for each `NEIGHBOURHOOD_NAME` in Vancouver, and thus a better understanding of how tree density could be influenced for each area.
- Limited by the number of `NEIGHBOURHOOD_NAME` exceeding the number of colors
- Could be improved upon with `mark_geoshape()`, may require getting coordinate values that were removed in cleaning.

#### Boxplots of `DIAMETER` grouped by `HEIGHT_RANGE`

- Box plots of `DIAMETER` against `HEIGHT_RANGE`.
- For the most part, mean `DIAMETER` increases with `HEIGHT_RANGE`.
- Outliers for `DIAMETER` appear to be more frequent for lower `HEIGHT_RANGE` values, and less frequent for higher `HEIGHT_RANGE` values.

#### Number of `ON_STREET` grouped by `NEIGHBOURHOOD_NAME`

- Number of streets for each neighbourhood.
- Provides idea of potential variety in tree numbers for each location.

#### Proportions of `HEIGHT_RANGE` for each `NEIGHBOURHOOD_NAME`

- Normalized stacked bar plot for `HEIGHT_RANGE` proportions against `NEIGHBOURHOOD_NAME`.
- For the most part, the majority of `HEIGHT_RANGE` values are between `HEIGHT_RANGE == "10-20"` and `HEIGHT_RANGE == "30-40"`.

## Research Questions

## Task Analysis

## Preliminary Sketches

## Next Steps
