# Optimizing Urban Forests: Leveraging the Vancouver Public Tree Dataset for Sustainability and Recreation

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

- *What are the numbers and proportions of planted trees, by species and genus?* Identifying which species have sufficiently large amounts of samples for both planted and non-planted specimens to conduct analyses with can assist in identifying physical differences between planted and non-planted specimens.
- *Which locations within each neighbourhood can host wide varieties of species?* Understanding this could help identify locations that are well-suited to hosting wider varieties of species, ensuring biodiversity and better ecosystem health across different areas of the city.
- *How do trees that have been planted directly compare in terms of diameter to those that have grown naturally?* Knowing this could highlight how urban planting practices affect tree growth. Planted trees may face more limitations, such as space or soil conditions, which could influence their growth compared to naturally occurring trees.

### Visualisations -- Person 1

### Visualisations -- Person 2

### Visualisations -- Person 3

#### Visualization 1: What are the counts and proportions of planted trees?

##### Marks

- Bar plot:
  - Used to accurately display the proportions of planted specimens between species, ordered by total number of specimens.
  - Bar lengths represent proportions of planted specimens for given species, and color differentiation displays the species' total population size.
- Dot plot:
  - Used to provide an interpretable display of the variation in proportions and total populations.
  - Population size is log-transformed to allow for easier interpretation of values given drastic variations in such.

##### Channels

- Bar plot:
  - Position:
    - Y-axis represents species.
    - X-axis represents the proportions of planted specimens for given species.
  - Color represents the species' total population size, log-transformed, and uses a sequential continuous color palette to display the change in log-transformed total populations, and to display the differences in population sizes should the data be filtered by the widgets.
  - Opacity: Upon brushing on a given range of species, the opacity of all other areas are set to be low, drawing attention to the species under analysis.
  - Tooltip: Displays the corresponding species, genus, proportions of planted specimens and total population size, improving clarity.
- Dot plot:
  - Position:  
    - X-axis represents log-transformed population size, to allow for easier interpretation of values given drastic variations in such.
    - Y-axis represents the proportions of planted specimens for given species.
  - Opacity: Upon brushing on a given range of points, the opacity of all other points are set to be low, drawing attention to the points under analysis.
  - Tooltip: Displays the corresponding species, genus, proportions of planted specimens and total population size, improving clarity.

##### Interaction and UI Widgets 

- Genus Dropdown:  
  - Filters trees based on genus, dynamically updating both the histogram and dot plot. 
  - This ensures the user can apply focused comparisons of counts and proportions between similar species.

- Min Total Count Input Box:  
  - Allows users to select a minimum total population size, to ensure that the values displayed have sufficient samples to conduct analyses with.
  - Set to 300 by default.

- Min Proportion and Max Proportion Sliders:
    - Allows users to select minimum and maximum proportions of planted species, to find species that can be used for practical analysis of characteristics between planted and non-planted samples.
    - Set to 0.3 and 0.7 respectively by default.

- Bidirectional Selection:  
  - Users can brush on either plot to filter values on both sides.
  - Species selection from the bar plot, proportion and log-transformed total count from the dot plot.

- Linked Filtering:  
  - Ensures the bar plot and dot plot remain synchronized. Brushing on either view updates both visualizations, creating a cohesive exploration experience.

- Conditional Highlighting:  
  - Upon brushing into specific marks, the opacity of all other related marks are set to be low, drawing attention to the area under analysis, improving focus and reducing cognitive load.

- Tooltip Enhancements:  
  - Tooltips provide precise numerical values for proportions of planted specimens and total population size corresponding to each species, enhancing interpretability without cluttering the visualization.

##### Tasks Supported by the Visualization
- Retrieve Value: Tooltips allow users to extract specific details, such as proportions of planted specimens and total population size corresponding to each species. 
- Filter: Users can filter data by genus selection (via dropdown), selection of boundaries for population size (via textbox) and proportions of planted specimens (via sliders), and brushing within either plot, enabling focused exploration.
- Compute Derived Value: To obtain the proportion of planted specimens over the total populations for each species, two aggregations were required. The first aggregation involved counting the number of trees with explicit `DATE_PLANTED` values grouped by species, under the assumption that all trees without the `DATE_PLANTED` were not planted trees, while the second involved counting the total number trees for the species that had `DATE_PLANTED` specimens. The proportion was obtained by dividing the number of planted specimens over the total number of specimens for each species.
- Sort: Species in the bar plot are are sorted by population size.

##### Why These Choices Were Effective

- Data Processing:
   - Aggregating proportion of planted specimens over the total populations for each species ensures the visualization is concise and focused on species with sufficiently large amounts of samples to conduct analyses with.  
   - Filtering the dataset avoids overwhelming users with less relevant data while still providing meaningful insights into planted proportions.  

- Comprehensive Analysis:  
   - The bar plot and dot plot visualise variations of proportions of planted specimens across species and population sizes.
   - Together, they allow users to discover which species has sufficient data for both planted and non-planted specimens through the combinations of the total number of trees and the proportion of planted samples.

- Dynamic Exploration:  
   - The dropdown menu, input box, sliders and bidirectional interactions allow users to explore the data dynamically, refining their analysis based on genus, population size, proportions and species.  
   - Linked filtering ensures consistency between the bar plot and dot plot, maintaining a seamless exploration experience.

- Enhanced Interpretability:  
   - Tooltips and conditional highlighting make the visualization accessible to a wide audience, supporting informed decision-making about species with greater flexibility in terms of what species could be focused on.

![plant_viz1](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/f0234f356bd51f871e926d49095ba7b17b5e9a24/images/ntam_viz/plant_viz1.png)

#### Visualization 2: Which planted species exist in many different locations within each neighbourhood?

##### Marks

- Choropleth:
  - Used to display proportions of streets within Vancouver neighborhoods with sufficient species variation, 15 in this case.  
  - The geospatial layout provides geographic context, helping users quickly identify areas with higher or lower homogeneity.  
  - Color intensity (`viridis` scheme) encodes proportions of streets within the neighbourhood with over 15 different species, emphasizing areas with the most extreme variations of species diversity.
- Bar plot:
  - Used to provide more detailed information within each neighbourhood on the counts of species for each street.
  - Bar lengths represent number of species within specific streets, enabling users more detailed information on species variation that would be difficult to display on the choropleth.

##### Channels

- Choropleth:
  - Position: Geographic boundaries represent neighborhoods, offering spatial context for biodiversity distribution.  
  - Color: Encodes proportions of streets within the neighbourhood with over 15 different species (`viridis` scheme), emphasizing areas with the most extreme variations of species diversity.
  - Opacity: Upon selection of an area, the opacity of all other areas are set to be low, drawing attention to the area under analysis.
  - Tooltip: Provides additional details like neighborhood name, number of streets, and proportion of streets with high variety, enhancing interpretability.
- Bar plot:
  - Position:  
    - Y-axis represents neighbourhoods.
    - X-axis represents the counts of species within each street.
  - Color represents the street's corresponding neighbourhood, primarily to group the locations appropriately. The customised color scheme set was intended such that colorblind individuals would be able to perceptual group and differentiate the streets between categories close to each other.
  - Tooltip: Displays the corresponding neighbourhood, street and number of distinct species, improving clarity.

##### Interaction and UI Widgets 

- Mouse-Based Neighborhood Selection:
  - Users can click on a specific neighborhood in the map to filter the bar chart, displaying detailed data for that neighborhood.

- Linked Filtering:  
  - Ensures the choropleth and bar chart remain synchronized. Clicking on a neighborhood updates both visualizations, creating a cohesive exploration experience.

- Conditional Highlighting:  
  - Upon selection of an area, the opacity of all other areas are set to be low, drawing attention to the area under analysis, improving focus and reducing cognitive load.

- Tooltip Enhancements:  
  - Tooltips provide precise numerical values for counts of streets with sufficient species variation and specific number of distinct species corresponding to each location, enhancing interpretability without cluttering the visualization.

##### Tasks Supported by the Visualization

- Retrieve Value: Tooltips allow users to extract specific details, such as counts of streets with sufficient species variation and specific number of distinct species corresponding to each location. 
- Filter: Users can filter data by selection in the choropleth, enabling focused exploration.  
- Compute Derived Value: To obtain the proportion of streets with sufficient species variation, two aggregations were required. The first aggregation involved counting the number of unique species within each street, while the second involved counting the number of streets within each neighbourhood. The proportion was obtained by dividing the number of streets that had sufficient numbers of distinct species over the total number of streets within each neighbourhood.
- Sort: Neighborhoods are implicitly ranked by proportion of streets with sufficient species variation (via color intensity on the map), and species variations are sorted by neighbourhood in the bar chart.

##### Why These Choices Were Effective

- Data Processing:
   - Aggregating unique species counts per street and extent of species variation within each neighbourhood ensures the visualization is concise and focused on significant contributors to biodiversity.  
   - Filtering the dataset avoids overwhelming users with less relevant data while still providing meaningful insights into biodiversity patterns.  

- Comprehensive Analysis:

   - The map provides an overview of spatial patterns, highlighting areas with high or low biodiversity.
   - The bar chart complements the map by offering detailed insights into the composition of biodiversity, breaking down data by locations.  
   - Together, they provide a holistic view of Vancouver’s urban tree ecosystem, balancing broad overviews with granular analyses.

- Dynamic Exploration:

   - Mouse-based neighborhood selection and linked filtering enable seamless exploration, allowing users to transition from spatial patterns to location-level breakdowns.  
   - Conditional highlighting improves focus, reducing cognitive load and enhancing interpretability.

- Enhanced Interpretability:

   - Tooltips and conditional highlighting make the visualization accessible to a wide audience, supporting informed decision-making about neighborhoods with greater flexibility in terms of species sustainability.  

##### Further Developments

- The intended functionality for this visualisation was that the user could select a specific neighbourhood in the choropleth to filter the display of species counts. However, as of this writing, the function has not been implemented, and external assistance is required to resolve it.
- The selected baseline of species variation may not be sufficient, and thus further UI widgets to provide options for such may be considered.
- The sheer quantity of neighbourhoods means that the neighbourhood locations in the bar plot run the risk of being indiscriminable.

![plant_viz2](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/f0234f356bd51f871e926d49095ba7b17b5e9a24/images/ntam_viz/plant_viz2.png)

#### Visualization 3: How do trees that have been planted directly compare in terms of diameter to those that have grown naturally?

##### Marks

- Histogram:
  - Used to display percentage changes in height between planted and non-planted specimens among all species.  
  - Bar heights correspond to counts for each range of change in height, allowing for a display on the distribution of potential height changes.  
  - Since the dataset only provides height ranges for each specimen, the heights for the trees had to be estimated by using the averages for each range, with the `>90` category being estimated with 100 m.

- Dot plot:  
  - Used to display the percentage changes in diameter between planted and non-planted specimens across all species.  
  - Dot positions represent percentage changes between planted and non-planted specimens across species, and the species are set in descending order. 
  - Used over bar charts to follow Tufte’s principle of data-ink ratio.

##### Channels

- Histogram:
  - Position:
    - X-axis represents bins of percentages to organise data into discrete categories.
    - Y-axis represents counts of species, showing magnitude. 
  - Length: Bar lengths encode the number of species in each height range, simplifying comparisons.  
  - Tooltip: Provides specific count value for hovered histogram bins, allowing for more direct comparison of values.  

- Dot plot:
  - Position:  
    - X-axis represents species, in descending order of percentage values.
    - Y-axis represents percentage changes in percentage changes in diameter between planted and non-planted specimens, allowing for an accurate display of the variation in differences across species.
  - Color: Color selected for each point is dependent on whether the value is negative or positive, with the specific color scheme selected to account for colorblindness. 
  - Tooltip: Displays the corresponding values for each species displayed, such as genus and percentage change in height, improving clarity.  

##### Interaction and UI Widgets

- Genus Dropdown:
  - Filters trees based on genus, dynamically updating both the histogram and dot plot. 
  - This ensures the user can apply focused comparisons of physical properties between similar species.  

- Linked Filtering:  
  - The user can brush the histogram to filter out which species had the corresponding change in height to be displayed in the dot plot along with their corresponding change in diameter.

- Conditional Highlighting:  
  - Brushing the histogram changes the corresponding counts for each blue bar, while the grey bars behind them display the original distribution.

- Tooltip Enhancements:  
  - Tooltips provide precise numerical values for counts and the percentage changes corresponding to each species, enhancing interpretability without cluttering the visualization. 

##### Tasks Supported by the Visualization

- Retrieve Value: Tooltips allow users to extract specific details, such as counts in specific ranges and percentage changes for species.
- Filter: Users can filter data by genus (via dropdown) and by brushing in histogram, enabling focused exploration.  
- Compute Derived Value: Differences in height and diameter between planted and non-planted trees are obtained by calculating the average height and diameter for each species, then comparing the percentage change from non-planted trees to planted trees. Since the dataset only provides height ranges for each specimen, the heights for the trees had to be estimated by using the averages for each range, with the `>90` category being estimated with 100 m.
- Sort: Neighborhoods are implicitly ranked by tall tree counts (via color intensity on the map), and height ranges are sorted by tree count in the bar chart.  
- Characterize Distribution: The combination of the historgam and dot plot allows users to analyze the distribution of changes in height and diameter.  

##### Why These Choices Were Effective

1. Comprehensive Analysis:  
   - The histogram provides an overview of the distribution of height changes.  
   - The dot plot displays the changes in diameter changes across species.  
   - These combined provide a better understanding of how drastically certain planted trees may differ compared to their naturally grown counterparts.

2. Dynamic Exploration:  
   - The dropdown menu and histogram brush allow users to explore the data dynamically, refining their analysis based on genus and height range.  
   - Linked filtering ensures consistency between the histogram and dot plot, maintaining a seamless exploration experience.  

3. Enhanced Interpretability:  
   - Conditional highlighting and tooltips improve clarity, making it easier for users to interpret the data and make informed decisions about identifying plants that grow differently from their naturally-grown counterparts.  

##### Further developments

- The displayed data is limited by the inability to ensure that there are sufficient planted and non-planted samples for each given species. Thus the calculated differences in diameter and height may be highly skewed and otherwise inaccurate, and will need to be accounted for in the future.
- Similarly, any species that does not have sufficient data needs to be shown as well in some form.

![plant_viz3](https://github.com/ubc-dsci320-2024w2/project-team_kbn/blob/f0234f356bd51f871e926d49095ba7b17b5e9a24/images/ntam_viz/plant_viz3.png)