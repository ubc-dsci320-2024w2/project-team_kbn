---
layout: page
title:  "Preliminary Sketches"
---

### Person 1 - Sustainability Focus 

**How do height and diameter vary across different tree species in Vancouver’s public spaces?**

Stacked bars illustrate the distribution of height, while the line overlay depicts trends in diameter. This method effectively combines two important aspects: the range of heights and the trends in diameter. It utilizes both the position (with bar height representing count) and line encoding (to show diameter trends) effectively. This combination allows for easy comparison of height categories and average diameters within a single plot.

![b_sketch_1](../images/Bri_sketches/sketch_1.jpg)

**How does the spatial distribution of the physical traits of species differ across Vancouver?**

A scatterplot displays individual trees at their exact geographic coordinates, preserving spatial accuracy. This method avoids the distortions associated with choropleth maps, which aggregate data into arbitrary regions. In the scatterplot, ordinal height categories (small, medium, and large) are represented using distinct shapes, which helps to eliminate biases related to color hierarchy.

![b_sketch_2](../images/Bri_sketches/sketch_2.jpg)

**How do height and diameter of tree influence their placement in different urban settings (e.g., streets, parks, medians, and greenways)?**

Boxplot divide data into five columns and create 15 small plots, which can overwhelm viewers and make comparisons between settings and heights challenging. Grouped bar charts with line overlays may lead to misleading conclusions due to the apparent trends shown by the lines. In contrast, a heatmap is more effective because it directly connects height, diameter, and placement in a single, intuitive view. This makes it particularly useful for high-level comparisons.

![b_sketch_3](../images/Bri_sketches/sketch_%233.jpg)


### Person 2 - Picnic Focus

**Which neighbourhoods have the highest density of large trees (e.g., height over 40 feet) that provide ample shade for comfortable picnic spots?**

A choropleth map visualizes tree density across neighborhoods. While the low-fidelity sketches, like the bar chart and heatmap, provide clear summaries, they lack interactivity and can become cluttered due to many categories. The high-fidelity design enhances the choropleth map with tooltips and filtering, making it easier to explore picnic spots. This approach improves usability by grouping colors effectively, reducing cognitive load, and enabling seamless interaction for better decision-making.

<img src="../images/kli_sketches/sketch_1.png" style="width: 80%; height: auto;" />

**Which neighbourhoods have the highest diversity of tree families, offering visually varied and unique picnic environments?** 

The low-fidelity sketches, including a bar graph, pie charts, and a choropleth map to compare the number of unique trees in each neighborhood, provide useful insights but lack interactivity and may feel overwhelming. The high-fidelity design improves the bar graph by making comparisons clearer and adding filtering and sorting based on selected map areas for better exploration. This approach enhances clarity and usability by visually grouping related data.

  <img src="../images/kli_sketches/sketch_2.png" style="width: 80%; height: auto;" />

**Which neighbourhoods have trees that produce high amounts of pollen, potentially affecting picnic experiences for people with allergies?**

The low-fidelity sketches, including a bubble plot, bar graph, and choropleth map, show pollen levels across neighborhoods but lack data integration. The high-fidelity design improves this by zooming in on a specific neighborhood with a city map and using a scatterplot to display pollenated trees, combining multiple views for a clearer understanding. It also includes tooltips for easier exploration.

  <img src="../images/kli_sketches/sketch_3.png" style="width: 80%; height: auto;" />



### Person 3 - Planting Focus

The following sketches assume that `SPECIES_NAME` is filtered such that they follow the rules below:

- A reasonably large `Total_Count` value (at least 300) to mitigate the risk of having too few samples of each species to effectively measure and compare characteristics.
- `Proportion_Planted` to be within certain range of values (between 0.33 and 0.67) to mitigate the possibility that the obtained properties of planted trees are by random chance, and ensure that there are plenty of both planted and non-planted trees to compare against each other.

**Which planted species exist in many different locations within each neighbourhood?**

The sketchs are a heatmap, a choropleth, and a set of pie charts, each displaying the proportion of streets within each `NEIGHBOURHOOD_NAME` that have least one instance of `SPECIES_NAME`. These sketches provides an understanding of which species are more common in larger varieties of environments and which species are rarer in comparison.

The high-fidelity sketch expands on the choropleth by allowing zooming into each `NEIGHBOURHOOD_NAME` to display the exact number of planted trees within each street for the given locations. The sketch adheres to the principles of effectiveness, as the channels used are spatial region, color luminance and saturation for the choropleth, and position on an aligned scale and length for the bar plots, allowing for greater accuracy, popout, grouping and discriminability between regions. It also adheres to the Gestalt principle of containment by allowing for zooming to bar plots specific to each `NEIGHBOURHOOD_NAME`.

<div style="display: flex; gap: 10px;">
    <img src="../images/ntam_sketches/sketch_3_1_1.jpg" alt="Sketch 3 1 1" style="width: 30%;">
    <img src="../images/ntam_sketches/sketch_3_1_2.jpg" alt="Sketch 3 1 2" style="width: 30%;">
    <img src="../images/ntam_sketches/sketch_3_1_3.jpg" alt="Sketch 3 1 3" style="width: 30%;">
</div>
<img src="../images/ntam_sketches/hi_sketch_1.jpg" alt="Hi Sketch 1" style="width: 50%">


**How do trees that have been planted directly compare in terms of diameter to those that have grown naturally?**

The sketches are a bar plot, a dot plot, and a line plot. The first two sketches have `SPECIES_NAME` on the x-axis, and the percentage difference in `DIAMETER` between planted and non-planted `SPECIES_NAME` trees on the y-axis, with non-planted trees as the baseline. The last sketch has the average `DIAMETER` of planted and non-planted trees on the x-axis and y-axis respectively, compared against the `y=x` line. These sketches provides information on how well planted trees fare in terms of growth  compared to non-planted trees, and how effective they are in their current environments.

The high-fidelity sketch expands on the bar plot, by including a tooltip for the average diameters of planted and non-planted trees, as well as a filter for plants by `GENUS_NAME`. The sketch adheres to the principles of effectiveness, as the magnitude channels used are position on an aligned scale and length, allowing for greater accuracy and discriminability. It also adheres to the Gestalt principle of continuity by being arranged in descending order of `DIAM_DIFF_PERCENT`, the percentage difference in diameter between the planted trees and the non-planted trees.

<div style="display: flex; gap: 10px;">
    <img src="../images/ntam_sketches/sketch_3_2_1.jpg" alt="Sketch 3 2 1" style="width: 30%;">
    <img src="../images/ntam_sketches/sketch_3_2_2.jpg" alt="Sketch 3 2 2" style="width: 30%;">
    <img src="../images/ntam_sketches/sketch_3_2_3.jpg" alt="Sketch 3 2 3" style="width: 30%;">
</div>

<img src="../images/ntam_sketches/hi_sketch_2.jpg" alt="Hi Sketch 2" style="width: 50%;">

**What is the distribution of ages for specific tree species?**

The sketches are a density plot, a box plot, and a histogram, all displaying the distribution of age (calculated by the number of days between the planting date and March 5 2025), faceted by `SPECIES_NAME`. These sketches helps with identifying which tree species have longer-standing populations and which ones are relatively newer.

The high-fidelity sketch expands on the density plot, by including a tooltip for the average age and standard deviation for the existing tree ages, as well as a filter for plants by `GENUS_NAME`. The sketch adheres to the principles of effectiveness, as the channels used are area and spatial region, allowing for greater accuracy and grouping between regions. It also adheres to the Gestalt principle of connection, by allowing filtering of density plots by `GENUS_NAME`.

<div style="display: flex; gap: 10px;">
    <img src="../images/ntam_sketches/sketch_3_3_1.jpg" alt="Sketch 3 3 1" style="width: 30%;">
    <img src="../images/ntam_sketches/sketch_3_3_2.jpg" alt="Sketch 3 3 2" style="width: 30%;">
    <img src="../images/ntam_sketches/sketch_3_3_3.jpg" alt="Sketch 3 3 3" style="width: 30%;">
</div>

<img src="../images/ntam_sketches/hi_sketch_3.jpg" alt="Hi Sketch 3" style="width: 50%">