!!! danger "TODO"
    To be reviewed

The ROpenFLUID package allows to use OpenFLUID within the GNU [R environment](http://www.r-project.org/) environment. This package is available for OpenFLUID 1.7.2 and later versions. Only linux and windows system are currently supported.

## Prerequisites

* Have OpenFLUID 1.7.2 or later installed
* Download and install the [R](http://www.r-project.org/) environment
* Install the RUnit package within the [R](http://www.r-project.org/) environment. Open an [R](http://www.r-project.org/) session and run the following command:
```R
install.packages('RUnit')
```


## Installation of the ROpenFLUID package

* Download the [ROpenFLUID package](http://www.umr-lisah.fr/openfluid/index.php?page=dloads) corresponding to your OpenFLUID version
* Install the ROpenFLUID package within the [R](http://www.r-project.org/) environment. Open an [R](http://www.r-project.org/) session and run the following command:
```R
install.packages('ROpenFLUID_x.x.x-x.tar.gz',repos=NULL)
```
_in the previous command, replace x.x.x-x with the correct version number (e.g. 2.0.0-3)_

## Using OpenFLUID within [R](http://www.r-project.org/)

* The ROpenFLUID package reference manual is available in the [[Documentation]] section.
* All OpenFLUID commands in R are prefixed by OpenFLUID. (''e.g. OpenFLUID.openDataset, OpenFLUID.runSimulation, ...'')


## Examples

* Opening an input dataset and running the simulation
```R
library("ROpenFLUID")  # should be done only once

ofsim = OpenFLUID.openDataset("/path/to/dataset.IN")
OpenFLUID.runSimulation(ofsim)
```


* Opening an input dataset, running the simulation and visualising the variable "varA" of the unit "18" of class "EU", included in the "full" output set
```R
library("ROpenFLUID")  # should be done only once

ofsim = OpenFLUID.openDataset("/path/to/dataset.IN")
OpenFLUID.runSimulation(ofsim)
resEU18 = OpenFLUID.loadResult(ofsim,"EU",18,"full")
plot(resEU18$varA,type="l")
```


* Opening an input dataset, modifying simulation time step and running the simulation
```R
library("ROpenFLUID")  # should be done only once

ofsim = OpenFLUID.openDataset("/path/to/dataset.IN")
OpenFLUID.setDeltaT(ofsim,3600)
OpenFLUID.runSimulation(ofsim)
```


* Opening an input dataset, modifying parameter "coeff" of the simulation function ""example.function.A" and running the simulation
```R
library("ROpenFLUID")  # should be done only once

ofsim = OpenFLUID.openDataset("/path/to/dataset.IN")
OpenFLUID.setFunctionParam(ofsim,"example.function.A","coeff",12.1)
OpenFLUID.runSimulation(ofsim)
```


* Opening an input dataset, modifying inputdata "idata1" of the unit "18" of class "EU" and running the simulation
```R
library("ROpenFLUID")  # should be done only once

ofsim = OpenFLUID.openDataset("/path/to/dataset.IN")
OpenFLUID.setInputData(ofsim,"EU",18,"idata1",99.9)
OpenFLUID.runSimulation(ofsim)
```
