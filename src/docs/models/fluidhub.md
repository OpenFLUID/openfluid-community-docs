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
While repositories have been replicated from LISAH-Wareshub to OpenFLUID-FluidHub instance, users will have to update their local git settings to use new service. To do so, a [custom shell script](https://nextcloud.inrae.fr/s/BfZBS3LGaSk9xgn) is provided. It takes a path in argument (eg waresdev folder absolute path) and will convert all "origin" remotes from LISAH-Wareshub to OpenFLUID-fluidhub and keep previous remote url as "old_wareshub" remote.

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

### User guide
#### Fragments
*Metadata*: should be stored in a `openfluid-dataset.json` with content in this format:
```json
{
  "id": "h.k",
  "name": "Hayami method",
  "description": "diffusive wave equation resolved with Hayami method",
  "version": "0.1",
  "status": "alpha",
  "authors": [
    {"name": "M R."}
  ],
  "contacts": [],
  "license": "",
  "tags":[""],
  "links": [],
  "issues" : [],
  "dependencies": {},
  "fragment": {
    "openfluid-components": ["core"]
  }
}

```
*Version detection*: not applicable, fragment not necessarily associated with an openfluid version.

#### Datasets
To store datasets, once the repository is created by an administrator, it can be populated with a push. 

*Metadata*: should be stored in a `openfluid-dataset.json` with content in this format:
```json
{
  "id": "thiszone_thismodel",
  "name": "",
  "description": "",
  "version": "fluidx-4",
  "status": "",
  "authors": [
    {
      "name": "B C",
      "email": "bc@spumpkins.org"
    }
  ],
  "contacts": [
    {
      "name": "OpenFLUID contact",
      "email": "contact@openfluid-project.org"
    }
  ],
  "license": "BSD",
  "tags": [
    "domain::hydrology",
    "projectX",
    "type::full-dataset"
  ],
  "links": [
    {
      "label": "OpenFLUID",
      "url": "www.openfluid-project.org"
    },
    {
      "label": "OpenFLUID community",
      "url": "community.openfluid-project.org"
    }
  ],
  "issues": [],
  "dataset": {
  }
}
```
*Version detection*: as for wares, it is done based on branch name but with a dedicated versioning number system. Currently supported version is `fluidx-4`