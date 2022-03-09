## Background of MHYDAS-Pesticides

Water quality management is a key issue in catchment areas or drinking water catchment areas, most of which are occupied by farming systems that use pesticides. Diagnosing the risks of contamination according to the plant protection practices in use in the catchment areas, but also the climatic, pedological and hydrological specificities of these catchment areas is a difficult exercise due to the multiplicity of the physical, chemical and biological processes involved and their dependence on the intrinsic properties and anthropisation of the environments concerned. The same applies to the design of new plant protection practices that reduce the impact of pesticide use on water resources. In this respect, modelling approaches of the hydro-chemical functioning of catchment areas are potential tools to better evaluate the use-impact relationships of pesticides and thus help in the diagnosis and re-design of agricultural systems in terms of impacts on water resources.  
<br/>
It is in this spirit that the distributed hydrological modelling approach [MHYDAS](../mhydas) (Distributed Hydrological Modelling of Agro-Systems) was initiated in 1995. The basic principle of this approach is to integrate, in a balanced manner, the representation of the physical space in and on which the flows develop, the representation of the mechanisms at the origin of the flows and the representation of the agricultural technical acts which jointly influence the properties of the physical space and the expression of the flow mechanisms. 


## Features et latest version of  MHYDAS-Pesticides 

Since 2000, several versions of MHYDAS have been developed. The initial version consisted of an event-driven hydrological model to simulate floods in a catchment with heterogeneous land management practices (Moussa et al., 2000; Moussa et al; 2002; Chahinian, 2004). Later versions extended the event-based model to simulate pesticide surface transfer (MHYDAS-Pesticides-0.x: Bouvet et al., 2010) and erosion processes (MHYDAS-Erosion: Gumières et al.; 2011). These new versions were developed on the OpenFLUID software platform for spatial modelling in landscapes (Fabre et al., 2010) in order to promote the modularity of the modelling and facilitate the coupling of new spatial processes. For MHYDAS-Pesticides, a new version 1.0 has been developed. This version 1.0 upgrades MHYDAS-Pesticides to OpenFLUID 2.1.x and introduces a set of new features. 

* Continuous modelling version that now also simulates inter-flood processes in terms of hydrological and solute fluxes (evapotranspiration, percolation, degradation...), 
* Representation of the evolution of soil infiltrability as a function of agricultural soil management operations, weed development and rainfall, 
* Representation of row crops and associated crops with distinction of different modes of row management within the same agricultural plot, 
* Representation of the pesticide transfer process in the soil, 
* Representation of the infiltration and retention capacities of pesticides by agricultural ditches according to the state of the ditches, 
* Introduction of a variable calculation time step according to the hydrological events in order to optimise the calculation time of the simulations. 

Thus, version 1.0 of MHYDAS-Pesticides allows the simulation of the hydrological fate of a pesticide molecule following its application in a heterogeneous cultivated landscape with predominant Hortonian runoff flows and changes in the properties of the soil surface layer under the effect of soil management actions. The currently available modelling parameterisations apply primarily to the case of vine crops, but can be extended to the more general case of row crops with or without associated grassing. 
The figure below summarises the main processes represented in MHYDAS-Pesticides 1.0 

## Processes represented in MHYDAS-Pesticides 

<img src="../mhydas-pesticides-processes.png" style="width:800px;">

## Acknowledgements

The development of MHYDAS 1.0 was carried out within the framework of the FEDER-PollDiff project, 2018-2021, supported by the AAP READYNOV of the [Occitanie region](https://www.laregion.fr) and the [European Union](https://european-union.europa.eu/index_en).  

<br/>

<img src="{{ ofweb_url }}/images/logo_Occitanie.png" style="height:100px; margin-right: 30px;">
<img src="{{ ofweb_url }}/images/logo_EuropeOccitanie.png" style="height:100px; margin-right: 30px;">
<img src="{{ ofweb_url }}/images/logo_Europe.jpg" style="height:100px; margin-right: 30px;">

<br/>
