## Overview

FluidHub is a deployable system to provide online services for capitalization, follow-up and sharing of models.  

This system proposes features for each hosted simulator, observer and builder-extension:

* source code management (git)
* issue tracker (bugs, changes, review)
* access rights management
* associated documentation
* meta-information: license, contributor(s), contact(s), ...

FluidHub is made of a management system of git repositories, API, webservices and web interface. It can be deployed for various collaborative working purposes : projects, workgroups, research units, company, ...  
The OpenFLUID-DevStudio application allows to directly connect to a FluidHub repository to facilitate development, follow-up and sharing of simulators, observers, and extensions for OpenFLUID-Builder.

An example of a FluidHub instance is the models repository of LISAH research unit, which can be accessed at
[https://hub.openfluid-project.org/ui/](https://hub.openfluid-project.org/ui/)  
It it presented below.

## LISAH-WaresHub

The WaresHub service was the predecessor of FluidHub. The LISAH-Wareshub instance is kept for conservation (https://dev.openfluid-project.org/lisah-wareshub/report/), but not maintained anymore.

### Migration
While repositories have been replicated from LISAH-Wareshub to OpenFLUID-FluidHub instance, users will have to update their local git settings to use new service. To do so, a custom shell script is provided: https://nextcloud.inrae.fr/s/BfZBS3LGaSk9xgn. It takes a path in argument (eg waresdev folder absolute path) and will convert all "origin" remotes from LISAH-Wareshub to OpenFLUID-fluidhub and keep previous remote url as "old_wareshub" remote.

## OpenFLUID-FluidHub

OpenFLUID-FluidHub is the repository for simulators, observers and builder-extensions designed and developed at LISAH research unit.  
In particular, it hosts the MHYDAS and WATSFAR models, the Geo-MHYDAS geomatic tool, and also models coming from reseach works lead at LISAH:

* Surface hydrology
* Groundwater hydrology
* Fate and transfer or organic pollutant (pesticides)
* Erosive transfer
* Agronomy
* ...

### Changes from Wareshub
* New categories: fragments and datasets
* Display of signature and README online for wares in 2.2.+

OpenFLUID-FluidHub can be accessed at [https://hub.openfluid-project.org/ui/](https://hub.openfluid-project.org/ui/).
Access to source codes is allowed depending on users access rights.
