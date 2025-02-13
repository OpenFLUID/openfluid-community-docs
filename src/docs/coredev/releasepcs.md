
## Preliminary checks

### OpenFLUID framework and applications, and related documentation

* [ ] All modifications are commited
* [ ] All tests passes in Debug build mode
* [ ] Version number is correct in CMake.in.cmake
* [ ] CHANGELOG file is up-to-date
* [ ] Version number is correct in user manual
* [ ] All translatable strings are translated in french
* [ ] All examples can be built

### Bindings

ROpenFLUID:

* [ ] Version number is correct
* [ ] The package is checked and builds correctly
* [ ] Man pages are up-to-date

PyOpenFLUID:

* [ ] Version number is correct
* [ ] The package is checked and builds correctly

OpenFLUIDjs:

* [ ] Version number is correct
* [ ] The package is checked and builds correctly

### Models

* [ ] Simulators of provided models (MHYDAS) are adapted, builds and works perfectly


## Building and packaging

### OpenFLUID framework and applications

* Build and create packages in Release mode (see [how to build OpenFLUID](../coredev/build.md)) for the following platforms:
    * [ ] Linux 64bits
    * [ ] Win 64bits
    * [ ] macOS 64bits
* [ ] Build and create source code package


### Models

_Only if external model packages are provided separately with the release_

* Build and create packages for the following platforms:
    * [ ] Linux 64bits
    * [ ] Win 64bits
* [ ] Build and create source code package


### Bindings

ROpenFLUID:

* [ ] Build and create packages
* [ ] Generate doc


### Containers

* [ ] Configure and build images for Docker and Singularity
* [ ] Tag docker images (latest, major.minor.patch, major.minor, major)


## Pre-deployment

### Uploads

* [ ] Upload OpenFLUID packages
* [ ] Upload models packages (if any)
* [ ] Update containers configurations on GitHub
* [ ] Upload Docker image on DockerHub
* [ ] Update README on DockerHub
* [ ] Update brew cask configuration on Github
* [ ] Upload "highlights on version" video on YouTube (if any)


### Web site

* [ ] Release notes are up to date and added to the release page
* [ ] Date is set in the release notes
* [ ] Fair use charter is up to date
* [ ] Blog article for release annoucement is written


### Community site

* [ ] Documentation page is up to date with latest available documents
* [ ] "Upgrading to a new version" page is up to date with correct instructions
* [ ] Fair use charter PDFs and links are up to date
* [ ] Highlights video is added to the materials page (if any, with rotation of older videos if needed)


## Deployment


* [ ] Deploy prepared community site
* [ ] Deploy prepared web site
* [ ] Add announcements on OpenFLUID mailing-list
* [ ] Add announcements on Twitter
* [ ] Add announcements on Slack workspaces


## Internal maintenance

* Create and check version tagging with correct `vM.m.p` pattern : 
    * [ ] openfluid
    * [ ] ropenfluid
    * [ ] homebrew-openfluid
* [ ] Update master branch to develop branch and push it on GitHub
* [ ] Push tags on GitHub (if not already done)
* Create releases on GitHub
    * [ ] openfluid
    * [ ] ropenfluid
* [ ] Push to secondary repositories, including tags
* [ ] Close the related milestone in the OpenFLUID Roadmap (if the release is a final release for the version milestone)