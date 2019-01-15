## Getting the sources

The OpenFLUID source code is available on our [GitHub organization](https://github.com/OpenFLUID).
You may clone the repositories to work with the source code. More information are available on the [Working with source code](srccodework.md) page.


## Building on linux

### Prerequisites


Install the required libraries and tools using the following command:

Ubuntu 14.04 and higher, Debian Jessie and higher
```sh
sudo apt-get install build-essential lsb-release g++ gfortran git cmake \
                     texlive-latex-extra texlive-fonts-extra latex2html doxygen \
                     libboost-all-dev libgdal1-dev libgeos++-dev \
                     qt5-default qtbase5-dev-tools qttools5-dev-tools libqt5svg5-dev \
                     p7zip-full gnuplot graphviz python2.7
```

Fedora 25 and higher
```sh
sudo dnf install gcc-c++ gcc-gfortran make cmake git \
                 boost-devel gdal-devel geos-devel \
                 qt5-qttools-devel qt5-qtbase-devel qt5-qtsvg-devel qt5-qtwebkit-devel qt5-qtsvg-devel \
                 p7zip gnuplot graphviz doxygen rpm-build redhat-lsb
```

### Configure the build

* create a build directory in your source directory ( e.g. \_build)
* go into this  directory
* run the cmake command, for development or release build

__Example for development build__
```sh
mkdir _build
cd _build
cmake ..
```

__Example for release build__
```sh
mkdir _build
cd _build
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
```

The following options are available to control the build process

* `-DOFBUILD_ENABLE_SANITIZER` : Enable the compiler sanitizer to track memory address errors (default value : `OFF`)
* `-DOFBUILD_ENABLE_TESTING` : Enable the build of tests (`ON` in Debug mode, `OFF` in Release mode)
* `-DOFBUILD_ENABLE_HEAVYTESTING` : Enable the build of tests (default value : `OFF`)


### Build

* Run "make" from your build directory
```sh
make
```

### Testing

* Run "ctest" from your build directory (available in development build only)
```sh
ctest
```

### Packaging and installation

#### Creating binary packages (recommended way for installation)

* Run "cpack" from your build directory (available in release build only)
```sh
cpack
```

#### Creating source packages

* Run "make package_source" from your build directory
```sh
 make package_source
```

#### Raw installation (not recommended)

* Run "make install" from your build directory
```sh
sudo make install
```

### Full example : Building release package from develop branch

This example shows how to get the current sources from the OpenFLUID git repository, and create a package for installation.  
The previously mentioned [prerequisites](#prerequisites) should be satisfied.

```sh
git clone https://github.com/OpenFLUID/openfluid
cd openfluid
mkdir _build
cd _build
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make
cpack
```


## Building on MacOS

!!! note
    These instructions are for OpenFLUID 2.1.5+.

### Prerequisites

**XCode**

* Install the latest version of [XCode](https://developer.apple.com/xcode/) with command line tools.


**Dependencies**

* Open a Terminal and install brew package manager if not already installed ([http://brew.sh/](http://brew.sh))
```sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* Update brew to be sure to have the latest version installed
```sh
brew update
```

* Install dependencies packages using brew
```sh
brew install cmake qt5 boost geos gdal rapidjson doxygen p7zip gnuplot
```

### Configure the build

1. Open a Terminal, and go into the OpenFLUID sources directory
1. Add the Qt bin path to the PATH environment variable
1. Create a build directory in your source directory ( e.g. "\_build")
1. Go into this  directory
1. Run the cmake command, for development or release build

```sh
export PATH=$PATH:$(brew --prefix qt5)/bin
```

_Example for release build_
```sh
mkdir _build
cd _build
cmake .. -DCMAKE_PREFIX_PATH=$(brew --prefix qt5)/lib/cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local
```


_Example for development build_
```sh
mkdir _build
cd _build
cmake .. -DCMAKE_PREFIX_PATH=$(brew --prefix qt5)/lib/cmake
```


### Build

Run the make command from the \_build directory
```sh
make
```

### Packaging

After having built OpenFLUID in release mode, run the following command from the build directory
```sh
cmake -P ofpack-osx-brewcask.cmake
```

## Building on Windows

!!! note
    These instructions are for OpenFLUID 2.1.0 and later versions.


### Prerequisites

#### Tools

**CMake**

* Download the [CMake](http://www.cmake.org) installer version 2.8.12 or higher, and install CMake


**Qt**

* Download the [Qt](http://qt-project.org/downloads) installer for Windows with MinGW, version 5.4 or higher
* Install Qt


**Doxygen**

* Download the [Doxygen](http://www.stack.nl/~dimitri/doxygen/) installer, and install Doxygen


#### Support libraries

OpenFLUID requires Boost, GEOS, GDAL, RapidJSON to be built. In order to install those development libraries, you can use the provided installer (recommended) or build the libraries by yourself.  
<br/>

##### The easy way: use the provided installer (recommended)

* Download the [build support installer](http://www.openfluid-project.org/resources/tools/OpenFLUID-buildsupport-win32.exe)
* Install it (e.g. in C:\OpenFLUID-buildsupport)


##### The hard way: build the libraries by yourself

**Git**

* Download the [Git installer](https://git-scm.com/download/win), and install Git


** MSYS **

* Download the [MSYS](http://downloads.sourceforge.net/mingw/MSYS-1.0.11.exe) installer (version 1.0.11 is recommended)
* Run MSYS installation. During the installation, change the MinGW path to the Qt MINGW path (e.g. c:/Qt/Tools/mingw48_32).  


** Boost **

* Download the [Boost](http://www.boost.org) sources package version 1.54 or higher, and uncompress it in a folder of your choice (different from C:\OpenFLUID-buildsupport, e.g. C:\OpenFLUID-buildsupport-sources\Boost).
* Copy the the content of the source include directory (e.g. C:\OpenFLUID-buildsupport-sources\Boost\include) into the install include directory (e.g. C:\OpenFLUID-buildsupport\include)

_For an OpenFLUID Debug build only_

* Create a \_build folder in the boost sources folder (e.g. C:\OpenFLUID-buildsupport-sources\Boost\\\_build)
* Open the Qt MinGW console, go to the boost sources folder, and run the following command
```sh
 bootstrap gcc  
 b2 install --build-dir=_build --toolset=gcc --prefix="C:\OpenFLUID-buildsupport" \
   variant=release threading=multi link=shared --with-test
```

**GEOS**

* Download [GEOS source](http://download.osgeo.org/geos/geos-3.3.8.tar.bz2) archive (3.3.8 or later recommended), and uncompress it in a folder of your choice (different from C:\OpenFLUID-buildsupport, e.g. C:\OpenFLUID-buildsupport-sources\GEOS)
* Build GEOS through MSYS using the following instructions
```sh
 ./configure --prefix=/c/OpenFLUID-buildsupport --build=mingw32 \
   --enable-static=no --enable-shared=yes --disable-inline
 make
 make install
```
* Create a file called <tt>geos-config.cmake</tt> in C:\OpenFLUID-buildsupport\share, and put the following contents in it (adapt to the GEOS version you are installing)
  SET(GEOS_VERSION "3.3.8")

This will build and install GEOS libraries and tools in C:\OpenFLUID-buildsupport  


**GDAL**

* Download [GDAL source](http://trac.osgeo.org/gdal/wiki/DownloadSource) archive, and uncompress it in a folder of your choice (different from C:\OpenFLUID-buildsupport, e.g. C:\OpenFLUID-buildsupport-sources\GDAL)
* Read instructions from [GDAL wiki for building with MinGW](http://trac.osgeo.org/gdal/wiki/BuildingWithMinGW). The GNUMakefile modifications must be performed as recommended
* Build GDAL through MSYS using the following instructions
```sh
 ./configure --prefix=/c/OpenFLUID-buildsupport --build=mingw32 \
   --without-python --without-libtool \
   --with-libz=internal --with-libtiff=internal \
   --with-geos=/c/OpenFLUID-buildsupport/bin/geos-config
 make
 make install
```
This will build and install GDAL libraries and tools in C:\OpenFLUID-buildsupport

### Configure the build

* Create a build directory in the OpenFLUID source directory ( e.g. "\_build-devel" or "\_build-release")
* From the Qt console, go into this  directory
* From the Qt console, set the SUPPORT_DIR environment variables, then run the cmake command, for development or release build, with the MinGW generator

_Development build_
```sh
mkdir _build-devel
cd _build-devel
set SUPPORT_DIR=C:\OpenFLUID-buildsupport
cmake .. -G "MinGW Makefiles" -DCMAKE_PREFIX_PATH=C:\OpenFLUID-buildsupport
```

_Release build_
```sh
mkdir _build-release
cd _build-release
set SUPPORT_DIR=C:\OpenFLUID-buildsupport
cmake .. -G "MinGW Makefiles" -DCMAKE_PREFIX_PATH=C:\OpenFLUID-buildsupport \
  -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=..
```

The cmake command must be run every time a CMakeLists.txt file is modified, or a source file is added or removed.


### Build

* From the command prompt, run "mingw32-make" in the build directory
```sh
mingw32-make
```


### Testing

1. From the command prompt, add the  \_build-devel/dist/bin folder to the PATH environment variable
1. From the command prompt, run "ctest" in the build directory
```sh
ctest
```


### Packaging

* From the command prompt, run "cpack" from the build directory
```sh
 cpack -G "NSIS"
```
