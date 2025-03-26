---
layout: page
title:  "Exploratory Data Analysis"
---

### EDA: Person 1 - Sustainability Focus

#### Distribution of Diameter and Height Range and Tree Species

Vancouver's public tree inventory primarily consists of small to medium-sized trees. Most of these trees have diameters below 40 inches and heights under 30 feet. Larger specimens, with diameters greater than 100 inches and heights exceeding 50 feet, are quite rare. This scarcity may due to urban constraints, such as limited space and maintenance challenges. The inventory is dominated by tree families such as Rosaceae (rose), Aceraceae (maple), and Fagaceae (oak), indicating a deliberate selection for traits. Moreover, there is a positive correlation between tree height and diameter, which aligns with natural growth patterns.
![species_diameter_height_distribution](../images/Bri_eda1/combined_distribution_figure.png)
![diameter_height_relation](../images/Bri_eda1/avg_dia_height.png)

#### Distribution of Average Diameter and Count of Height Range in the Top 20 Common Family Species

Vancouver's top 20 tree families display distinct growth patterns. Larger species, such as Cupressaceae (cypress) and Salicaceae (willow), tend to have greater average diameters and heights, often exceeding 50 meters. This may be due to their slow growth rates or genetic traits. In contrast, smaller families like Cornaceae (dogwood) and Styracaceae (storax) typically reach shorter heights, ranging from 10 to 30 meters, and have narrower trunks, reflecting their faster growth rates and ornamental roles.
![top_20_species_avg_dia_and_height_distri](../images/Bri_eda1/tree_distri.png)

#### Distribution of Species, Diameter and Height across Vancouver

Vancouver’s three most common tree families—Aceraceae (maple), Fagaceae (oak/beech), and Rosaceae (rose)—exhibit distinct spatial and physical patterns. The Aceraceae and Rosaceae families generally have larger diameters and are evenly distributed throughout the city. In contrast, the Fagaceae family, consisting of smaller-diameter trees, tends to cluster in specific areas. Most tree heights range between 10 to 30 meters, with very few exceeding this height, indicating similar growth limitations across the urban landscape. 
![top_3_species_distri](../images/Bri_eda1/top_3_species.png)

#### Distribution of Diameter and Height in Different Street Side

Vancouver’s street-side tree growth varies significantly by location: parks host the largest trees in both diameter and height, likely due to lower disturbance and ample space. Even and odd street sides show nearly identical diameter ranges and shorter heights (mostly under 30m), reflecting uniform urban conditions and management. In contrast, bike medians and greenways feature smaller trees, suggesting recent plantings or intentional size control for safety, visibility, or space efficiency.
![street_side_diameter_height_distribution](../images/Bri_eda1/street_side_fig.png)

### EDA: Person 2 - Picnic Focus

#### Density of Large Trees by Neighbourhood

Kitsilano has the highest number of large trees, making it a potentially ideal picnic spot if only considering places with lots of shades. The presence of many "Null" labeled trees suggests data collection issues or missing information, which, if addressed, could enhance tree distribution understanding and support urban planning. It's surprising that Strathcona has the fewest large trees, despite having parks like MacLean Park and Strathcona Park, possibly due to a higher proportion of open ground or local factors influencing tree growth.
![large_tree_distribution](../images/kli_eda1/large_tree_distribution.png)


#### Diversity of Tree Families by Neighbourhood

Shaughnessy has the highest tree family diversity, likely due to the presence of the VanDusen Botanical Garden. Many trees with high diversity are unassigned to specific neighborhoods, and it would be useful to investigate their locations and assign them. Most other neighborhoods have similar levels of tree family diversity, with no significant differences. Additionally, there is an approximately equal amount of pollen-producing and non-pollen-producing tree families in each neighborhood.
![unique_trees_per_neighbourhood_colored_by_pollen](../images/kli_eda1/unique_trees_per_neighbourhood_colored_by_pollen.png)


#### Pollen Distribution by Neighbourhood

Every neighborhood has both pollen-producing and non-pollen trees, with none being exclusively one type. Hastings-Sunrise, Renfrew-Collingwood, and Kensington-Cedar Cottage have the highest overall tree numbers, indicating significant tree coverage. Some neighborhoods, like Kitsilano, Mount Pleasant, and West Point Grey, have more pollen-producing trees than non-pollen ones, showing a noticeable difference in tree types.
![combined_pollen_figure](../images/kli_eda1/combined_pollen_figure.png)

#### Exploring Trees that are Null in Neighbourhood

Null values (wine-red squares) tend to cluster in specific areas, such as near Dunbar-Southlands, suggesting overlooked trees during labeling. A large cluster above the West End, located in Stanley Park, could benefit from being treated as its own neighborhood due to ambiguity in its classification. Many unlabelled trees near West Point Grey, close to the University of British Columbia, could be considered part of a "University Neighbourhood" in future analyses to improve tree distribution insights.
![combined_pollen_figure](../images/kli_eda1/null_neighbourhood_relative_to_known_neighbourhood.png)


### EDA: Person 3 - Planting Focus

#### Count of each `SPECIES_NAME` that have been planted

- `Planted_Count` for each species is derived by counting the number of rows with `DATE_PLANTED` filled for each tree species.
- `Proportion_Planted` derived from dividing `Planted_Count` by the total number of the given species.
- Would ideally want a reasonably large `Total_Count` value (at least 300) to mitigate the risk of having too few samples of each species to effectively measure and compare characteristics.
- Would also want `Proportion_Planted` to be within certain range of values (between 0.33 and 0.67) to mitigate the possibility that the obtained properties of planted trees are by random chance, and ensure that there are plenty of both planted and non-planted trees to compare against each other.
- Applied log-transform to `Total_Count` to make colored value range easier to interpret.
- Greater values of `Total_Count` generally provide less extreme values of `Proportion_Planted`.

![species_count_chart](../images/ntam_eda1/species_count_chart.png)

#### Scatterplot of `LATITUDE` against `LONGITUDE`

- Distribution of data points along axes of latitude and longitude.
- Provides an estimated "map" of the areas for each `NEIGHBOURHOOD_NAME` in Vancouver, and thus a better understanding of how tree density could be influenced for each area.
- Limited by the number of `NEIGHBOURHOOD_NAME` exceeding the number of colors
- Could be improved upon with `mark_geoshape()`, may require getting coordinate values that were removed in cleaning.

![latvlong](../images/ntam_eda1/latvlong.png)

#### Boxplots of `DIAMETER` grouped by `HEIGHT_RANGE`

- Box plots of `DIAMETER` against `HEIGHT_RANGE`.
- For the most part, mean `DIAMETER` increases with `HEIGHT_RANGE`.
- Outliers for `DIAMETER` appear to be more frequent for lower `HEIGHT_RANGE` values, and less frequent for higher `HEIGHT_RANGE` values.

![public_trees_box](../images/ntam_eda1/public_trees_box.png)

#### Number of `ON_STREET` grouped by `NEIGHBOURHOOD_NAME`

- Number of streets for each neighbourhood.
- Provides idea of potential variety in tree numbers for each location.

![species_per_genus_chart](../images/ntam_eda1/species_per_genus_chart.png)

#### Proportions of `HEIGHT_RANGE` for each `NEIGHBOURHOOD_NAME`

- Normalized stacked bar plot for `HEIGHT_RANGE` proportions against `NEIGHBOURHOOD_NAME`.
- For the most part, the majority of `HEIGHT_RANGE` values are between `HEIGHT_RANGE == "10-20"` and `HEIGHT_RANGE == "30-40"`.

![neighbour_height_stack](../images/ntam_eda1/neighbour_height_stack.png)