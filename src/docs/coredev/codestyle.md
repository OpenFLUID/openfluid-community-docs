{!common/codestyle.md!}

## Automatic tools for checking OpenFLUID source code

### Static code analysis (cppcheck)

This tool analyses the official OpenFLUID source code using the [cppcheck](http://cppcheck.sourceforge.net/) static analysis tool for C/C++. It helps to point out potential problems such as memory leaks, uninitialized variables, unused variables, ...  
It does not automatically modify the source code.  

To run this tool, once the CMake configuration is done, execute the following command from the build tree:
```
make cppcheck
```

Options passed to the cppcheck tool can be set through the `CPPCHECK_EXTRA_OPTIONS` CMake variable (in the `CMake.in.cmake` file or your `CMake.in.local.cmake` file)

This tool requires an installed Python interpreter and the cppcheck tool.

### Coding style

This tool checks the official OpenFLUID source code for pointing out out potential coding style problems.  
It does not automatically modify the source code.  

To run this tool, once the CMake configuration is done, execute the following command from the build tree:
```
make stylecheck
```

This tool requires an installed Python interpreter.
