
The ROpenFLUID package allows to use OpenFLUID within the GNU [R](http://www.r-project.org/) environment. This package is available for OpenFLUID 1.7.2 and later versions. Only linux and windows systems are currently supported.

## Prerequisites

* Have OpenFLUID 1.7.2 or later installed
* Download and install the [R](http://www.r-project.org/) environment
* Install the [RUnit](https://cran.r-project.org/web/packages/RUnit/) package within the [R](http://www.r-project.org/) environment. Open an [R](http://www.r-project.org/) session and run the following command:
```R
install.packages('RUnit')
```


## Installation of the ROpenFLUID package

* Download the [ROpenFLUID](http://www.openfluid-project.org/downloads/) package corresponding to your OpenFLUID version
* Install the ROpenFLUID package within the [R](http://www.r-project.org/) environment. Open an [R](http://www.r-project.org/) session and run the following command:
```R
install.packages('ROpenFLUID_x.x.x-x.tar.gz',repos=NULL)
```
_in the previous command, replace x.x.x-x with the correct version number (e.g. 2.1.9-20190918)_

## Using OpenFLUID within [R](http://www.r-project.org/)

* The ROpenFLUID package reference manual is available in the [Manuals](../start/manuals.md) section.
* All OpenFLUID commands in R are prefixed by OpenFLUID. (''e.g. OpenFLUID.openDataset, OpenFLUID.runSimulation, ...'')


## Examples

_(The following commands are illustrated with the example "Primitives" delivred with OpenFLUID)_


* Running a project as a black box. This command allows a low interaction level between R and OpenFLUID environnement, the pre- and post-processing of a simulation are performed without the ROpenFLUID package commands.
```R
library("ROpenFLUID")  # should be done only once

OpenFLUID.runProject("/path/to/openfluid/examples/Primitives")
```


* Opening an input dataset, running the simulation and visualising the temporal evolution of the variable "var1" of the unit "8" of class "unitsA"
```R
ofsim = OpenFLUID.openDataset("/path/to/openfluid/examples/Primitives/IN")
OpenFLUID.setCurrentOutputDir("/path/to/openfluid/examples/Primitives/OUT")
OpenFLUID.addVariablesExportAsCSV(ofsim,"unitsA",8,"var1")  # to export all variables of class "unitsA", do not specify either unit identifiers or variable names
OpenFLUID.runSimulation(ofsim)
var1A8 = OpenFLUID.loadResult(ofsim,"unitsA",8,"var1")
plot(var1A8$datetime,var1A8$var1,type="l")
```


* Opening an input dataset, modifying simulation default time step and running the simulation
```R
OpenFLUID.setDefaultDeltaT(ofsim,1800)
OpenFLUID.runSimulation(ofsim)
```


* Opening an input dataset, modifying parameter "gmult" of the simulator "examples.primitives.unitsA.up" and running the simulation
```R
gmult = as.numeric(OpenFLUID.getSimulatorParam(ofsim,"examples.primitives.unitsA.up","gmult"))  # warning: the return type of this command is "character"
OpenFLUID.setSimulatorParam(ofsim,"examples.primitives.unitsA.up","gmult",0.5*gmult)
OpenFLUID.runSimulation(ofsim)
```


* Opening an input dataset, modifying attribute "inivar1" of the unit "8" of class "unitsA" and running the simulation
```R
inivar1 = as.numeric(OpenFLUID.getAttribute(ofsim,"unitsA",8,"inivar1"))  # warning: the return type of this command  is "character"
OpenFLUID.setAttribute(ofsim,"unitsA",8,"inivar1",inivar1+1)
OpenFLUID.runSimulation(ofsim)
```
