## General information

### What is OpenFLUID?

OpenFLUID is a software environment for spatial modelling landscapes in landscapes, mainly focused on fluxes. It is made of the OpenFLUID framework, OpenFLUID software applications, and uses simulators for spatialized dynamics.  
See the [OpenFLUID overview](http://www.openfluid-project.org/about) for more details.

### What are OpenFLUID simulators?

OpenFLUID simulators are computational codes which can be dynamically plugged to the OpenFLUID framework in order to build coupled models adapted to the modelling context and objectives, and then run simulations based on these coupled models.  
See the [framework and simulators overview](http://www.openfluid-project.org/about/) for more details.

### What is the OpenFLUID license?

OpenFLUID is distributed online under the GPLv3 license, but can be licensed with different terms if needed  
See the [OpenFLUID license](../general/license.md) page for license text.

### On which operating systems OpenFLUID is available?

OpenFLUID works on Linux, Windows and MacOS systems. It is developed on linux system, and has been tested under Linux 64 bits for Ubuntu, Debian and Fedora distributions, Windows 10 (64bits). It should run on other compatibles operating systems.  
It is available on MacOSX as an HomeBrew package.  
As far as possible, we recommend to run OpenFLUID on linux systems as it is the main development system.  
See the [Downloads](http://www.openfluid-project.org/downloads/) page for a list of available packages and installers.

### I need help about OpenFLUID, what can I do?

First of all, you are really encouraged to read the [manuals](../start/manuals.md).  
You can also get help from the OpenFLUID community using the mailing-list or the dedicated Slack workspace. See the [support](../start/support.md) page for details.

### I found a bug or I would like to suggest a feature, what should I do?

You can report a bug or suggest a new feature by filling a New Issue on the [issues ticket system](http://github.com/OpenFLUID/openfluid).

## Installation

### How do I get the latest OpenFLUID packages for installation?

The latest OpenFLUID packages are available from the [OpenFLUID downloads page](http://www.openfluid-project.org/downloads/)

### How do I get the current source code and build OpenFLUID?

You can get the current OpenFLUID source code from our git repository on GitHub, using the following command:
```sh
git clone https://github.com/OpenFLUID/openfluid
```

This source code can be built following the [build instructions](../coredev/build.md).

## Using OpenFLUID

### How do I add paths to search for simulators?

When using the openfluid command line application, this can be done using the `-p` option. In this case, the added paths are enabled for the current launched simulation.

When using the openfluid-builder application, this can be done through the preferences dialog box. In this case, the added paths are persistant until they are removed from the preferences.

### How to enable verbose display while executing simulations?

When running a simulation using the openfluid command line application, you can add the `-v` command line option to enable the verbose display during the execution.  

### How to generate a performance profile while executing simulations?

When running a simulation using the openfluid command line application, you can use the `-k` command line option to enable profiling mode giving information about the time spent in the each part of the simulation. Using the OpenFLUID-Builder application, the profiling can be enabled in the _Simulation configuration_ tab.  
The profiling results are stored in 3 files located in the output directory:

* `openfluid-profile-timeindex.log` contains the time spent in each simulator at each time index
* `openfluid-profile-cumulative.log` contains the cumulative time spent in each simulator index
* `openfluid-profile-schedule.log` contains the scheduling order of each simulator at each time index

You can also consult the simulation log file named `openfluid-messages.log` which is also located in the output directory.

## Development of simulators

### How do I create and build a new simulator?

See the [manuals](../start/manuals.md) or the [create and build a simulator](../scidev/simbuild.md) page.

### What coding style should I use for writing source code?

The best coding style for your simulators development is the coding style you are familiar with, as far as it is shared and applied in the work group you are belonging to. If you are not using a specific coding style, we recommend to use the [OpenFLUID coding style](../coredev/codestyle.md).

### How can I log information, warnings and errors messages during simulations?

You can log informations from your simulators using the OpenFLUID logging feature. This is the recommended way to log messages. Avoid using `std::cout` or `std::cerr` as the output to screen is not guaranteed on all systems.  
For details, see the [manuals](../start/manuals.md), and go to the _Development of the simulator source code_ section.

### How can I store data and status from one time step to the next time step?

In this case, you can use "ID-maps" structures as attribute of the C++ class of your simulator .  
For details, see the see the [manuals](../start/manuals.md), and go to the _Development of the simulator source code_ section.

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

For downloaded simulators, reinstall the new version of the simulators, corresponding to the OpenFLUID version you have just installed.  

For your own simulators, you have to rebuild them for linking with newly installed OpenFLUID framework. See the [build a simulator](../scidev/simbuild.md) page for more details about building simulators from source code.

### I installed a new OpenFLUID version on Linux and the OpenFLUID-Builder icon does not show, what should I do?

Just restart your computer, and the OpenFLUID-Builder icon should reappear.  

### I get a Qt version issue when trying to switch to a more recent version, how to fix it?

It is probably related with a conflict between Qt5 and Qt6. We will consider here recent OS where Qt6 is the expected version.

If  `qmake --version` targets Qt5 or displays an error like `qmake: could not exec '/usr/lib/qt5/bin/qmake': No such file or directory`

1) Check `qmake` install: `sudo find /usr -name qmake 2>/dev/null`  
2) Configure `qmake` with `update-alternatives`  (execute second line only if a version of `qmake` for Qt5 is found)
```
sudo update-alternatives --install /usr/bin/qmake qmake /usr/lib/qt6/bin/qmake 20 
sudo update-alternatives --install /usr/bin/qmake qmake /usr/lib/qt5/bin/qmake 10 
```
3) Select `qmake` version by executing `sudo update-alternatives --config qmake` and chose **Qt6** in the list  
4) Ensure qmake version is consistent: `qmake --version`

### When i recompile a ware more than once, it fails. How to handle this?
This is a known issue in OpenFLUID since release 2.2.0. If this happens you should clean the build directory (use "purge" option in CLI or DevStudio dashboard) and rerun the configuration and compilation steps.

## Known issues

### All systems

- Potential crash when quitting Builder with an example project opened. (Qt5 systems)

### Fedora

- Examples projects and simulators cannot be installed.

### Windows

- Unable to install wares when Builder is open under Windows


If you detect any bugs, please check for [Github issues](https://github.com/OpenFLUID/openfluid/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22confirmed%20bug%20%3Abug%3A%22) first. If it is not mentioned, you can [contact us](../start/support.md).