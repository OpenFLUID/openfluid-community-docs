
# OpenFLUID Community documentation


## Documentation sources

The documentation sources are located in the `src` directory. It is made of a set of simple pages, written in markdown and powered by [MkDocs](www.mkdocs.org).  
The [main page](src/docs/index.md) of this documentation is the `src/docs/index.md` file.


## Builder environment

The builder environment is a docker container that includes tools to generate the site.
To setup this environment and run command into this, just run the build script:
```
./build-env
```


## Build operations

Once the shell from the container is running, you can use scripts located in /workdir/scripts:
* `build` for building the community site

The build results are available in the `_build` directory
