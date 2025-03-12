# Optimizing Urban Forests: Leveraging the Vancouver Public Tree Dataset for Sustainability and Recreation

## Introduction

The Public Tree Dataset, published by the City of Vancouver and maintained by the Vancouver Board of Parks and Recreation, provides detailed information on public trees across the city. It includes data on tree location, species, size, planting date, and coordinates. Note that private trees are not included. The dataset is updated daily on weekdays, with tree attributes refreshed regularly, although some attributes may take several years to update, depending on priorities and resources (City of Vancouver, 2025). For this analysis, we are using data last modified on March 4th, 2025.

The City of Vancouver uses this dataset primarily to manage the urban forest as part of its Healthy City Strategy, aiming to improve the physical and mental health of the population through the creation of environments that foster well-being (City of Vancouver, 2018, n.d.-a). The urban forest also provides additional benefits, such as cleaner air, carbon capture, wildlife habitats, and protection from storms, extreme heat, and climate change impacts (City of Vancouver, n.d.).

To enhance the dataset’s value, we added two new columns by integrating external databases. The FAMILY_NAME column was created by mapping tree genus names to their respective families through the Global Biodiversity Information Facility (GBIF) database. This was done as a family has a higher taxonomic rank in the biological classification hierarchy than genus, offers broader insights into the relationships among tree species. This classification offers broader insights into the relationships among tree species. The HAS_POLLEN column was added by extracting pollen-related data from the Palynological Database (PalDat) to identify tree species that produce pollen. All external data usage complies with the respective terms of use, including proper attribution, and the project is strictly for non-commercial purposes in accordance with the licensing terms of GBIF (CC BY) and PalDat (educational/non-commercial use).

Our team consists of Kaylee Li, Brianna Zhou, and Nicholas Tam. In line with the dataset’s original purpose, our primary goal is to optimize tree placement and management to maximize sustainability and recreational benefits for Vancouver’s urban environment.

The intended audiences for this dataset include urban foresters, city planners, local communities, and ecologists. Ecologists can use the diversity of tree species for research, while local communities and city planners can identify optimal recreation locations. Urban foresters can utilize the data to plan tree-planting strategies that further improve the city's environment.

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

### EDA: Person 1 - Sustainability Focus

#### Distribution of Diameter and Height Range and Tree Species

Vancouver's public tree inventory primarily consists of small to medium-sized trees. Most of these trees have diameters below 40 inches and heights under 30 feet. Larger specimens, with diameters greater than 100 inches and heights exceeding 50 feet, are quite rare. This scarcity may due to urban constraints, such as limited space and maintenance challenges. The inventory is dominated by tree families such as Rosaceae (rose), Aceraceae (maple), and Fagaceae (oak), indicating a deliberate selection for traits. Moreover, there is a positive correlation between tree height and diameter, which aligns with natural growth patterns.
![species_diameter_height_distribution](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/e0f0de4a9c083a83478cae6041df0418a47dd82c/images/Bri_eda1/combined_distribution_figure.png)
![diameter_height_relation](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/da727681923e3e667ae2d341332d89a752fad87c/images/Bri_eda1/avg_dia_height.png)

#### Distribution of Average Diameter and Count of Height Range in the Top 20 Common Family Species

Vancouver's top 20 tree families display distinct growth patterns. Larger species, such as Cupressaceae (cypress) and Salicaceae (willow), tend to have greater average diameters and heights, often exceeding 50 meters. This may be due to their slow growth rates or genetic traits. In contrast, smaller families like Cornaceae (dogwood) and Styracaceae (storax) typically reach shorter heights, ranging from 10 to 30 meters, and have narrower trunks, reflecting their faster growth rates and ornamental roles.
![top_20_species_avg_dia_and_height_distri](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/e0f0de4a9c083a83478cae6041df0418a47dd82c/images/Bri_eda1/tree_distri.png)

#### Distribution of Species, Diameter and Height across Vancouver

Vancouver’s three most common tree families—Aceraceae (maple), Fagaceae (oak/beech), and Rosaceae (rose)—exhibit distinct spatial and physical patterns. The Aceraceae and Rosaceae families generally have larger diameters and are evenly distributed throughout the city. In contrast, the Fagaceae family, consisting of smaller-diameter trees, tends to cluster in specific areas. Most tree heights range between 10 to 30 meters, with very few exceeding this height, indicating similar growth limitations across the urban landscape. 
![top_3_species_distri](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/e0f0de4a9c083a83478cae6041df0418a47dd82c/images/Bri_eda1/top_3_species.png)

#### Distribution of Diameter and Height in Different Street Side

Vancouver’s street-side tree growth varies significantly by location: parks host the largest trees in both diameter and height, likely due to lower disturbance and ample space. Even and odd street sides show nearly identical diameter ranges and shorter heights (mostly under 30m), reflecting uniform urban conditions and management. In contrast, bike medians and greenways feature smaller trees, suggesting recent plantings or intentional size control for safety, visibility, or space efficiency.
![street_side_diameter_height_distribution](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/e0f0de4a9c083a83478cae6041df0418a47dd82c/images/Bri_eda1/street_side_fig.png)

### EDA: Person 2 - Picnic Focus

#### Density of Large Trees by Neighbourhood

Kitsilano has the highest number of large trees, making it a potentially ideal picnic spot if only considering places with lots of shades. The presence of many "Null" labeled trees suggests data collection issues or missing information, which, if addressed, could enhance tree distribution understanding and support urban planning. It's surprising that Strathcona has the fewest large trees, despite having parks like MacLean Park and Strathcona Park, possibly due to a higher proportion of open ground or local factors influencing tree growth.
![large_tree_distribution](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/d0484cd12fb51c9bd60a68d0d8200253155cd063/images/kli_eda1/large_tree_distribution.png)


#### Diversity of Tree Families by Neighbourhood

Shaughnessy has the highest tree family diversity, likely due to the presence of the VanDusen Botanical Garden. Many trees with high diversity are unassigned to specific neighborhoods, and it would be useful to investigate their locations and assign them. Most other neighborhoods have similar levels of tree family diversity, with no significant differences. Additionally, there is an approximately equal amount of pollen-producing and non-pollen-producing tree families in each neighborhood.
![unique_trees_per_neighbourhood_colored_by_pollen](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/d0484cd12fb51c9bd60a68d0d8200253155cd063/images/kli_eda1/unique_trees_per_neighbourhood_colored_by_pollen.png)


#### Pollen Distribution by Neighbourhood

Every neighborhood has both pollen-producing and non-pollen trees, with none being exclusively one type. Hastings-Sunrise, Renfrew-Collingwood, and Kensington-Cedar Cottage have the highest overall tree numbers, indicating significant tree coverage. Some neighborhoods, like Kitsilano, Mount Pleasant, and West Point Grey, have more pollen-producing trees than non-pollen ones, showing a noticeable difference in tree types.
![combined_pollen_figure](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/d0484cd12fb51c9bd60a68d0d8200253155cd063/images/kli_eda1/combined_pollen_figure.png)

#### Exploring Trees that are Null in Neighbourhood

Null values (wine-red squares) tend to cluster in specific areas, such as near Dunbar-Southlands, suggesting overlooked trees during labeling. A large cluster above the West End, located in Stanley Park, could benefit from being treated as its own neighborhood due to ambiguity in its classification. Many unlabelled trees near West Point Grey, close to the University of British Columbia, could be considered part of a "University Neighbourhood" in future analyses to improve tree distribution insights.
![combined_pollen_figure](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/d0484cd12fb51c9bd60a68d0d8200253155cd063/images/kli_eda1/null_neighbourhood_relative_to_known_neighbourhood.png)


### EDA: Person 3 - Planting Focus

#### Count of each `SPECIES_NAME` that have been planted

- `Planted_Count` for each species is derived by counting the number of rows with `DATE_PLANTED` filled for each tree species.
- `Proportion_Planted` derived from dividing `Planted_Count` by the total number of the given species.
- Would ideally want a reasonably large `Total_Count` value (at least 300) to mitigate the risk of having too few samples of each species to effectively measure and compare characteristics.
- Would also want `Proportion_Planted` to be within certain range of values (between 0.33 and 0.67) to mitigate the possibility that the obtained properties of planted trees are by random chance, and ensure that there are plenty of both planted and non-planted trees to compare against each other.
- Applied log-transform to `Total_Count` to make colored value range easier to interpret.
- Greater values of `Total_Count` generally provide less extreme values of `Proportion_Planted`.

![species_count_chart](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/8c1a742714bd91f33b64e198fca46adb72061f20/images/analysis3_eda/species_count_chart.png)

#### Scatterplot of `LATITUDE` against `LONGITUDE`

- Distribution of data points along axes of latitude and longitude.
- Provides an estimated "map" of the areas for each `NEIGHBOURHOOD_NAME` in Vancouver, and thus a better understanding of how tree density could be influenced for each area.
- Limited by the number of `NEIGHBOURHOOD_NAME` exceeding the number of colors
- Could be improved upon with `mark_geoshape()`, may require getting coordinate values that were removed in cleaning.

![latvlong](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/8c1a742714bd91f33b64e198fca46adb72061f20/images/analysis3_eda/latvlong.png)

#### Boxplots of `DIAMETER` grouped by `HEIGHT_RANGE`

- Box plots of `DIAMETER` against `HEIGHT_RANGE`.
- For the most part, mean `DIAMETER` increases with `HEIGHT_RANGE`.
- Outliers for `DIAMETER` appear to be more frequent for lower `HEIGHT_RANGE` values, and less frequent for higher `HEIGHT_RANGE` values.

![public_trees_box](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/8c1a742714bd91f33b64e198fca46adb72061f20/images/analysis3_eda/public_trees_box.png)

#### Number of `ON_STREET` grouped by `NEIGHBOURHOOD_NAME`

- Number of streets for each neighbourhood.
- Provides idea of potential variety in tree numbers for each location.

![species_per_genus_chart](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/8c1a742714bd91f33b64e198fca46adb72061f20/images/analysis3_eda/species_per_genus_chart.png)

#### Proportions of `HEIGHT_RANGE` for each `NEIGHBOURHOOD_NAME`

- Normalized stacked bar plot for `HEIGHT_RANGE` proportions against `NEIGHBOURHOOD_NAME`.
- For the most part, the majority of `HEIGHT_RANGE` values are between `HEIGHT_RANGE == "10-20"` and `HEIGHT_RANGE == "30-40"`.

![neighbour_height_stack](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/8c1a742714bd91f33b64e198fca46adb72061f20/images/analysis3_eda/neighbour_height_stack.png)

## Research Questions

### Person 1 - Sustainability Focus

How do different tree species in Vancouver’s public spaces vary in terms of growth patterns and physical traits, and what does this suggest about their sustainability for Vancouver’s urban environment?

Sub Questions:

- *How do height and diameter vary across different tree species in Vancouver’s public spaces?* Examines the fundamental growth of characteristics of trees, which are essential for understanding their long-term sustainability in urban areas
- *How does the spatial distribution of the physical traits of species differ across Vancouver?*
Determines whether certain species are concentrated in specific areas due to environmental factors, urban planning decisions, or ecological suitability.
- *How do height and diameter of trees influence their placement in different urban settings (e.g., streets, parks, medians, and greenways)?* Trees of different sizes and growth patterns may be more appropriate for certain settings. Understanding these relationships supports better planning for sustainability.

### Person 2 - Picnic Focus

How can the Vancouver tree dataset help identify the best locations for spring picnics in Vancouver, tailored to different preferences?

Sub Questions:

- *Which neighbourhoods have the highest density of large trees (e.g., height over 40 feet) that provide ample shade for comfortable picnic spots?* Large trees are essential for creating shaded areas, which can significantly enhance the picnic experience on sunny days.
- *Which neighbourhoods have the highest diversity of tree families, offering visually varied and unique picnic environments?* A mix of tree species can create a more aesthetically pleasing and engaging atmosphere for picnickers.
- *Which neighbourhoods have trees that produce high amounts of pollen, potentially affecting picnic experiences for people with allergies?* Identifying high-pollen areas can help allergy sufferers avoid discomfort or plan allergy-friendly events.

### Person 3 - Planting Focus

Given the tree dataset, how would we want to arrange the types of trees to be planted in certain locations, such that they could survive and significantly improve the ecosystem?

Sub Questions:

- *Which planted species exist in many different locations within each neighbourhood?* Understanding this could help identify species that are well-suited to multiple environments, ensuring biodiversity and better ecosystem health across different areas of the city.
- *How do trees that have been planted directly compare in terms of diameter to those that have grown naturally?* Knowing this could highlight how urban planting practices affect tree growth. Planted trees may face more limitations, such as space or soil conditions, which could influence their growth compared to naturally occurring trees.
- *What is the distribution of ages for specific tree species?* This could reveal whether the neighbourhoods are planting enough young trees to sustain long-term tree coverage and whether certain species need more attention for regeneration or maintenance.


## Task Analysis

### Person 1 - Sustainability Focus

- Determine Range: Identify the range of tree diameters.
- Characterize Distribution: Analyze the distribution of diameters and heights among different tree species as well as along different street sides.
- Sort: Rank tree species based on the count of trees, their average diameters and the most common height ranges.
- Filter: Select the top 20 tree species that have diameters greater than 60 inches to illustrate their distribution.
- Calculate the average diameter for each height range of the tree species.
- Compute Derived Value:
  - Compute the total number of trees/ average number of trees in each street side
  - Compute the total number of trees in each family species

### Person 2 - Picnic Focus

- Retrieve Value: Retrieve the number of large trees (height over 40 feet) in each neighbourhood.
- Find Extremum: Which neighbourhood or area has the highest density of large trees, the greatest tree diversity, and ideally the lowest pollen levels?
- Filter: Filter for neighbourhoods with the highest density of large trees (over 40 feet) that provide shaded picnic spots and are dominated by specific tree species, such as cherry blossoms.
- Compute Derived Value: Calculate the tree families diversity in each neighbourhood.
- Sort: Rank neighbourhoods by tree diversity.

### Person 3 - Planting Focus

- Compute: Compute the average percentage differences in `DIAMETER` between planted and non-planted trees, and the ages by the number of days between `DATE_PLANTED` and March 5 2025.
- Filter: Filter out `SPECIES_NAME` such that there are plenty of both planted and non-planted trees.
- Characterise distribution: Find the distribution of ages for planted tree `SPECIES_NAME`?
- Sort: Rank `SPECIES_NAME` for appearing in the greatest number of `NEIGHBOURHOOD_NAME` and having large proportions of each corresponding`ON_STREET` containing them.
- Retrieve value: Retrieve the number of trees that have been planted, separated by `SPECIES_NAME`.

## Preliminary Sketches

### Person 1 - Sustainability Focus 

**How do height and diameter vary across different tree species in Vancouver’s public spaces?**

Stacked bars illustrate the distribution of height, while the line overlay depicts trends in diameter. This method effectively combines two important aspects: the range of heights and the trends in diameter. It utilizes both the position (with bar height representing count) and line encoding (to show diameter trends) effectively. This combination allows for easy comparison of height categories and average diameters within a single plot.
![b_sketch_1](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/e0f0de4a9c083a83478cae6041df0418a47dd82c/images/Bri_sketches/sketch_1.jpg)

**How does the spatial distribution of the physical traits of species differ across Vancouver?**

A scatterplot displays individual trees at their exact geographic coordinates, preserving spatial accuracy. This method avoids the distortions associated with choropleth maps, which aggregate data into arbitrary regions. In the scatterplot, ordinal height categories (small, medium, and large) are represented using distinct shapes, which helps to eliminate biases related to color hierarchy.
![b_sketch_2](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/e0f0de4a9c083a83478cae6041df0418a47dd82c/images/Bri_sketches/sketch_2.jpg)

**How do height and diameter of tree influence their placement in different urban settings (e.g., streets, parks, medians, and greenways)?**

Boxplot divide data into five columns and create 15 small plots, which can overwhelm viewers and make comparisons between settings and heights challenging. Grouped bar charts with line overlays may lead to misleading conclusions due to the apparent trends shown by the lines. In contrast, a heatmap is more effective because it directly connects height, diameter, and placement in a single, intuitive view. This makes it particularly useful for high-level comparisons.
![b_sketch_3](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/e0f0de4a9c083a83478cae6041df0418a47dd82c/images/Bri_sketches/sketch_%233.jpg)

### Person 2 - Picnic Focus

**Which neighbourhoods have the highest density of large trees (e.g., height over 40 feet) that provide ample shade for comfortable picnic spots?**

A choropleth map visualizes tree density across neighborhoods. While the low-fidelity sketches, like the bar chart and heatmap, provide clear summaries, they lack interactivity and can become cluttered due to many categories. The high-fidelity design enhances the choropleth map with tooltips and filtering, making it easier to explore picnic spots. This approach improves usability by grouping colors effectively, reducing cognitive load, and enabling seamless interaction for better decision-making.
<img src="https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/d0484cd12fb51c9bd60a68d0d8200253155cd063/images/kli_sketches/sketch_1.png" height="200px" width="auto" />


**Which neighbourhoods have the highest diversity of tree families, offering visually varied and unique picnic environments?** 

The low-fidelity sketches, including a bar graph, pie charts, and a choropleth map to compare the number of unique trees in each neighborhood, provide useful insights but lack interactivity and may feel overwhelming. The high-fidelity design improves the bar graph by making comparisons clearer and adding filtering and sorting based on selected map areas for better exploration. This approach enhances clarity and usability by visually grouping related data.
![k_sketch_2](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/d0484cd12fb51c9bd60a68d0d8200253155cd063/images/kli_sketches/sketch_2.png){:height="200px" width="auto"}


**Which neighbourhoods have trees that produce high amounts of pollen, potentially affecting picnic experiences for people with allergies?**

The low-fidelity sketches, including a bubble plot, bar graph, and choropleth map, show pollen levels across neighborhoods but lack data integration. The high-fidelity design improves this by zooming in on a specific neighborhood with a city map and using a scatterplot to display pollenated trees, combining multiple views for a clearer understanding. It also includes tooltips for easier exploration.
![k_sketch_3](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/d0484cd12fb51c9bd60a68d0d8200253155cd063/images/kli_sketches/sketch_3.png){:height="200px" width="auto"}


### Person 3 - Planting Focus

The following sketches assume that `SPECIES_NAME` is filtered such that they follow the rules below:

- A reasonably large `Total_Count` value (at least 300) to mitigate the risk of having too few samples of each species to effectively measure and compare characteristics.
- `Proportion_Planted` to be within certain range of values (between 0.33 and 0.67) to mitigate the possibility that the obtained properties of planted trees are by random chance, and ensure that there are plenty of both planted and non-planted trees to compare against each other.

Sketch 1: Which planted species exist in many different locations within each neighbourhood?

The sketch is a heatmap, with `NEIGHBOURHOOD_NAME` on the x-axis, `SPECIES_NAME` on the y-axis, and colour indicating the proportion of streets within each `NEIGHBOURHOOD_NAME` with at least one instance of `SPECIES_NAME`. This sketch provides an understanding of which species are more common in larger varieties of environments and which species are rarer in comparison.

Sketch 2: How do trees that have been planted directly compare in terms of diameter to those that have grown naturally?

The sketch is a bar plot, with `SPECIES_NAME` on the x-axis, and the percentage difference in `DIAMETER` between planted and non-planted `SPECIES_NAME` trees on the y-axis, with non-planted trees as the baseline. This sketch provides information on how well planted trees fare in terms of growth  compared to non-planted trees, and how effective they are in their current environments.

Sketch 3: What is the distribution of ages for specific tree species?

The sketch is a density plot, with age (calculated by the number of days between the planting date and March 5 2025) on the x-axis, and the density on the y-axis, faceted by `SPECIES_NAME`. This sketch helps with identifying which tree species have longer-standing populations and which ones are relatively newer.

![n_sketch_3](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/8c1a742714bd91f33b64e198fca46adb72061f20/images/analysis3_eda/sketch_3.jpg)

The high-fidelity sketch selected was a dot plot version of the sketch for the question "How do `SPECIES_NAME` trees that have been planted directly compare in terms of `DIAMETER` to those that have grown naturally?". The sketch adheres to the principles of effectiveness, as the magnitude channel used is position on an aligned scale, allowing for greater accuracy and discriminability. It also adheres to the Gestalt principle of continuity by being arranged in descending order of `DIAM_DIFF_PERCENT`, the percentage difference in diameter between the planted trees and the non-planted trees.

![n_hi_fidelity_sketch](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/8c1a742714bd91f33b64e198fca46adb72061f20/images/analysis3_eda/hi_fidelity_sketch.png)

## Next Steps

### Person 1 - Sustainability Focus

- Compare height and diameter distribution between North and South Vancouver to identity regional to see how environment and urbanization impact growth
- Compare how trees grow in parks vs. along streets
- Look at species known to withstand drought, heavy rain, or storms and analyze their distribution across Vancouver
- Highlight trees best suited for Vancouver’s long-term urban sustainability.

### Person 2 - Picnic Focus

- Fill in missing values in the 'neighbourhood' column using KNN to predict locations like Stanley Park, UBC, or a specific Vancouver neighbourhood.
- Combine 'Has Pollen,' 'Tree Diversity,' and 'Tree Density (Large Trees)' to identify the best picnic locations based on pollen, tree variety, and shade as a whole
- Build an interactive view that lets users filter picnic spots based on their preferences for tree density, diversity, or pollen levels, allowing them to find the best spots for their own needs.

### Person 3 - Planting Focus

- Diameter may not be an effective metric of plant health, as planted trees need to be lighter for easier transplanting and maintenance (Camu, 2022); the ratio of plant height to diameter may be a more effective metric.
- Determine which planted species exist in many different locations within each neighbourhood.
- Filter out which trees have planted equivalents and reasonably large values for the total number of trees and proportion of trees that have been planted.
- Determine the distribution of ages from the filtered tree species from the step above.

## References

- City of Vancouver. (2025, March 4). Public trees. City of Vancouver Open Data Portal. [https://opendata.vancouver.ca/explore/dataset/public-trees/information/?disjunctive.neighbourhood_name&disjunctive.on_street&disjunctive.species_name&disjunctive.common_name](https://opendata.vancouver.ca/explore/dataset/public-trees/information/?disjunctive.neighbourhood_name&disjunctive.on_street&disjunctive.species_name&disjunctive.common_name)
- City of Vancouver. (2018). Urban Forest Strategy, 2018 update. [https://vancouver.ca/files/cov/urban-forest-strategy.pdf](https://vancouver.ca/files/cov/urban-forest-strategy.pdf)
- City of Vancouver. (n.d.). Vancouver’s Urban Forest. [https://vancouver.ca/parks-recreation-culture/urban-forest-strategy.aspx#:~:text=Vancouver’s%20urban%20forest%20includes%20every,the%20impacts%20of%20climate%20change](https://vancouver.ca/parks-recreation-culture/urban-forest-strategy.aspx#:~:text=Vancouver’s%20urban%20forest%20includes%20every,the%20impacts%20of%20climate%20change)
- City of Vancouver. (n.d.-a). Healthy City Strategy. [https://vancouver.ca/people-programs/healthy-city-strategy.aspx](https://vancouver.ca/people-programs/healthy-city-strategy.aspx)
- Camu, B. (2022, April 3). Bigger is not better! 3 reasons why you should plant trees when they are smaller. Leaf & Limb. [https://www.leaflimb.com/bigger-is-not-better-3-reasons-why-you-should-plant-trees-when-they-are-smaller/#:~:text=Saplings%20are%20easier%20to%20maintain,best%20hope%20for%20future%20success](https://www.leaflimb.com/bigger-is-not-better-3-reasons-why-you-should-plant-trees-when-they-are-smaller/#:~:text=Saplings%20are%20easier%20to%20maintain,best%20hope%20for%20future%20success)
- GBIF.org (2025), Global Biodiversity Information Facility, https://www.gbif.org.
- PalDat – a palynological database (2000 onwards, www.paldat.org)
