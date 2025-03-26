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

## Visualisations

### Visualisations -- Person 1

#### Visualisation 1: How do height and diameter vary across different tree species in Vancouver’s public spaces?

##### Mark

- **Heatmap**: Used to compare tree diameters across different height ranges and species. The color intensity effectively illustrates variations in diameter at various heights, making patterns and outliers easily identifiable.

- **Bar Chart**: Used to show the average tree diameter for the top 20 species. The height of each bar allows for straightforward comparisons of tree species regarding diameter, making it easy to rank them.

##### Channels
**Heatmap**: 

- **Position**:
    - X-axis represents different tree species
    - Y-axis denotes height ranges.

- **Color:**  
  A sequential color scale using the scheme red, yellow, and blue is employed. Colors represent varying values of average diameter: red indicates smaller diameters, yellow signifies intermediate sizes, and blue represents larger diameters.

- **Opacity:**  
  Based on the selections made (species that are selected or hovered over), if the average diameter exceeds the threshold set via the slider, the opacity of the corresponding rectangles is set to 1 (highlighted). Non-selected boxes are dimmed to an opacity of 0.3.

- **Tooltip:**  
  Each tooltip provides additional information, including the total tree count, species, height range, and average diameter, enhancing the interpretability of the heatmap.

**Bar Chart**: 
- **Position**:
    - X-axis represents tree species
    - Y-axis indicates their average diameter, promoting an intuitive understanding of size differences.
  
- **Length:** The height of the bars represents the average diameter for each tree species, arranged in ascending order. This sorting simplifies the identification of species with the largest and smallest diameters.

- **Opacity:** When a species is selected, its bar is fully visible (opacity set to 1). For all other species, the bar's opacity is dimmed to 0.3.

- **Tooltip:** The tooltip provides details such as tree species and average diameter, enhancing the interpretability of the data.

##### Interaction and UI Widges

- **Diameter Slider:** This slider allows users to filter heatmap cells by setting a minimum average diameter (avg_diameter) for the tree species they wish to explore.
- **Reset Button:** This button resets the diameter filter to its default state (minimum diameter set to 0). When activated, it restores visibility for all species in the visualizations.
- **Bidirectional Linking:** Users can click on a specific species in either the heatmap or bar chart to select it. Once selected, the species is highlighted in both plots, allowing users to focus on a specific tree species and observe its distribution across both visualizations simultaneously.
- **Conditional Highlighting:** The selected tree species is highlighted in full opacity, while other species are dimmed. This feature enhances focus and reduces visual clutter.
- **Tooltip Enhancements:** Tooltips provide precise numerical values for tree counts, height ranges, and average diameter, improving interpretability while maintaining a clean visualization.


##### Tasks Supported by the Visualization

1. **Retrieve Value:** Tooltips allow users to extract specific details about the tree species, including their average diameter, tree count, height range, and species name.
2. **Characterize Distribution:** Analyze the distribution of tree diameters across different species and height ranges to understand how these factors compare among the various species
3. **Filter:** Users can filter the data based on criteria such as minimum average diameter (using a slider) and specific species selections (via click).
4. **Compute Derived Value:** Aggregated metrics, such as average diameter and tree count per species and height range, are computed and displayed, providing insights into the characteristics of tree populations.
5. **Find Extremum:** Identify species with the largest and smallest average diameters, and examine which height ranges correspond to these extreme values.
6. **Determine Range:** Identify the range of tree diameters within each species and height category.
7. **Find Anomalies:** Detect any species that exhibit unexpectedly high or low diameters at specific heights.
8. **Sort:** Rank tree species by average diameter in ascending order.

##### Why These Choices Were Effective

1. **Data Processing:**  
- Aggregating the data by species and height combination helps summarize the relationship between species, their height ranges, and average diameters. This method allows for easy comparison across different species, helping users understand how height and diameter vary for each type.
- The filter that shows only the top 20 families ensures that the visualization emphasizes the most significant species in terms of their presence in Vancouver’s public spaces. This approach prevents users from being overwhelmed by less-representative species and instead highlights those that the public interacts with most frequently.

2. **Comprehensive Analysis:**  
- The heatmap provides a spatial overview of how height ranges and average diameters are distributed across tree species. This enables users to visually identify trends, such as which species tend to be taller or have larger diameters.
- The bar chart complements the heatmap by offering a detailed view of the average diameter per species, sorted by species name. This visualization clarifies how diameters differ among species, offering insight into which species are larger or smaller and allowing users to dive deeper into individual species for more details.

3. **Dynamic Exploration:**  
- **Species Selection:** Users can explore specific species in more detail through click interactions. This feature allows them to see how the diameter and height of a selected species compare to others. 
- **Average Diameter Slider:** The slider enhances users' ability to focus on specific subsets of the data, particularly regarding tree diameters.
- **Conditional Highlighting:** This feature improves focus on selected species or height ranges, reducing cognitive load and making it easier to visually assess how specific trees or species compare in terms of size characteristics.

4. **Enhanced Interpretability:**  
- Tooltips provide users with direct access to key information such as species name, height range, average diameter, and tree count. This clarity ensures that users understand the data points they are interacting with.
- The opacity changes on hover or selection help guide the user’s attention to the most relevant data, improving the clarity of comparisons between species.

#### Visualisation 2: How does the spatial distribution of the physical traits of species differ across Vancouver?

##### Mark

- **Scatter Plots:** Used to represent tree diameters at different latitudes for various height categories. Each point represents an aggregated average, making spatial trends clear.
- **Bar Charts:** Used to display the dominant species within each height category. This allows for easy comparison of species distribution across different tree sizes.

##### Channels

#### Channels:
**Scatter Plot**
- **Position**:
    - X-axis represents different height categories (small, medium, large)
    - Y-axis encodes the binned latitude as a quantitative value along the y-axis. Latitude is binned into small intervals (step = 0.01) to smooth the distribution.

- **Size**: The size of the circles represents the number of trees in a given height and latitude bin, with a specific scale for tree count.

- **Color:** The color of the circles is determined by whether the point is selected (via dot selection). Selected dots are colored red, while unselected dots are green, highlighting the interactive selection.

- **Tooltip:** Provides additional information on hover, including latitude, height category, average diameter, and tree count.

**Bar Chart**
- **Position:**
    - X-axis represents the binned tree diameter values (maximum of 50 bins)
    - Y-axis represents the tree count in each diameter bin.

- **Tooltip:** Provides additional information on hover, including the height category, tree count, and binned latitude.

##### Interaction and UI Widges

- **Threshold Slider:** The threshold_slider dynamically filters the scatter plot, showing only trees with a count greater than or equal to the selected threshold value.
- **Diameter Slider:** The diameter_selection slider filters the species chart to display only those trees with a diameter greater than or equal to the selected value.
- **Dot Selection:** The dot_selection enables the user to select a specific group of trees by clicking on a scatter plot point. The selected trees' height and latitude values are then used to filter the species chart.
- **Linked Filtering:**
1. As the threshold slider value changes, the scatter plot updates in real-time to reflect the data points that meet the tree count criteria. This allows users to focus on areas with higher tree counts.
2. As the diameter slider value changes, the bar chart updates in real-time to reflect the data points that meet the minimum diameter criteria.
3. Once a point is selected in the scatter plot, the species chart (bar chart) updates to display only data that corresponds to the selected height category and latitude bin.   
- **Conditional Highlighting:** When a point is selected, its color changes from green (default) to red, visually indicating the selection. The species chart then updates to display the diameters of trees corresponding to the selected height and latitude bins.
- **Tooltip Enhancements:** Tooltips provide precise numerical values for tree counts, average diameter, and latitude bin improving interpretability while maintaining a clean visualization.


##### Tasks Supported by the Visualization

1. **Characterize Distribution:**
   - Users can explore how tree diameter distribution varies across different height and latitude categories using the bar chart (species chart).
   - The scatter plot illustrates the distribution of tree counts for each height and latitude bin.
2. **Retrieve Value:** Tooltips enable users to extract specific details about tree species, including average diameter, tree count, and height range across different latitudes.
3. **Filter:**
   - Adjusting the diameter slider filters the bar chart to display only trees with diameters greater than or equal to the selected value, allowing users to focus on specific tree sizes.
   - By selecting a specific point on the scatter plot, users can filter the bar chart to show only the tree diameter distribution for the chosen height and latitude group.
4. **Find Extremum:** Users can interact with the scatter plot to visually identify the latitude bins and heights that correspond to the largest and smallest tree counts.
5. **Determine Range:** Identify the range of tree diameters within each tree species and height category. The species chart displays the range of diameters using bars for the diameter bins. The diameter slider allows users to further filter this range, showing only the trees that fall within the selected diameter thresholds.
6. **Correlate:** Users can identify patterns or trends in tree data distribution, such as whether trees in certain height categories are concentrated in specific latitudes or whether diameter distributions differ significantly across groups.

##### Why These Choices Were Effective

1. **Comprehensive Analysis:**  
- The scatter plot, when used in combination with the latitude binning, directly answers the question of how the spatial distribution (latitude) influences the physical traits (height and diameter) of tree species. Users can quickly observe trends such as which species tend to be taller or have larger diameters at specific latitudes.
- The bar chart complements this analysis by providing a more focused view of the diameter distribution for specific height categories and species. Users can compare the average diameters and see how species vary in size across different latitudes.
2. **Dynamic Exploration:**  
- **Threshold Slider:** The slider allows users to set a threshold for the minimum tree count. As users adjust the slider, the chart updates in real-time to show only the points where the tree count meets or exceeds the specified threshold.
- **Diameter Slider:** The Diameter Slider provides a way to filter data based on the diameter of the trees. It lets users focus on a specific range of tree sizes.
- **Dot Selection:** Dot Selection allows users to click on specific dots in the scatter plot, which represent trees in a particular height and latitude range. It provides a mechanism for selecting and filtering data interactively.
- **Conditional Highlighting:** Conditional Highlighting helps users visually distinguish between selected and unselected data points based on their interactions. This increases the visibility of the elements the user is focusing on and improves the overall clarity of the visualization.
3. **Enhanced Interpretability:**  
- Tooltips provide users with direct access to key information such as tree count, height range and average diameter. This clarity ensures that users understand the data points they are interacting with.

#### Visualisation 3: How do height and diameter of tree influence their placement in different urban settings (e.g., streets, parks, medians, and greenways)?

##### Mark

- **Stacked Bar Chart:** Used to compare tree height categories (small, medium, large) across different street sides. The stacked format allows for a direct proportional comparison across categories.
- **Histogram:** Used to represent the frequency distribution of tree diameters for the selected street side and height category. The binning approach in the histogram effectively shows the distribution of tree sizes.

##### Channels

**Stacked Bar Chart**
- **Position**:
    - X-axis represents different street side
    - Y-axis represents relative proportions of different height ranges (small, medium, large)

- **Color:** The color of the bar is represented by different height ranges

- **Opacity:** Encodes the opacity of each bar, which changes based on the selection of height size (height_selection) and street side (street_selection). Selected values are fully visible (opacity = 1), and others are dimmed (opacity = 0.3).

- **Tooltip:** Provides additional information on hover, including height category, diameter, steer side and tree count.

**Bar Chart**
- **Position:**
    - X-axis represents the diameter of trees). This axis is divided into bins with a maximum of 30 bins.
    - Y-axis represents the tree count in each diameter bin.

- **Tooltip:** Provides additional information on hover, including height category, diameter, steer side and tree count.

##### Interaction and UI Widges

- **Height Selection Radio Button:** This widget allows the user to select a height range for the trees. The options "Small," "Medium," and "Large" correspond to the HEIGHT_SIZE variable, while the "Show All" option displays all tree heights, regardless of the size.

- **Street Selection Radio Button:** This widget allows the user to select a street side (or choose "Show All" to include all streets). The street sides are dynamically populated based on the dataset, and users can pick a specific street side for analysis.

- **Linked Filtering:**
1. The height selection filters both visualizations to display only data corresponding to the selected street side (or all street sides if "Show All" is selected).
2. The street selection filters both visualizations to display only data corresponding to the selected street side (or all street sides if "Show All" is selected).

- **Conditional Highlighting:**
1. The height selection controls the opacity of the bars in the height_bar chart. Trees of the selected height range are fully visible, while trees outside the selection are dimmed.
2. The street selection filters both visualizations to display only data corresponding to the selected street side (or all street sides if "Show All" is selected).

- **Tooltip Enhancements:** Tooltips provide precise numerical values for tree counts, average diameter, and improving interpretability while maintaining a clean visualization.

##### Tasks Supported by the Visualization

1. **Characterize Distribution:**  The height distribution allows users to see which sides of the street have a greater number of trees within specific height ranges.

2. **Filter:** Filtering by tree diameter ensures that the visualization only displays relevant data, specifically trees with diameters under 60 cm. Users can also filter by street side for more precise information.

3. **Retrieve Value:**  Tooltips enable users to extract detailed information about the average diameter, tree count, and height range for different sides of the street.

4. **Compute Derived Value:**  Calculate the total number of trees for each street side and height category.

5. **Find Extremum:**  The stacked bars allow users to easily compare the relative proportions of different height categories on each side of the street.

6. **Determine Range:**  The histogram bins for each street side display the range of tree diameters within each selected height category. Users can visually assess the distribution of tree diameters for each side of the street by selecting different height categories using radio buttons.

7. **Find Anomalies:** Identify any unusual diameter distribution patterns that may exist for specific combinations of street sides and height ranges.

#### Why These Choices Were Effective

1. **Comprehensive Analysis:**  
- The stacked bar chart represents the count of trees in each height category (Small, Medium, Large) across various street sides (urban settings). This allows users to compare how different height categories are distributed across the urban settings.
- The bar chart (histogram) visually shows the distribution of tree diameters across different settings. By binning the diameter data, users can observe the prevalence of certain tree sizes across urban locations.

2. **Dynamic Exploration:**
- **Height Selection Radio Button**: Users can filter by height categories (Small, Medium, Large) or choose "Show All" to view all trees regardless of height. This enables focused exploration of how different height ranges are distributed across various street sides.
- **Street Side Selection:** Users can filter by specific urban settings (e.g., streets, parks, greenways), which allows them to explore how trees of different heights and diameters are placed in these settings.
- **Conditional Highlighting:** Conditional Highlighting helps users visually distinguish between selected and unselected combinations based on their interactions. This increases the visibility of the elements the user is focusing on and improves the overall clarity of the visualization.

3. **Enhanced Interpretability:**  
- Tooltips provide users with direct access to key information such as tree count, height range, street side and average diameter. This clarity ensures that users understand the data points they are interacting with.

### Visualisations -- Person 2

#### Visualization 1: Which neighbourhoods have the highest density of large trees (e.g., height over 40 feet) that provide ample shade for comfortable picnic spots? Large trees are essential for creating shaded areas, which can significantly enhance the picnic experience on sunny days.

##### Marks

- Map (Geospatial Visualization):
  - Used to display tall tree counts (>40ft) across Vancouver neighborhoods.  
  - The geospatial layout provides geographic context, helping users quickly identify areas with dense tall trees.  
  - Color intensity (greens scheme) encodes tall tree counts, emphasizing neighborhoods with the highest concentrations of mature vegetation.  

- Bar Chart:  
  - Used to show the distribution of trees by height range within the selected neighborhood.  
  - Bar lengths represent tree counts for each height range, enabling detailed analysis of tree height composition and supporting comparisons.  

##### Channels

- Map
  - Position: Geographic boundaries represent neighborhoods, offering spatial context for tall tree distributions.  
  - Color: Encodes tall tree counts using a gradient (greens scheme), making it easy to spot areas with high tall tree densities.  
  - Opacity: Highlights the selected neighborhood in full opacity while dimming others, focusing user attention on the chosen area.  
  - Tooltip: Provides additional details like total tree count, tall tree count, and rank, enhancing interpretability.  

- Bar Chart  
  - Position:  
    - Y-axis represents height ranges, organizing data into discrete categories.  
    - X-axis indicates tree count, showing magnitude.  
  - Length: Bar lengths encode the number of trees in each height range, simplifying comparisons.  
  - Color: Uses a consistent greens scheme to align with the map, reinforcing the focus on tall trees.  
  - Tooltip: Displays exact values for tree counts and height ranges, improving clarity.  

##### Interaction and UI Widgets

- Height Slider:
  - Filters trees based on a minimum height threshold (e.g., "At Least Height: 50ft").  
  - This ensures the visualization focuses on tall trees, aligning with the goal of identifying mature vegetation suitable for picnic environments.  

- Neighborhood Dropdown:  
  - Allows users to select a specific neighborhood, dynamically updating both the map and bar chart.  
  - This interaction enables focused analysis by neighborhood, ensuring the visualization adapts to the user’s chosen area.  

- Linked Filtering:  
  - Synchronizes the map and bar chart. Selecting a neighborhood updates both visualizations, creating a cohesive exploration experience.  

- Conditional Highlighting:  
  - Highlights the selected neighborhood in full opacity while dimming others, improving focus and reducing visual clutter.  

- Tooltip Enhancements:  
  - Tooltips provide precise numerical values for tall tree counts, height ranges, and ranks, enhancing interpretability without cluttering the visualization.  

##### Tasks Supported by the Visualization

- Retrieve Value: Tooltips allow users to extract specific details, such as tall tree counts, neighborhood names, and height range distributions.
- Filter: Users can filter data by neighborhood (via dropdown) and by tree height (via slider), enabling focused exploration.  
- Compute Derived Value: Aggregated metrics like total tree count and tall tree count per neighborhood are computed and displayed, providing insights into tree density and maturity.  
- Find Extremum: The map highlights neighborhoods with the highest tall tree densities, while the bar chart identifies dominant height ranges.  
- Sort: Neighborhoods are implicitly ranked by tall tree counts (via color intensity on the map), and height ranges are sorted by tree count in the bar chart.  
- Determine Range: The map’s color scale visualizes the span of tall tree counts across neighborhoods, helping users understand variability.  
- Characterize Distribution: The combination of the map and bar chart allows users to analyze the spread of tall trees spatially and compositionally.  

##### Why These Choices Were Effective

1. Comprehensive Analysis:
   - The map provides an overview of spatial patterns, highlighting areas with dense tall trees.  
   - The bar chart complements the map by offering detailed insights into tree height composition at the neighborhood level.  
   - Together, they provide a holistic view of Vancouver's tree ecosystem, addressing both spatial and compositional aspects.  

2. Dynamic Exploration:  
   - The dropdown menu and height slider allow users to explore the data dynamically, refining their analysis based on neighborhood and tree size.  
   - Linked filtering ensures consistency between the map and bar chart, maintaining a seamless exploration experience.  

3. Enhanced Interpretability:  
   - Conditional highlighting and tooltips improve clarity, making it easier for users to interpret the data and make informed decisions about identifying neighborhoods with the highest density of large trees for comfortable picnic spots.  

#### Visualisation 2: Which neighbourhoods have the highest diversity of tree families, offering visually varied and unique picnic environments? A mix of tree species can create a more aesthetically pleasing and engaging atmosphere for picnickers.

##### Marks

- Map (Geospatial Visualization):
  - Used to display the diversity of tree genera across Vancouver neighborhoods.  
  - The geospatial layout provides geographic context, enabling users to quickly identify areas with high biodiversity.  
  - Color intensity (`blues` scheme) encodes unique tree genera counts, making it easy to spot neighborhoods with the highest ecological richness.  

- Bar Chart:  
  - Used to show the top 10 tree families by distinct genera count for the selected neighborhood.  
  - Bar lengths represent the number of distinct genera per family, enabling comparisons and highlighting the most biodiverse families.  

##### Channels

- Map  
  - Position: Geographic boundaries represent neighborhoods, offering spatial context for biodiversity distribution.  
  - Color: Encodes unique tree genera counts using a gradient (`blues` scheme), emphasizing areas with high biodiversity.  
  - Highlighting: Highlights the selected neighborhood in yellow, drawing attention to the area under analysis.  
  - Tooltip: Provides additional details like neighborhood name, unique genera count, and rank, enhancing interpretability.  

- Bar Chart  
  - Position:  
    - Y-axis lists tree families, sorted in descending order of distinct genera count, emphasizing the most biodiverse families.  
    - X-axis represents the number of distinct genera, showing magnitude.  
  - Length: Bar lengths encode the number of distinct genera, simplifying comparisons between families.  
  - Tooltip: Displays exact values for genera counts and family names, improving clarity.  

##### Interaction and UI Widgets

- Mouse-Based Neighborhood Selection:  
  - Users can click on a specific neighborhood in the map to filter the bar chart, displaying data for that neighborhood.  
  - This interaction is bi-directional: selecting a neighborhood updates both the map and bar chart, ensuring synchronization.  

- Conditional Highlighting:  
  - Highlights the selected neighborhood in yellow while dimming others, improving focus and reducing cognitive load.  

- Linked Filtering:  
  - Ensures the map and bar chart remain synchronized. Clicking on a neighborhood updates both visualizations, creating a cohesive exploration experience.  

- Tooltip Enhancements:  
  - Tooltips provide precise numerical values for unique genera counts, ranks, and family-specific details, enhancing interpretability without cluttering the visualization.  

##### Tasks Supported by the Visualization

- Retrieve Value: Tooltips allow users to extract specific details, such as unique genera counts, neighborhood names, and biodiversity ranks.  
- Filter: Users can filter data by neighborhood (via mouse-based selection), enabling focused exploration.  
- Find Extremum: The map highlights neighborhoods with the highest biodiversity, while the bar chart identifies the most biodiverse tree families.  
- Sort: Neighborhoods are implicitly ranked by biodiversity (via color intensity on the map), and tree families are explicitly sorted by genera count in the bar chart.  
- Characterize Distribution: The combination of the map and bar chart allows users to analyze the spread of biodiversity spatially and compositionally.  

##### Why These Choices Were Effective

1. Data Processing:  
   - Aggregating unique genera counts per neighborhood and identifying the top 10 tree families ensures the visualization is concise and focused on significant contributors to biodiversity.  
   - Filtering the dataset avoids overwhelming users with less relevant data while still providing meaningful insights into biodiversity patterns.  

2. Comprehensive Analysis:  
   - The map provides an overview of spatial patterns, highlighting areas with high or low biodiversity.  
   - The bar chart complements the map by offering detailed insights into the composition of biodiversity, breaking down data by tree families.  
   - Together, they provide a holistic view of Vancouver’s urban tree ecosystem, balancing broad overviews with granular analyses.  

3. Dynamic Exploration:  
   - Mouse-based neighborhood selection and linked filtering enable seamless exploration, allowing users to transition from spatial patterns to family-level breakdowns.  
   - Conditional highlighting improves focus, reducing cognitive load and enhancing interpretability.  

4. Enhanced Interpretability:  
   - Tooltips and conditional highlighting make the visualization accessible to a wide audience, supporting informed decision-making about neighborhoods with diverse picnic environments.  

#### Visualisation 3: Which neighbourhoods have trees that produce high amounts of pollen, potentially affecting picnic experiences for people with allergies? Identifying high-pollen areas can help allergy sufferers avoid discomfort or plan allergy-friendly events.

##### Marks

- Scatterplot:  
  - Used to display the spatial distribution of trees in the selected neighborhood, with points color-coded by pollen presence (Yes/No).  
  - The scatterplot provides a geographic overview, enabling users to identify areas with high concentrations of pollen-producing trees or non-pollen-producing trees.  

- Bar Chart:  
  - Used to show the top 10 streets by tree count in the selected neighborhood, further broken down by pollen presence.  
  - Bar lengths represent tree counts, and color differentiation highlights the proportion of pollen-producing vs. non-pollen-producing trees on each street.  

##### Channels

- Scatterplot  
  - Position: X and Y coordinates represent the geographic locations of trees, offering spatial context.  
  - Color: Encodes pollen presence using distinct colors (e.g., red for "Yes" and blue for "No"), making it easy to distinguish between pollen-producing and non-pollen-producing trees.  
  - Tooltip: Provides additional details like tree location and pollen status, enhancing interpretability.  

- Bar Chart  
  - Position:  
    - Y-axis lists streets, sorted by tree count in descending order, emphasizing streets with the highest tree densities.  
    - X-axis represents tree count, showing magnitude.  
  - Length: Bar lengths encode the number of trees, simplifying comparisons between streets.  
  - Color: Differentiates between pollen-producing and non-pollen-producing trees within each street, highlighting compositional patterns.  
  - Tooltip: Displays exact values for tree counts and pollen breakdowns, improving clarity.  

##### Interaction and UI Widgets

- Dropdown Menu (Neighborhood Selection):  
  - Allows users to select a specific neighborhood from a list, dynamically updating both the scatterplot and bar chart.  
  - This interaction ensures the visualization adapts to the user’s chosen area, enabling focused exploration.  

- Pollen Radio Button (Has Pollen Selection):  
  - Lets users filter trees based on whether they produce pollen ("Yes" or "No").  
  - This feature allows users to focus on specific subsets of data, such as identifying high-pollen areas or planning allergy-friendly events.  

- Linked Filtering:  
  - Ensures both the scatterplot and bar chart update dynamically based on the selections.  
  - For example, selecting a neighborhood updates both visualizations, while filtering by pollen presence refines the displayed data consistently across views.  

- Tooltip Enhancements:  
  - Tooltips provide precise numerical values and additional context, such as tree location and pollen status, without cluttering the visualization.  

##### Tasks Supported by the Visualization

- Retrieve Value: Tooltips allow users to extract specific details, such as tree locations and pollen statuses.  
- Filter: Users can filter data by neighborhood (via dropdown) and pollen presence (via radio buttons), enabling focused exploration.  
- Find Extremum: The scatterplot highlights areas with high concentrations of pollen-producing trees, while the bar chart identifies streets with the most trees.  
- Sort: Streets are explicitly sorted by tree count in the bar chart, emphasizing areas with the highest tree densities.  
- Characterize Distribution: The combination of the scatterplot and bar chart allows users to analyze the spread of pollen-producing trees spatially and compositionally.  

##### Why These Choices Were Effective

1. Comprehensive Analysis:  
   - The scatterplot provides a spatial overview of tree distribution, helping users identify areas with high pollen-producing tree concentrations.  
   - The bar chart complements the scatterplot by offering detailed insights into specific streets, breaking down data by pollen presence.  
   - Together, these visualizations provide a holistic view of Vancouver’s urban tree ecosystem, balancing broad overviews with granular analyses.  

2. Dynamic Exploration:  
   - Dropdown and radio button selections give users control over filtering data, enabling them to explore patterns of pollen presence in specific neighborhoods.  
   - Linked filtering ensures consistency across visualizations, reducing confusion and maintaining focus.  

3. Enhanced Interpretability:  
   - Tooltips and clear color encoding improve clarity, making the visualization accessible to a wide audience.  
   - These features support informed decision-making about identifying high-pollen areas to avoid discomfort for allergy sufferers or plan allergy-friendly events.  

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