
## Preliminary checks

### OpenFLUID framework and applications, and related documentation

* All modifications are commited
* All tests passes in Debug build mode
* Version number is correct in CMake.in.cmake
* CHANGELOG file is up-to-date
* Version number is correct in user manual
* All documentation can be built (user manual, API guide, ...)
* All translatable strings are translated in french
* All examples can be built

### Bindings

ROpenFLUID:

* Version number is correct
* The package is checked and builds correctly
* Man pages are up-to-date

### Models

* Simulators of provided models (MHYDAS) are adapted, builds and works perfectly

### Community site

* Documentation page is up to date with latest available documents
* "Upgrading to a new version" page is up to date with correct instructions
* "Release notes" page is up to date


## Building and packaging

### OpenFLUID framework and applications

* Build and create packages in Release mode (see [how to build OpenFLUID](../coredev/build.md)) for the following platforms:
    * Linux 64bits
    * Win 32bits
    * macOS 64bits
* Build and create source code package


### Models
* Build and create packages for the following platforms:
    * Linux 64bits
    * Win 32bits
* Build and create source code package


### Bindings

ROpenFLUID:

* Build and create packages


### Containers

* Configure and build images for Docker and Singularity


## Deployment

### Uploads

* Upload OpenFLUID packages
* Upload Models packages (if any)
* Upload containers configurations and images


### Announcements

* Update Downloads page on OpenFLUID website with new available packages
* Add announcements on
    * OpenFLUID web site
    * OpenFLUID mailing-list
    * Twitter

### Internal maintenance

* If the release is a final release for the version milestone, close the related milestone in the OpenFLUID Roadmap
* Update master branch to develop branch
