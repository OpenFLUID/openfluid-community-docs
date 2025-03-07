!!! note "OpenFLUID Versions"
    The following instructions are for OpenFLUID versions 2.0.x and later.  
    As older versions are deprecated, we do not provide online instructions for these older versions. However, you can [contact us](../start/support.md)

!!! note "ROpenFLUID"
    For installation notes about the ROpenFLUID package for R, please report to the [R OpenFLUID dedicated page](../external/ropenfluid.md)



## Linux


### OpenFLUID 2.2.0+

_Since OpenFLUID 2.2.0, OpenFLUID relies on Qt5 or Qt6 for its UI_

#### Ubuntu 22.04 and higher, Debian 12 and higher

1) Download the [OpenFLUID package](http://www.openfluid-project.org/downloads/) corresponding to the Ubuntu version you are using and install it
```sh
sudo apt install </path/to/openfluid/debfile>
# where </path/to/openfluid/debfile> is the path to the downloaded deb file for OpenFLUID.
```

<small>
`apt install` should install automatically following dependencies: `build-essential g++ cmake git debhelper pkg-config doxygen, libboost-all-dev libgdal-dev libgeos++-dev, qt6-base-dev, qt6-tools-dev, libqt6svg6-dev, qt6-tools-dev-tools, qt6-l10n-tools, gnuplot p7zip-full graphviz`
</small>

2) Check the installation by typing the following command in a terminal
```sh
openfluid --version
```


To build <strong>ware documentation</strong>, you will require following packages: `texlive-latex-base`, `texlive-fonts-extra`, `pandoc` (and `pandoc-citeproc` for Ubuntu 22.04 and below)

If your system has issues by having both Qt5 and Qt6, see [related section in troubleshooting page](../general/faq.md#i-get-a-qt-version-issue-when-trying-to-switch-to-a-more-recent-version-how-to-fix-it).

#### Linux Fedora 40 and higher


1) Download the [OpenFLUID package](http://www.openfluid-project.org/downloads/) corresponding to the Fedora version you are using and install it
```sh
sudo rpm -i </path/to/openfluid/rpmfile>
# where </path/to/openfluid/rpmfile> is the path to the downloaded rpm file for OpenFLUID.
```

<small>
`rpm` should install automatically following dependencies: `make, gcc-c++, gcc-gfortran, cmake, boost-devel >= 1.54, gdal-devel, libcurl, p7zip, gnuplot, graphviz, git, qt6-qttools-devel, qt6-qtbase-devel, qt6-qtsvg-devel, qt6-qtwebengine-devel`
</small>

2) Check the installation by typing the following command in a terminal
```sh
openfluid --version
```

To build <strong>ware documentation</strong>, you will require following packages: `texlive-scheme-full`, `texlive-collection-fontsextra`, `pandoc`


### OpenFLUID 2.1.5 to 2.1.11

_Since OpenFLUID 2.1.5, OpenFLUID for Linux systems also relies on Qt5_

#### Ubuntu 16.04 and higher, Debian 8 and higher

1) Install required libraries and development tools  :
```sh
sudo apt-get install build-essential g++ cmake git debhelper pkg-config doxygen \
                     libboost-all-dev libgdal-dev libgeos++-dev \
                     qt5-default qtbase5-dev-tools qttools5-dev-tools libqt5svg5-dev \
                     gnuplot p7zip-full graphviz
```

!!! warning
    Since Ubuntu 22.04, the package `qt5-default` is neither recognized by the system nor necessary, so it is recommended to remove it from the package list to install


2) Download the [OpenFLUID package](http://www.openfluid-project.org/downloads/) corresponding to the Ubuntu version you are using and install it
```sh
sudo dpkg -i </path/to/openfluid/debfile>
# where </path/to/openfluid/debfile> is the path to the downloaded deb file for OpenFLUID.
```

3) Check the installation by typing the following command in a terminal
```sh
openfluid --version
```


#### Linux Fedora 25 and higher

1) Install required libraries and development tools  :
```sh
sudo dnf install -y gcc-c++ gcc-gfortran make cmake git \
                    boost-devel gdal-devel geos-devel \
                    qt5-qttools-devel qt5-qtbase-devel qt5-qtsvg-devel qt5-qtwebkit-devel qt5-qtsvg-devel \
                    p7zip gnuplot graphviz doxygen rpm-build redhat-lsb
# use dnf instead of yum on recent Fedora versions
```
2) Download the [OpenFLUID package](http://www.openfluid-project.org/downloads/) corresponding to the Fedora version you are using and install it
```sh
sudo rpm -i </path/to/openfluid/rpmfile>
# where </path/to/openfluid/rpmfile> is the path to the downloaded rpm file for OpenFLUID.
```
3) Check the installation by typing the following command in a terminal
```sh
openfluid --version
```


### OpenFLUID 2.1.0 - 2.1.4

#### Ubuntu 14.04&rarr;16.04 and Debian Jessie

1) Install required libraries and development tools  :
```
sudo apt-get install g++ cmake debhelper pkg-config doxygen \
                     libboost-all-dev libqt4-dev libgdal1-dev libgeos++-dev \
                     gnuplot p7zip-full graphviz
```
2) Download the [OpenFLUID package](http://www.openfluid-project.org/downloads/) corresponding to the Ubuntu version you are using and install it
```sh
sudo dpkg -i </path/to/openfluid/debfile>
# where </path/to/openfluid/debfile> is the path to the downloaded deb file for OpenFLUID.
```

3) Check the installation by typing the following command in a terminal
```sh
openfluid --version
```


#### Linux Fedora 21+

1) Install required libraries and development tools  :
```sh
sudo yum install -y gcc-c++ gcc-gfortran make cmake git \
                    boost-devel qt-devel gdal-devel geos-devel \
                    p7zip gnuplot graphviz doxygen rpm-build redhat-lsb
# use dnf instead of yum on recent Fedora versions
```
2) Download the [OpenFLUID package](http://www.openfluid-project.org/downloads/) corresponding to the Fedora version you are using and install it
```sh
sudo rpm -i </path/to/openfluid/rpmfile>
# where </path/to/openfluid/rpmfile> is the path to the downloaded rpm file for OpenFLUID.
```
3) Check the installation by typing the following command in a terminal
```sh
openfluid --version
```

### OpenFLUID 2.0.x

#### Ubuntu

Preliminary configuration step **on Ubuntu 12.04 only**, for more recent versions of CMake, GDAL and GEOS libraries
```sh
sudo add-apt-repository ppa:ubuntugis/ppa
sudo add-apt-repository ppa:czchen/travis-ci
sudo apt-get update
```

1) Install required libraries and development tools  :
```sh
sudo apt-get install g++ cmake debhelper pkg-config doxygen \
                     libboost-all-dev libqt4-dev libgdal1-dev libgeos++-dev \
                     gnuplot p7zip-full graphviz
```

2) Download the [OpenFLUID package](http://www.openfluid-project.org/downloads/) corresponding to the Ubuntu version you are using and install it
```sh
sudo dpkg -i </path/to/openfluid/debfile>
# where </path/to/openfluid/debfile> is the path to the downloaded deb file for OpenFLUID.
```

3) Check the installation by typing the following command in a terminal
```
openfluid --version
```


## MacOS

### OpenFLUID 2.1.5+

!!! warning
    Since OpenFLUID 2.1.5, the macOS installation relies on the [Brew packaging tool](https://brew.sh/).  
    It is still an unstable packaging, and is available only for macOS 10.14 _Mojave_ and 10.15 _Catalina_


Install Brew (_Task to perform only once, see also [https://brew.sh/](https://brew.sh/)_)
```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Add OpenFLUID tap for Brew _(Task to perform only once)_
```sh
brew tap OpenFLUID/openfluid
```

Install OpenFLUID using Brew (with `--no-quarantine` option to avoid Gatekeeper restrictions in recent MacOS versions)
```sh
brew cask install --no-quarantine openfluid
```


### OpenFLUID 2.1.3 - 2.1.4

!!! warning
    The OSX installer is only available for OpenFLUID 2.1.3 and later versions.  
    It is still an early preview release, and has only been tested on macOS 10.11

1) Download the [OpenFLUID .dmg file](http://www.openfluid-project.org/downloads/) and mount it in the Finder.  

2) Read installation instructions. Notice brew dependencies.  

3) Install the OpenFLUID package  

4) If you plan to develop your own simulators, you have to install Xcode and Xcode Command line Tools  


## Windows

1) Download [OpenFLUID for Windows](http://www.openfluid-project.org/downloads/) and install it using the automatic installer. This installer includes the required libraries and sets the required environment variables for OpenFLUID.

2) Check the installation by typing the following command in a command prompt
```sh
 openfluid --version
```

3) If you plan to use advanced OpenFLUID observers or develop your own simulators, observers or builder-extensions: you are really encouraged to download and install these additional support tools for Windows, available from the [OpenFLUID downloads page](http://www.openfluid-project.org/downloads/).

### For older versions or custom install
Instead of the OpenFLUID-support installer, you may want to install dependencies by yourself (this part is not up to date anymore in 2024)

* Install the [Qt 5.9.6 package for Windows](http://download.qt.io/archive/qt/5.9/5.9.6/qt-opensource-windows-x86-5.9.6.exe). During the installation process, select MinGW 5.3 32bits in `Qt > Qt5.9.6` and `Qt > Tools` sections
* Install the [CMake tool for Windows](http://www.cmake.org/download/)
* Open the OpenFLUID-DevStudio application, go to the _Edit > Preferences..._ menu. In the preferences dialog, go to the _Development tools_ section and run the Qt detection process by using the _Detect Qt development tools (MinGW)_ button.


## Containers

OpenFLUID can be used through containerization (Operating-system-level virtualization), using Docker or Singularity software.  


### Docker

[Docker](https://www.docker.com/) images and usage instructions are available on Docker Hub : [https://hub.docker.com/r/openfluid/openfluid/](https://hub.docker.com/r/openfluid/openfluid/).  
<br/>
To use these images, the Docker container platform is required. Installation intructions are available at [https://docs.docker.com/install/](https://docs.docker.com/install/)


### Singularity

[Singularity](https://singularity.lbl.gov/) images uses Docker images hosted on Docker Hub.
To build a Singularity image based on the latest OpenFLUID version, run the following command (with sudo if needed)
```sh
singularity build <imgfile> docker://openfluid/openfluid
```
*(Replace `<imgfile>` by the filename of the image to build, e.g. openfluid.img)*  
<br/>

To build a Singularity image based on a specific OpenFLUID version, run the following command (with sudo if needed)
```sh
singularity build <imgfile> docker://openfluid/openfluid:<tag>
```
*(Replace `<tag>` by the specific OpenFLUID version tag for the image to build, e.g. `2.1.9`. Available tags are listed on [https://hub.docker.com/r/openfluid/openfluid/](https://hub.docker.com/r/openfluid/openfluid/))*  
<br/>

Once the image is created, use the `singularity shell` command or execute the image from the command line
```sh
singularity shell <imgfile>
```
or
```sh
./<imgfile>
```  
<br/>
Installation instructions for Singularity are available at [https://sylabs.io/docs/](https://sylabs.io/docs/)
