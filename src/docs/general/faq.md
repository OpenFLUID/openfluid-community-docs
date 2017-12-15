## General information

### What is OpenFLUID?

OpenFLUID is a software environment for modelling landscapes functionning, mainly focused on spatialized fluxes. It is made of the OpenFLUID framework, OpenFLUID software applications, and uses simulators for spatialized dynamics.  
See the [OpenFLUID overview](http://www.openfluid-project.org/index.php?page=about) for more details.

### What are OpenFLUID simulators?

OpenFLUID simulators are computational codes which can be dynamically plugged to the OpenFLUID framework in order to build coupled models adapted to the modelling context and objectives, and then run simulations based on these coupled models.  
See the [framework and simulators overview](http://www.openfluid-project.org/index.php?page=about#softdesign) for more details.

### What is the OpenFLUID license?

OpenFLUID is distributed online under the GPLv3 license, but can be licensed with different terms if needed  
See the [OpenFLUID license](http://www.openfluid-project.org/index.php?page=license) page for license text.

### On which operating systems OpenFLUID is available?

OpenFLUID works on Linux, Windows and MacOSX systems. It is developed on linux system, and has been tested under Linux 64 bits for Ubuntu, Debian and Fedora distributions, Windows 7 and Windows 8 (32bits). It should run on other compatibles operating systems. It is regularly rebuild on MacOSX, but not packaged and distributed for this system  
As far as possible, we recommend to run OpenFLUID on linux systems as it is our development system.  
See the [Downloads](http://www.openfluid-project.org/index.php?page=dloads) page for a list of available packages and installers.

### I need help about OpenFLUID, what can I do?

First of all, you are really encouraged to read the [Manuals](../start/manuals).  
You can also get help from the OpenFLUID community using the mailing-list or the IRC channel. See the [support](../start/support) page for details.

### I found a bug or I would like to suggest a feature, what should I do?

You can report a bug or suggest a new feature by filling a New Issue on the [Issues ticket system](http://github.com/OpenFLUID/openfluid).

## Installation

### How do I get the latest OpenFLUID packages for installation?

The latest OpenFLUID packages are available from the [OpenFLUID downloads page](http://www.openfluid-project.org/index.php?page=dloads)

### How do I get the current source code and build OpenFLUID?

You can get the current OpenFLUID source code from our git repository on GitHub, using the following command:
```sh
git clone https://github.com/OpenFLUID/openfluid
```

This source code can be built following the [build instructions](../coredev/build).

## Using OpenFLUID

### How do I add paths to search for simulators?

When using the openfluid command line application, this can be done using the "-p" option. In this case, the added paths are enabled for the current launched simulation.

When using the openfluid-builder application, this can be done through the preferences dialog box. In this case, the added paths are persistant until they are removed from the preferences.

### How to get more details about the simulations executions?

When using the openfluid-engine application, you can use the "-v" command line option to get a verbose run.  
You can also use the "-k" command line option to enable profiling mode giving information about the time spent in the different part of the simulation. The profiling results are stored in the profile.dat and profile_steps.dat files, located in the output directory.  
Finally, you can consult the simulators log files located in the output directory.

## Development of simulators

### How do I create and build a new simulator?

See the [Create and build a simulator](../scidev/simbuild) page.

### What coding style should I use for writing source code?

The best coding style for your simulators development is the coding style you are familiar with, as far as it is shared and applied in the work group you are belonging to. If you are not using a specific coding style, we recommend to use the [OpenFLUID coding style](../coredev/codestyle).

### How can I log information, warnings and errors messages during simulations?

You can log informations from your simulators using the OpenFLUID logging feature. This is the recommended way to log messages. Avoid using std::cout or std::cerr as the output to screen is not guaranteed on all systems.  
For details, see the [manuals](../start/manuals), and go to the "Development of the simulator source code" of the manual.

### How can I store data and status from one time step to the next time step?

In this case, you can use "ID-maps" structures as attribute of the C++ class of your simulator .  
For details, see the see the [manuals](../start/manuals), and go to the "Development of the simulator source code" of the manual.

## Troubleshooting

### How can I resolve the "Too many open files" error?

This error is due to operating system limitations. It often occurs when a lot of simulation results are set to be saved to files.  
It can be resolved by limiting the number of outputs by adapting the outputs configuration.  

The other method is to modify the operating system configuration (when possible).  
On linux systems, this limitation can be disabled by adding the following lines to the /etc/security/limits.conf file
```txt
* soft nofile 65535
* hard nofile 65535
```

### I installed a new OpenFLUID version and OpenFLUID doesn't start anymore, why?

When installing a new version of OpenFLUID, you may experience problems such as OpenFLUID-Builder does not start anymore. In this case, you have to update the installed simulators.

For downloaded simulators (such as the MHYDAS model), reinstall the new version of the simulators, corresponding to the OpenFLUID version you have just installed.  

For your own simulators, you have to rebuild them for linking with new OpenFLUID framework. See the [build a simulator](../scidev/simbuild) page for more details about building simulators from source code.

### I installed a new OpenFLUID version on Linux and the OpenFLUID-Builder icon does not show, what should I do?

Just restart your computer, and the OpenFLUID-Builder icon should reappear.  
