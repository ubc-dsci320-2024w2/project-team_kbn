# Title

## Introduction

The Public Tree Dataset provides information on public trees in Vancouver, including their location, species, size, planting date, and coordinates. It is published by the City of Vancouver and maintained by the Vancouver Board of Parks and Recreation. Private trees are not included in the inventory. The dataset refreshes daily on weekdays, with tree attributes updated regularly, though it may be several years between updates for some attributes. Priorities and resources determine how fast a change in reality is reflected in the data (City of Vancouver, 2025). For our analysis, we will use data last modified on March 4th, 2025.

The City of Vancouver primarily uses the dataset for maintaining the city’s urban forest, which contributes to Vancouver’s Healthy City Strategy goal of continually improving the conditions that allow everyone to enjoy the highest level of health and well-being possible, by creating environments that benefit physical and mental health (City of Vancouver, 2018, n.d.-a). Other benefits of maintaining the urban forest include cleaner air, capturing carbon, providing habitats for wildlife, and protecting the city from storms, extreme heat, and the impacts of climate change (City of Vancouver, n.d.).

Our team consists of Kaylee Li, Brianna Zhou, and Nicholas Tam. Based on the dataset’s original purpose, our primary goal is to utilise the dataset to optimise tree placement and management for more effective sustainability and recreational benefits for Vancouver’s urban environment.

The intended audiences for this dataset are urban foresters, city planners, local communities, and ecologists. The data provided for the variety of tree species could serve as an additional sample for ecologists. Local communities and city planners could use the data to map out and set up ideal recreation locations. Urban foresters could use the data to plan the types and quantities of trees to plant to improve the environment further.

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

**How do different tree species in Vancouver’s public spaces vary in terms of growth patterns and physical traits, and what does this suggest about their sustainability for Vancouver’s urban environment?**

Sub Questions:

- *How do height and diameter vary across different tree species in Vancouver’s public spaces?* Examines the fundamental growth of characteristics of trees, which are essential for understanding their long-term sustainability in urban areas
- *How does the spatial distribution of the physical traits of species differ across Vancouver?* Determines whether certain species are concentrated in specific areas due to environmental factors, urban planning decisions, or ecological suitability.
- *How do height and diameter of trees influence their placement in different urban settings (e.g., streets, parks, medians, and greenways)?* Trees of different sizes and growth patterns may be more appropriate for certain settings. Understanding these relationships supports better planning for sustainability.

#### Distribution of Diameter and Height Range and Tree Species

Vancouver's public tree inventory primarily consists of small to medium-sized trees. Most of these trees have diameters below 40 inches and heights under 30 feet. Larger specimens, with diameters greater than 100 inches and heights exceeding 50 feet, are quite rare. This scarcity may due to urban constraints, such as limited space and maintenance challenges. The inventory is dominated by tree families such as Rosaceae (rose), Aceraceae (maple), and Fagaceae (oak), indicating a deliberate selection for traits. Moreover, there is a positive correlation between tree height and diameter, which aligns with natural growth patterns.
![species_diameter_height_distribution](images/Bri_eda1/combined_distribution_figure.png)
![diameter_height_relation](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/da727681923e3e667ae2d341332d89a752fad87c/images/Bri_eda1/avg_dia_height.png)

#### Distribution of Average Diameter and Count of Height Range in the Top 20 Common Family Species

Vancouver's top 20 tree families display distinct growth patterns. Larger species, such as Cupressaceae (cypress) and Salicaceae (willow), tend to have greater average diameters and heights, often exceeding 50 meters. This may be due to their slow growth rates or genetic traits. In contrast, smaller families like Cornaceae (dogwood) and Styracaceae (storax) typically reach shorter heights, ranging from 10 to 30 meters, and have narrower trunks, reflecting their faster growth rates and ornamental roles.


#### Distribution of Species, Diameter and Height across Vancouver

Vancouver’s three most common tree families—Aceraceae (maple), Fagaceae (oak/beech), and Rosaceae (rose)—exhibit distinct spatial and physical patterns. The Aceraceae and Rosaceae families generally have larger diameters and are evenly distributed throughout the city. In contrast, the Fagaceae family, consisting of smaller-diameter trees, tends to cluster in specific areas. Most tree heights range between 10 to 30 meters, with very few exceeding this height, indicating similar growth limitations across the urban landscape. 

#### Distribution of Diameter and Height in Different Street Side

Vancouver’s street-side tree growth varies significantly by location: parks host the largest trees in both diameter and height, likely due to lower disturbance and ample space. Even and odd street sides show nearly identical diameter ranges and shorter heights (mostly under 30m), reflecting uniform urban conditions and management. In contrast, bike medians and greenways feature smaller trees, suggesting recent plantings or intentional size control for safety, visibility, or space efficiency.

### EDA: Picnic

**How can the Vancouver tree dataset help identify the best locations for spring picnics in Vancouver, tailored to different preferences?**

Sub Questions:

- *Which neighbourhoods have the highest density of large trees (e.g., height over 40 feet) that provide ample shade for comfortable picnic spots?* Large trees are essential for creating shaded areas, which can significantly enhance the picnic experience on sunny days.
- *Which neighbourhoods have the highest diversity of tree families, offering visually varied and unique picnic environments?* A mix of tree species can create a more aesthetically pleasing and engaging atmosphere for picnickers.
- *Which neighbourhoods have trees that produce high amounts of pollen, potentially affecting picnic experiences for people with allergies?* Identifying high-pollen areas can help allergy sufferers avoid discomfort or plan allergy-friendly events.

### EDA: Planting

**Given the tree dataset, how would we want to arrange the types of trees to be planted in certain locations, such that they could survive and significantly improve the ecosystem?**

Sub Questions:

- *Which planted species exist in many different locations within each neighbourhood?*
- *How do trees that have been planted directly compare in terms of diameter to those that have grown naturally?*
- *What is the distribution of ages for specific tree species?*

#### Count of each `SPECIES_NAME` that have been planted

- `Planted_Count` for each species is derived by counting the number of rows with `DATE_PLANTED` filled for each tree species.
- `Proportion_Planted` derived from dividing `Planted_Count` by the total number of the given species.
- Would ideally want a reasonably large `Total_Count` value (at least 300) to mitigate the risk of having too few samples of each species to effectively measure and compare characteristics.
- Would also want `Proportion_Planted` to be within certain range of values (between 0.33 and 0.67) to mitigate the possibility that the obtained properties of planted trees are by random chance, and ensure that there are plenty of both planted and non-planted trees to compare against each other.
- Applied log-transform to `Total_Count` to make colored value range easier to interpret.
- Greater values of `Total_Count` generally provide less extreme values of `Proportion_Planted`.

![species_count_chart](../images/analysis3_eda/species_count_chart.jpg)

#### Scatterplot of `LATITUDE` against `LONGITUDE`

- Distribution of data points along axes of latitude and longitude.
- Provides an estimated "map" of the areas for each `NEIGHBOURHOOD_NAME` in Vancouver, and thus a better understanding of how tree density could be influenced for each area.
- Limited by the number of `NEIGHBOURHOOD_NAME` exceeding the number of colors
- Could be improved upon with `mark_geoshape()`, may require getting coordinate values that were removed in cleaning.

![latvlong](../images/analysis3_eda/latvlong.jpg)

#### Boxplots of `DIAMETER` grouped by `HEIGHT_RANGE`

- Box plots of `DIAMETER` against `HEIGHT_RANGE`.
- For the most part, mean `DIAMETER` increases with `HEIGHT_RANGE`.
- Outliers for `DIAMETER` appear to be more frequent for lower `HEIGHT_RANGE` values, and less frequent for higher `HEIGHT_RANGE` values.

![public_trees_box](../images/analysis3_eda/public_trees_box.jpg)

#### Number of `ON_STREET` grouped by `NEIGHBOURHOOD_NAME`

- Number of streets for each neighbourhood.
- Provides idea of potential variety in tree numbers for each location.

![species_per_genus_chart](../images/analysis3_eda/species_per_genus_chart.jpg)

#### Proportions of `HEIGHT_RANGE` for each `NEIGHBOURHOOD_NAME`

- Normalized stacked bar plot for `HEIGHT_RANGE` proportions against `NEIGHBOURHOOD_NAME`.
- For the most part, the majority of `HEIGHT_RANGE` values are between `HEIGHT_RANGE == "10-20"` and `HEIGHT_RANGE == "30-40"`.

![neighbour_height_stack](../images/analysis3_eda/neighbour_height_stack.jpg)

## Research Questions

### Sustainability Focus

How do different tree species in Vancouver’s public spaces vary in terms of growth patterns and physical traits, and what does this suggest about their sustainability for Vancouver’s urban environment?

Sub Questions:

- *How do height and diameter vary across different tree species in Vancouver’s public spaces?* Examines the fundamental growth of characteristics of trees, which are essential for understanding their long-term sustainability in urban areas
- *How does the spatial distribution of the physical traits of species differ across Vancouver?*
Determines whether certain species are concentrated in specific areas due to environmental factors, urban planning decisions, or ecological suitability.
- *How do height and diameter of trees influence their placement in different urban settings (e.g., streets, parks, medians, and greenways)?* Trees of different sizes and growth patterns may be more appropriate for certain settings. Understanding these relationships supports better planning for sustainability.

### Picnic Focus

How can the Vancouver tree dataset help identify the best locations for spring picnics in Vancouver, tailored to different preferences?

Sub Questions:

- *Which neighbourhoods have the highest density of large trees (e.g., height over 40 feet) that provide ample shade for comfortable picnic spots?* Large trees are essential for creating shaded areas, which can significantly enhance the picnic experience on sunny days.
- *Which neighbourhoods have the highest diversity of tree families, offering visually varied and unique picnic environments?* A mix of tree species can create a more aesthetically pleasing and engaging atmosphere for picnickers.
- *Which neighbourhoods have trees that produce high amounts of pollen, potentially affecting picnic experiences for people with allergies?* Identifying high-pollen areas can help allergy sufferers avoid discomfort or plan allergy-friendly events.

### Planting Focus

Given the tree dataset, how would we want to arrange the types of trees to be planted in certain locations, such that they could survive and significantly improve the ecosystem?

Sub Questions:

- Which planted species exist in many different locations within each neighbourhood?
- How do trees that have been planted directly compare in terms of diameter to those that have grown naturally?
- What is the distribution of ages for specific tree species?

## Task Analysis

### Person 1

- Determine Range: Identify the range of tree diameters.
- Characterize Distribution: Analyze the distribution of diameters and heights among different tree species as well as along different street sides.
- Sort: Rank tree species based on the count of trees, their average diameters and the most common height ranges.
- Filter: Select the top 20 tree species that have diameters greater than 60 inches to illustrate their distribution.
- Calculate the average diameter for each height range of the tree species.
- Compute Derived Value:
  - Compute the total number of trees/ average number of trees in each street side
  - Compute the total number of trees in each family species

### Person 2

- Retrieve Value: Retrieve the number of large trees (height over 40 feet) in each neighbourhood.
- Find Extremum: Which neighbourhood has the highest density of large trees? (Find maximum density of large trees)
- Filter: Filter neighbourhoods with the highest density of large trees for shaded picnic spots.
- Compute Derived Value: Calculate the tree families diversity in each neighbourhood.
- Sort: Rank neighbourhoods by tree density or diversity.

### Person 3

- Compute: Compute the average percentage differences in `DIAMETER` between planted and non-planted trees, and the ages by the number of days between `DATE_PLANTED` and March 5 2025.
- Filter: Filter out `SPECIES_NAME` such that there are plenty of both planted and non-planted trees.
- Characterise distribution: Find the distribution of ages for planted tree `SPECIES_NAME`?
- Sort: Rank `SPECIES_NAME` for appearing in the greatest number of `NEIGHBOURHOOD_NAME` and having large proportions of each corresponding`ON_STREET` containing them.
- Retrieve value: Retrieve the number of trees that have been planted, separated by `SPECIES_NAME`.

## Preliminary Sketches

### Person 1

How do height and diameter vary across different tree species in Vancouver’s public spaces?

Stacked bars illustrate the distribution of height, while the line overlay depicts trends in diameter. This method effectively combines two important aspects: the range of heights and the trends in diameter. It utilizes both the position (with bar height representing count) and line encoding (to show diameter trends) effectively. This combination allows for easy comparison of height categories and average diameters within a single plot.

How does the spatial distribution of the physical traits of species differ across Vancouver?

A scatterplot displays individual trees at their exact geographic coordinates, preserving spatial accuracy. This method avoids the distortions associated with choropleth maps, which aggregate data into arbitrary regions. In the scatterplot, ordinal height categories (small, medium, and large) are represented using distinct shapes, which helps to eliminate biases related to color hierarchy.

How do height and diameter of tree influence their placement in different urban settings (e.g., streets, parks, medians, and greenways)?

Boxplot divide data into five columns and create 15 small plots, which can overwhelm viewers and make comparisons between settings and heights challenging. Grouped bar charts with line overlays may lead to misleading conclusions due to the apparent trends shown by the lines. In contrast, a heatmap is more effective because it directly connects height, diameter, and placement in a single, intuitive view. This makes it particularly useful for high-level comparisons.

### Person 2

### Person 3

The following sketches assume that `SPECIES_NAME` is filtered such that they follow the rules below:

- A reasonably large `Total_Count` value (at least 300) to mitigate the risk of having too few samples of each species to effectively measure and compare characteristics.
- `Proportion_Planted` to be within certain range of values (between 0.33 and 0.67) to mitigate the possibility that the obtained properties of planted trees are by random chance, and ensure that there are plenty of both planted and non-planted trees to compare against each other.

Sketch 1: Which planted species exist in many different locations within each neighbourhood?

The sketch is a heatmap, with `NEIGHBOURHOOD_NAME` on the x-axis, `SPECIES_NAME` on the y-axis, and colour indicating the proportion of streets within each `NEIGHBOURHOOD_NAME` with at least one instance of `SPECIES_NAME`. This sketch provides an understanding of which species are more common in larger varieties of environments and which species are rarer in comparison.

Sketch 2: How do trees that have been planted directly compare in terms of diameter to those that have grown naturally?

The sketch is a bar plot, with `SPECIES_NAME` on the x-axis, and the percentage difference in `DIAMETER` between planted and non-planted `SPECIES_NAME` trees on the y-axis, with non-planted trees as the baseline. This sketch provides information on how well planted trees fare in terms of growth  compared to non-planted trees, and how effective they are in their current environments.

Sketch 3: What is the distribution of ages for specific tree species?

The sketch is a density plot, with age (calculated by the number of days between the planting date and March 5 2025) on the x-axis, and the density on the y-axis, faceted by `SPECIES_NAME`. This sketch helps with identifying which tree species have longer-standing populations and which ones are relatively newer.

![sketch_3](../images/analysis3_eda/sketch_3.jpg)

The high-fidelity sketch selected was a dot plot version of the sketch for the question "How do `SPECIES_NAME` trees that have been planted directly compare in terms of `DIAMETER` to those that have grown naturally?". The sketch adheres to the principles of effectiveness, as the magnitude channel used is position on an aligned scale, allowing for greater accuracy and discriminability. It also adheres to the Gestalt principle of continuity by being arranged in descending order of `DIAM_DIFF_PERCENT`, the percentage difference in diameter between the planted trees and the non-planted trees.

![hi_fidelity_sketch](../images/analysis3_eda/hi_fidelity_sketch.jpg)

## Next Steps

### Person 1

- Compare height and diameter distribution between North and South Vancouver to identity regional to see how environment and urbanization impact growth
- Compare how trees grow in parks vs. along streets
- Look at species known to withstand drought, heavy rain, or storms and analyze their distribution across Vancouver
- Highlight trees best suited for Vancouver’s long-term urban sustainability.

### Person 2

- Impute Missing Neighbourhoods: Fill in missing values in the 'neighbourhood' column using KNN to predict locations like Stanley Park, UBC, or a specific Vancouver neighbourhood.
Layer Features for Optimal Picnic Spots: Combine 'Has Pollen,' 'Tree Diversity,' and 'Tree Density (Large Trees)' to identify the best picnic locations based on pollen, tree variety, and shade.
- Interactive Filtering for Picnic Spot Recommendations: Build an interactive tool (e.g., dashboard) that lets users filter picnic spots based on their preferences for tree density, diversity, or pollen levels, allowing them to find the best spots for their needs.

### Person 3

- Diameter may not be an effective metric of plant health, as planted trees need to be lighter for easier transplanting and maintenance (Camu, 2022); the ratio of plant height to diameter may be a more effective metric.
- Determine which planted species exist in many different locations within each neighbourhood.
- Filter out which trees have planted equivalents and reasonably large values for the total number of trees and proportion of trees that have been planted.
- Determine the distribution of ages from the filtered tree species from the step above.

## Resources

- City of Vancouver. (2025, March 4). Public trees. City of Vancouver Open Data Portal. [https://opendata.vancouver.ca/explore/dataset/public-trees/information/?disjunctive.neighbourhood_name&disjunctive.on_street&disjunctive.species_name&disjunctive.common_name](https://opendata.vancouver.ca/explore/dataset/public-trees/information/?disjunctive.neighbourhood_name&disjunctive.on_street&disjunctive.species_name&disjunctive.common_name)
City of Vancouver. (2018). Urban Forest Strategy, 2018 update. [https://vancouver.ca/files/cov/urban-forest-strategy.pdf](https://vancouver.ca/files/cov/urban-forest-strategy.pdf)
City of Vancouver. (n.d.). Vancouver’s Urban Forest. [https://vancouver.ca/parks-recreation-culture/urban-forest-strategy.aspx#:~:text=Vancouver’s%20urban%20forest%20includes%20every,the%20impacts%20of%20climate%20change](https://vancouver.ca/parks-recreation-culture/urban-forest-strategy.aspx#:~:text=Vancouver’s%20urban%20forest%20includes%20every,the%20impacts%20of%20climate%20change)
City of Vancouver. (n.d.-a). Healthy City Strategy. [https://vancouver.ca/people-programs/healthy-city-strategy.aspx](https://vancouver.ca/people-programs/healthy-city-strategy.aspx)