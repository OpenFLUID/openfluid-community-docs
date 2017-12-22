The creation and build of a simulator is performed using the OpenFLUID-DevStudio application.  
Make sure you have [installed the required tools](scidevenv.md) for building simulators.  
<br/>

!!! note "Language"
    As the OpenFLUID-DevStudio UI is multilingual, the items cited below such as menu names or labels can be in another language than english for you installation.

## Create a new simulator

Using the OpenFLUID-DevStudio:

1. Go to menu _File > New ware > Simulator..._
1. A dialog window opens to define the main characteristics of your simulator. You can let the defauilt values or customize the various items such as class name or file name. Note that the _Ware ID_ is important as it is the unique ID to identify your simulator, so choose it carefully. You may consult the [naming conventions](simdatanaming.md) which can help you to choose a correct ID.
1. Once the dialog window filled, click the _OK_ button and the simulator source code is automatically created.


## Configure and build a simulator

### Configuration phase

The configuration phase must be performed at least once.  
It is available using the _Configure_ button from the main toolbar, or using the menu _Build > Configure ware_.  
This phase checks the dependencies (tools and libraries) required to build the simulator. It can be performed either in _Release_ mode for performance optimization (mode by default, recommended) or in _Debug_ mode to be used with an external debugger.

### Build phase

The build phase must be performed each time the source code has been modified.  
It is available using the _Build_ button from the main toolbar, or using the menu _Build > Build ware_.  
This phase builds thes simulator source code into a binary plugin for the OpenFLUID platform. It can be performed either in _Build and install_ mode to make the simulator immediately available for simulations (mode by default, recommended) or in _Build only_ mode for intermediate builds for example.
