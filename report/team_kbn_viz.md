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

- *Which planted species exist in many different locations within each neighbourhood?* Understanding this could help identify species that are well-suited to multiple environments, ensuring biodiversity and better ecosystem health across different areas of the city.
- *How do trees that have been planted directly compare in terms of diameter to those that have grown naturally?* Knowing this could highlight how urban planting practices affect tree growth. Planted trees may face more limitations, such as space or soil conditions, which could influence their growth compared to naturally occurring trees.
- *What is the distribution of ages for specific tree species?* This could reveal whether the neighbourhoods are planting enough young trees to sustain long-term tree coverage and whether certain species need more attention for regeneration or maintenance.

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

[viz1](../images/ntam_viz/plant_viz1.html)