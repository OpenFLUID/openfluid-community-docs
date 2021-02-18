

# Contributing

As the OpenFLUID community documentation is adressed to the users, we ❤️ the contributions from any user!


## Preliminary operations

* Browse the [community documentation](http://community.openfluid-project.org) to get familiar with the documentation structure
* If not already done, have a look at [MkDocs](http://www.mkdocs.org) documentation tool and [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) syntax. The OpenFLUID community documentation is based on this tool and language
* If not already done, install required tools :
  1. Python 3 ([see instruction here](https://www.python.org/downloads/))
  1. MkDocs and extensions 
     ```sh
     pip3 install mkdocs mkdocs-markdownextradata-plugin pymdown-extensions markdown-include mkdocs-material bibtexparser
     ```

## Contribution process

1. Let us know you want to make a contribution, it is always better to know each others for later interactions. For that, you can use our [support tools](http://community.openfluid-project.org/start/support/)
1. Fork the documentation repository
1. Clone your fork locally and create a dedicated branch for your contributions
1. Update the documentation with your contributions by committing it locally. Check that your contributed documentation builds without problem usink mkdocs (see [next part](#writing-using-mkdocs))
1. Push it to your forked repository in the dedicated branch
1. Make a pull request for your contributions


## Writing using MkDocs

The documentation sources are located in the `src` directory. The [main page](src/docs/index.md) of this documentation is the `src/docs/index.md` file.

During the writing phase of your contributions, you can render the documentation using the MkDocs tool. The following recipe is for Linux environments.

1. Open a terminal
1. Go to the `src` directory
1. Run the `mkdocs serve` command from within this directory
1. Open your browser to the URL given by the `mkdocs serve` command

The documentation is automatically reloaded in the browser every time you save the markdown files on disk.