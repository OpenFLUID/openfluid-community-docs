## Overview

The MHYDAS model (Moussa et al., 2002, Hydrol. Process. 16) allows to simulate the water production and transfer on surface, the surface-subsurface simplified exchanges and the water balance at different scales - from plot to watershed, and from rain event to annual or pluri-annual simulations. It also can be extended by using extra thematic modules such as pollutant fate and transport or erosive transfer.  

The MHYDAS model takes into account specific features of agricultural landscapes : the influence of landscape discontinuities (reachs, plots, banks...), runoff-infiltration partition according to land use, exchanges between groundwater tables and ditches, ...  

Since version 2.1.8 of OpenFLUID, It is available with the OpenFLUID installation as a bundled example.


### Processes modelling

The dynamics of the MHYDAS model is based on coupled simulators representing several processes. Currently, the surface hydrology module is available as free download : it is made of a production simulator and transfer simulators. The production simulator splits the rainfall into infiltration and runoff on the surface units with the Morel-Seytoux method (1978). The transfer simulators transfer the runoff onto the spatial units (surface and reach segments) and is based on the semi-analytical solution of Hayami (1951).  

This module requires the rainfall as input data, a parameterisation related to the choosen resolution methods and a parameterisation of the spatial units based on geographical and hydrological data (spatial units geometry, soil hydraulic properties and initial moisture).  

If you want to use the MHYDAS model for other processes than surface hydrology, or using other numerical solutions, you can [contact us](http://www.openfluid-project.org/who).

Associated references:

* H. Morel-Seytoux. Derivation of equations for variable rainfall infiltration. Water Resources Research , 14:561–568, 1978.
* Hayami, S. 1951. ‘On the propagation of flood waves’, Disaster Prev. Res. Inst. Bull., 1, 1–16.


### Landscape representation

Landscape representation for the MHYDAS model is based on taking into account the spatial heterogeneities of the cultivated landscape. They lead to hydrological discontinuities and fast responses at high spatial resolutions.

The digital landscape representation for MHYDAS model requires :

* the identification of the natural and anthropogenic landscape elements to represent : ditches, rivers, plots, soil horizons, ...,
* the discretisation of the homogeneous spatial units in agreement with processes modelling,
* the connection of these spatial units through an oriented topology determined by water paths,
* the parametrisation of these spatial units according to processes modelling.


In order to help the modelers for the definition of the digital landscape representation for the MHYDAS model, the Geo-MHYDAS tool (Lagacherie et al , 2010) can be used. It automates a set of spatial analysis commands for performing the landscape discretisation as spatial units, with connections and parametrisation. You can [contact us](http://www.openfluid-project.org/who) if you want to use the Geo-MHYDAS tool.


## Example of application

An example of MHYDAS application is [available online](https://youtu.be/OOJR-rztycs) on YouTube.


## Documentation

The documentation related to each simulator of the MHYDAS model is available online :

* [water.atm-surf.rain-su.files](http://www.openfluid-project.org/resources/docs/mhydas/en/water.atm-surf.rain-su.files.pdf)
* [water.surf-uz.runoff-infiltration.mseytoux](http://www.openfluid-project.org/resources/docs/mhydas/en/water.surf-uz.runoff-infiltration.mseytoux.pdf)
* [water.surf.transfer-su.hayami](http://www.openfluid-project.org/resources/docs/mhydas/en/water.surf.transfer-su.hayami.pdf)
* [water.surf.transfer-rs.hayami](http://www.openfluid-project.org/resources/docs/mhydas/en/water.surf.transfer-rs.hayami.pdf)
