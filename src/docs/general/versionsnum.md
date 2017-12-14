
## Version numbers policy

This software version number policy is used for all OpenFLUID softwares, plugins and components. This policy is applied since the 1.3.1 version (included).  

The full version number is made of the following parts:

* the **MAJOR** number of the version
* the **MINOR** number of the version
* the **PATCH** number of the version
* an optional status (STATUS) that can be :
    * _rc_ (release candidate) : stable version, released for users testing, some non-functional features may be incomplete (docs, translations, ...)
    * _beta_ : almost stable version, with main features, few bugs left
    * _alpha_ : development version, with some of the main features, maybe many bugs


## Version compatibility

This software compatibility policy based on version numbers is used for both framework and software applications. This policy is applied since the 1.5 version (included).  


### API compatibility

The OpenFLUID [API](http://en.wikipedia.org/wiki/Application_programming_interface) using the same MAJOR.MINOR version are compatible, whatever is the PATCH version.  
This means that a source code (_e.g. simulators source code_) developed with a MAJOR.MINOR.x  version (_e.g. 1.5.2_) can be linked and compiled against any of the MAJOR.MINOR versions (_e.g. 1.5.0, 1.5.1, 1.5.3_) without any modification. Nevertheless, a compilation/link of the source code built using the API is strongly recommended, as the MAJOR.MINOR versions are not [ABI](http://en.wikipedia.org/wiki/Application_binary_interface) always compatibles (see below).


### ABI compatibility

The [ABI](http://en.wikipedia.org/wiki/Application_binary_interface) using the same MAJOR.MINOR.PATCH version are compatible. This means that a compiled code (_e.g. binary simulators files .so or .dll_) developed with a MAJOR.MINOR.PATCH version (_e.g. 1.5.2_) can be only used with an application using the same MAJOR.MINOR.PATCH versions (_e.g. 1.5.2_), without rebuilding.
