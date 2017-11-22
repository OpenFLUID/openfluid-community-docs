## Getting the sources

!!! danger "TODO"
    To be written


## Building on linux

### Prerequisites


Install the required libraries and tools using the following command:

Ubuntu 13.10 and higher, Debian Jessie and higher
```sh
sudo apt-get install build-essential lsb-release g++ gfortran git cmake \
                     texlive-latex-extra texlive-fonts-extra latex2html doxygen \
                     libboost-all-dev libqt4-dev libgdal1-dev libgeos++-dev \
                     p7zip-full gnuplot graphviz python2.7
```

Fedora 21 and higher
```sh
sudo yum install gcc-c++ gcc-gfortran make cmake git \
                 boost-devel qt-devel gdal-devel geos-devel \
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

!!! danger "TODO"
    To be written


## Building on Windows

!!! danger "TODO"
    To be written
