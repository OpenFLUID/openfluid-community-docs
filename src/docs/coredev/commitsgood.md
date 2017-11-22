
## Before committing

* The code must be **entirely compiled and built without error**
* The code should pass **all tests successfully**
* Strings to translate must be **marked for translation** (i.e. ```tr("string to translate")```)
* All **"development things" must be removed**, such as ```std::cout``` or ```std::cerr``` for debugging, temporary comments, temporary TODOs, etc...


## Commit contents

* A commit should be **as atomic as possible**: 1 task/1 bug fix = 1 commit
* A commit must **always contain a message** explaining the reason and/or the content of the commit


## Commit messages

A commit message should be made of 3 parts:

* A **summary title**
* A list of **things done** in this commit, each item must start with the `*` character
* If exists, a **reference to the issue** to which the commit is linked to, writent inside brackets. It is made of the id of the issue, prefixed by the OpenFLUID/openfluid  repository reference and a `#` character. It is introduced by the _references_ word if the commit is a contribution to solve the issue, or by the _closes_ word if the commit closes the issue.  
The issue tracking system is available on GitHub in the [OpenFLUID/openfluid repository](https://github.com/OpenFLUID/openfluid/issues). This tracking system holds issues tickets for all OpenFLUID repositories (main OpenFLUID framework and applications, ROpenFLUID, PyOpenFLUID, ...).  

The 3 parts are separated by a blank line.  
<br/>

Examples of commit messages:
```
Creation of the About dialog

* Added About dialog window
* Cleaned code

(references OpenFLUID/openfluid#21)
```

```
Fix of duplicates IDs for datastore items

* Added checking of IDs when instanciating datastore

(closes OpenFLUID/openfluid#23)
```
