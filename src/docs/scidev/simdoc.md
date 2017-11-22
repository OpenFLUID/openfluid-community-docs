!!! danger "TODO"
    To be reviewed  
    To add : from command line, run make command using specific doc target 

The writing of a simulator documentation is an important part of the development process.  
In order to help simulators designers and developers, the **sim2doc** tool can interpret the source code of the main .cpp file to generate documentation. This documentation is built using the simulator signature and free text located as comments in the text.  
<br/>
The **sim2doc** tool generates a LaTeX file that can be transformed on-the-fly as a PDF file or HTML content. The free text part can contain LaTeX commands, especially for maths formulas. Using the default template, the generated document will be structured as follows:

1. title with author(s)
1. brief description
1. handled data (variables, properties, simulator parameters, events, extrafiles, ...)
1. the free text


The free text part must be placed into comments, between the `<sim2doc>` and `</sim2doc>` tags.
```cpp
/*
<sim2doc>
This is the free text part of my simulator. I can write \latex commands and formulas like $f(x)=1/x$
</sim2doc>
*/
```
<br/>
To know how to use the sim2doc tool, just type the following command in your terminal :
```sh
openfluid buddy --buddy-help sim2doc
```
<br/>
The standard usage to build documentation from a .cpp file and build the PDF on-the-fly is :
```sh
openfluid buddy sim2doc --options=inputcpp=MySimulator.cpp,outputdir=/path/to/output/directory,pdf=1
```
