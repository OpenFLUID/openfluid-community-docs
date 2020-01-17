## Source code repositories

Code and tickets are hosted on GitHub in the [OpenFLUID Project](https://github.com/OpenFLUID/openfluid). A more 
comprehensive description of the versionning strategy is available [here](srccodework.md).

## Dependencies

The libraries are similar to those to build OpenFLUID : see [OpenFLUID build page](build.md) section corresponding to your system.

The main OpenFLUID dependencies are:

- **Boost**
- **Qt5**
- **RapidJSON**
- **GDAL**
- GEOS (optional)

To build documentation:

- **LaTeX**
- **Doxygen**

For usage:

- **gnuplot**
- **graphviz**

## Development environment


### Build

- **g++**
- **make**
- **CMake**



### IDE

The development editor choice is up to you, we list here two examples suitable for development in C++:

- **[Visual Studio Code](https://code.visualstudio.com/)**
- **[Atom](https://atom.io/)**

And for form/UI design:

- **QtCreator** (shipped with Qt)

### Analysis tools

- **Valgrind**, for analysis of segmentation faults and other memory issues

### Continuous integrations services

- **[Travis](https://travis-ci.org/OpenFLUID/openfluid)**, used for OpenFLUID test and package builds for linux and mac. See `.travis.yml` configuration file in the OpenFLUID repository.

- **[Appveyor](https://ci.appveyor.com/project/fabrejc/openfluid-hm6ac/branch/develop)**, used for OpenFLUID test build for windows. See `.appveyor.yml` configuration file in the OpenFLUID repository.
