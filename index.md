---
layout: page
title:  "Optimizing Urban Forests: Leveraging the Vancouver Public Tree Dataset for Sustainability and Recreation"
---
![Trees](https://images.unsplash.com/photo-1515884045391-a9e471f4d36f?q=80&w=1457&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

## Introduction

The City of Vancouver's [Public Tree Dataset](https://opendata.vancouver.ca/explore/dataset/public-trees/information/?disjunctive.neighbourhood_name&disjunctive.on_street&disjunctive.species_name&disjunctive.common_name), maintained by the Vancouver Board of Parks and Recreation, offers comprehensive records of public trees throughout the city. This valuable resource documents tree locations, species, dimensions, planting dates, and geographic coordinates (excluding private trees). Updated weekdays, the dataset's attributes refresh regularly, though some may take years to update due to resource constraints (City of Vancouver, 2025). Our analysis uses the March 4, 2025 version.

This dataset supports Vancouver's Healthy City Strategy by helping create environments that promote resident well-being (City of Vancouver, 2018). Urban forests provide critical benefits, including air purification, carbon sequestration, wildlife habitats, and climate resilience (City of Vancouver, n.d.). To enhance the dataset's utility, we integrated two key additions:

1. FAMILY_NAME: Mapped tree genera to families using data from [GBIF](https://www.gbif.org) (CC BY license), revealing broader taxonomic relationships.
2. HAS_POLLEN: Identified pollen-producing species via the [Palynological Database (PalDat)](https://www.paldat.org) (non-commercial use) to assess allergy impacts.

During initial analysis, we identified 3,928 records missing neighborhood data. Mapping these revealed concentrations in Stanley Park and UBC/West Point Grey areas (particularly Spanish Bank), plus scattered points in existing neighborhoods. To resolve this, we:

1. Used Geofabrik's [Overpass API](https://www.openstreetmap.org) to obtain boundaries for Stanley Park and West Point Grey.
2. Utilized Vancouver's [Local Area Boundary dataset](https://opendata.vancouver.ca/explore/dataset/local-area-boundary/information/?disjunctive.name), maintained by the City of Vancouver, for precise neighborhood mapping.
3. Assigned accurate neighborhood names to previously unclassified points.

Our team consists of Kaylee Li, Brianna Zhou, and Nicholas Tam. In alignment with the dataset’s original purpose, our primary goal is to optimize tree placement and management to maximize sustainability and recreational benefits for Vancouver’s urban environment. By improving the accuracy and utility of the dataset, we aim to support evidence-based decision-making that enhances the quality of life for Vancouver residents.

The intended audience for this dataset includes urban foresters, city planners, local communities, and ecologists. Ecologists can leverage the diversity of tree species for research purposes, while local communities and city planners can identify optimal locations for recreation. Urban foresters, on the other hand, can utilize the data to develop tree-planting strategies that further enhance the city’s environmental quality. Together, these stakeholders can work toward a more sustainable and resilient urban ecosystem.

---
The code used to generate the visualizations on these pages is available in our GitHub repository's main branch:  
https://github.com/ubc-dsci320-2024w2/project-team_kbn/tree/main