---
layout: page
title:  "Research Questions + Tasks Analysis"
---

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
