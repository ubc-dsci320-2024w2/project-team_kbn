---
layout: page
title:  "Optimizing Urban Forests: Leveraging the Vancouver Public Tree Dataset for Sustainability and Recreation"
---
![Trees](https://images.unsplash.com/photo-1515884045391-a9e471f4d36f?q=80&w=1457&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

## Introduction

The Public Tree Dataset, published by the City of Vancouver and maintained by the Vancouver Board of Parks and Recreation, provides detailed information on public trees across the city. It includes data on tree location, species, size, planting date, and coordinates. Note that private trees are not included. The dataset is updated daily on weekdays, with tree attributes refreshed regularly, although some attributes may take several years to update, depending on priorities and resources (City of Vancouver, 2025). For this analysis, we are using data last modified on March 4th, 2025.

The City of Vancouver uses this dataset primarily to manage the urban forest as part of its Healthy City Strategy, aiming to improve the physical and mental health of the population through the creation of environments that foster well-being (City of Vancouver, 2018, n.d.-a). The urban forest also provides additional benefits, such as cleaner air, carbon capture, wildlife habitats, and protection from storms, extreme heat, and climate change impacts (City of Vancouver, n.d.).

To enhance the dataset’s value, we added two new columns by integrating external databases. The FAMILY_NAME column maps tree genus names to their respective families using the Global Biodiversity Information Facility (GBIF) database. Since family is a higher taxonomic rank than genus, this provides broader insights into tree species relationships. The HAS_POLLEN column indicates whether a tree produces pollen based on its classification in the Palynological Database (PalDat), helping assess its impact on urban environments and outdoor activities, particularly for allergy-sensitive individuals. All external data usage complies with the respective terms of use, including proper attribution, and the project is strictly non-commercial per GBIF (CC BY) and PalDat (educational/non-commercial use) licensing.

Our team consists of Kaylee Li, Brianna Zhou, and Nicholas Tam. In line with the dataset’s original purpose, our primary goal is to optimize tree placement and management to maximize sustainability and recreational benefits for Vancouver’s urban environment.

The intended audiences for this dataset include urban foresters, city planners, local communities, and ecologists. Ecologists can use the diversity of tree species for research, while local communities and city planners can identify optimal recreation locations. Urban foresters can utilize the data to plan tree-planting strategies that further improve the city's environment.
