## Source code repositories

Code and tickets are hosted on GitHub in the [OpenFLUID Project](https://github.com/OpenFLUID/openfluid). A more 
comprehensive description of the versionning strategy is available [here](srccodework.md).

## Dependencies

The libraries are similar to those to build OpenFLUID : see [OpenFLUID build page](build.md) section corresponding to your system.

The main OpenFLUID dependencies are:

* **Boost**
* **Qt6**
* **GDAL**

To build documentation:

* **Pandoc**
* **LaTeX**
* **Doxygen**

For usage:

* **gnuplot**
* **graphviz**

## Development environment


### Build

* **g++**
* **make**
* **CMake**



### IDE

The development editor choice is up to you, we list here two examples suitable for development in C++:

* **[Visual Studio Code](https://code.visualstudio.com/)**
* **[Atom](https://atom.io/)**

And for form/UI design:

* **QtCreator** (shipped with Qt)

### Analysis tools

* **Valgrind**, for analysis of segmentation faults and other memory issues

### Continuous integrations services

* **[GitHub Actions](https://github.com/OpenFLUID/openfluid/actions/workflows/CI.yaml)**
  [![Ubuntu](https://github.com/OpenFLUID/openfluid/actions/workflows/CI-ubuntu.yaml/badge.svg)](https://github.com/OpenFLUID/openfluid/actions/workflows/CI-ubuntu.yaml) [![macOs](https://github.com/OpenFLUID/openfluid/actions/workflows/CI-macos.yaml/badge.svg)](https://github.com/OpenFLUID/openfluid/actions/workflows/CI-macos.yaml) [![Windows](https://github.com/OpenFLUID/openfluid/actions/workflows/CI-windows.yaml/badge.svg)](https://github.com/OpenFLUID/openfluid/actions/workflows/CI-windows.yaml)  
  Used for OpenFLUID test on linux, windows and mac and package builds for linux and mac.  
  See `.github/workflows/*.yaml` configuration file in the OpenFLUID repository.

