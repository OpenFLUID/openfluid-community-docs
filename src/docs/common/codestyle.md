The coding style conventions are often designed for a specific language. The following recommendations are designed to be applied to C++, but can be applied to other language (Java, C, ...)  
<br/>

!!! danger "Recommendation"
    **The major recommendation is to know and apply the following recommendations.**


## Naming conventions

### Files

The files should have understandable names. When a file is a declaration or a definition of a class, the file name should be the class name. For example, the file declaring the PluggableSimulator class should be named PluggableSimulator.hpp  
The main file of a program should be named main.xxx (when possible)

### Include guard  

The include guard for a .hpp file begins and ends with a double underscore `__`. It is mainly made of the file name in upper-case, and the dot `.` characters are replaced by an underscore. It is decorated with other informations according to the context of the developed source code.

#### OpenFLUID API header

In this context, the include guard for a header of the OpenFLUID API is prefixed with the 'OPENFLUID' word and the current namespace. Words are separated by a single underscore `_`.


Example for the DoubleValue.hpp file, located in the core namespace of the API:
```cpp
#ifndef  __OPENFLUID_CORE_DOUBLEVALUE_HPP__
#define  __OPENFLUID_CORE_DOUBLEVALUE_HPP__

// place the source code here

#endif  /* __OPENFLUID_CORE_DOUBLEVALUE_HPP__ */
```

#### OpenFLUID application header

In this context, the include guard for a header in an OpenFLUID application is prefixed with the OPENFLUID word and a short application identifier.  Words are separated by a single underscore `_`  
Short identifiers for current applications are:

* `BUILDERAPP` for OpenFLUID-Builder application
* `CMDLINEAPP` for OpenFLUID command line application
* `DEVSTUDIOAPP` for OpenFLUID-DevStudio application


Example for the SignatureWidget.hpp file of OpenFLUID-Builder:
```cpp
#ifndef  __OPENFLUID_BUILDERAPP_SIGNATUREWIDGET_HPP__
#define  __OPENFLUID_BUILDERAPP_SIGNATUREWIDGET_HPP__

// place the source code here

#endif  /* __OPENFLUID_BUILDERAPP_SIGNATUREWIDGET_HPP__ */
```


#### Other files



Other files (source codes of simulators, observers, extensions, external applications) should apply the default naming for include guards.

Example for a MyFilename.hpp file:
```cpp
#ifndef  __MYFILENAME_HPP__
#define  __MYFILENAME_HPP__

// place the source code here

#endif  /* __MYFILENAME_HPP__ */
```



### Identifiers

#### General rules

| Identifier | Rule | Example |
| ------------ | ------------- | ------------ |
| Local variable | use pascalCase  | MyVariable
| Variable in a macro | begins with a `_` (underscore), followed by an upper case 'M', followed by a `_` (underscore), followed by the name of the variable  | _M_Variable
| Constant value | use UPPERCASE, every sub-part of the name are separated by a `_` (underscore) |  MY_CONSTANT
| Type name | use PascalCase, followed by a '_' (underscore), followed by a 't' | Type_t
| Function name | use camelCase, preferably begins with a verb in lower case | doThisJob(...)
| Parameter | use PascalCase | TheParameter
| Class name | use PascalCase | ClassName
| Class attribute (private) | begins with a lowercase 'm', followed by a '_' (underscore), followed by the name in PascalCase | m_Member
| Class pointer attribute (private) | begins with a lowercase 'mp', followed by a '_' (underscore), followed by the name in PascalCase | mp_PtrMember
| Class static attribute (private) | begins with a lowercase 'ms', followed by a '_' (underscore), followed by the name in PascalCase | ms_StaticMember
| Class method (public or private) | use camelCase, preferably begins with a verb in lower case | doThisJob(...)
| Accessors to class members (getters and setters) | use camelCase, with [naming rules for accessors to class members](#specific-naming-rules-for-accessors-to-class-members) (see below) | setMember(...), getMember(), member()

The formats:

* UPPERCASE: use only uppercase letters
* lowercase: use only lowercase letters
* PascalCase: every sub-part begins with an uppercase letter, everything else in lowercase
* camelCase: every sub-part begins with an uppercase letter except the first subpart, everything else in lowercase


#### Pointer and reference expressions

When declaring a pointer variable or argument, you must place the asterisk adjacent to the type of the variable.  
When declaring a reference variable or argument, you must place the ampersand adjacent to the type of the variable.  
When using a pointer or reference, you must not place any space around period or arrow operators, and pointer operators do not have trailing spaces.
```cpp
class ObjectType
{
  public:
    void doThis(const std::string& Str)
    { /*...*/ }
};

int main(int argc, char* argv[])
{
  std::string S = "Hello";

  ObjectType* Op = new ObjectType();
  Op->doThis(S);

  ObjectType O = *Op;  
  O.doThis(S);

  delete Op;
}
```

#### Specific naming rules for accessors to class members

##### Setters

Setters must begin with the 'set' prefix.
```cpp
private:
  ObjectType m_member;

public:
  void setMember(const ObjectType& Obj);
```


##### Getters

When the getter returns a copy of a class member, it must begin with the 'get' prefix.  
When the getter gives a direct access to a class member (or a part of the class member) using a pointer or a reference (const or not) to this class member, it must not begin with the 'get' prefix. It is usually define with a name close to the referenced or pointed member name.

```cpp
private:
  ObjectType m_member;

public:
  ObjectType getMember();
  ObjectType& member();
```


#### Full example


```cpp
class Vehicle
{
  private:

    std::string m_Brand;

    std::string m_Model;

    std::string m_Color;

    EngineProperties m_EngineProps;

    Owner* mp_Owner;


  public:

    Vehicle(const std::string& Brand,
            const std::string& Model,
            const std::string& Color);

    ~Vehicle()
    { }

    std::string getBrand() const
    { return m_Brand; }

    std::string getModel() const
    { return m_Model; }

    std::string getColor();

    void setColor(const std::string& Color)
    { m_Color = Color; }

    const EngineProperties& engineProperties() const
    { return m_EngineProps; }

    Owner* owner()
    { return mp_Owner; }
};


Vehicle::Vehicle(const std::string& Brand,
                 const std::string& Model,
                 const std::string& Color):
  m_Brand(Brand), m_Model(Model), m_Color(Color)
{

}


std::string Vehicle::getColor()
{
  return m_Color;
}
```


### CMake variables, functions and macros

The CMake variables, functions and macros related to OpenFLUID must be prefixed by either the `OFBUILD_` or `OPENFLUID_` string, applying the following rules as strictly as possible:
* Use `OFBUILD_` for items which are internal to the OpenFLUID build system
* Use `OPENFLUID_` for items which may be publicly available through the SDK (i.e. items that may be used in config.hpp file or CMake modules for wares development)

You may also prefix temporary or local variables, macros and functions by a `_` character.


## Conventions for writing code

### Language

* The language used in the source code (identifiers, comments, ...) is the english language. This will ensure that the source code is easy to read and maintain by people from different countries.


### Indentation and statement blocks

* The indentation is done using two spaces '  '. The use of tabs should be avoided.
* The blocks of statements must be indented (functions, methods, loops, conditions, ...)
* In curly bracket programming languages (such as C++), the opening and closing brackets should be alone on a line. The indentation will begin just after the opening bracket and stop just before the closing bracket.
* In case of empty blocks
    * in header files (e.g. `*.hpp`), the block can be written on a single line using the `{ }` form just below the function or method declaration
    * in implementation files (e.g. `*cpp`), the block must be written on multiple lines
* Wherever possible, avoid using single line instruction without brackets under loops and conditions


```cpp
int a;
int i;

a = 18;

for (i=0; i<a; i++)
{
  if (i < 10)
  {
    std::cout << i << " is lesser than 10" << std::endl;
  }
  else if (i>10)
  {
    std::cout << i << " is greater than 10" << std::endl;
  }
  else
  {
    std::cout << i << " is equal to 10" << std::endl;
  }
}
```


### Included header files

In the `#include` part at the top of sources files, group files by category from more generic to more specific, e.g system and C++ STL includes first, then frameworks includes and finally the OpenFLUID includes.
```cpp
#include <iostream>
#include <vector>

#include <gdal.h>

#include <QString>
#include <QDir>

#include <openfluid/dllexport.hpp>
#include <openfluid/config.hpp>
#include <openfluid/core/DoubleValue.hpp>
#include <openfluid/tools/DataHelpers.hpp>
```

### Namespaces opening and closing

* Namespace content should begin on the next line after namespace opening bracket. The closing brancket should be on the next line after the namespace content.
* Nested namespaces should be opened on the same line
* Nested namespaces should be closed on the same line, with namespace name as comment

```cpp
namespace foo {

// here is the namespace content

}  // namespace foo


namespace foo { namespace bar {

// here is the namespace content

} }  //  namespaces
```


### Line length and wrapping

* For better reading and printing, each line of text in your code should be at most 120 characters long.

* The wrapping of parameters should be done by an alignment of parameters under the beginning of parameters

* The wrapping in assignments should be done with an indentation of two spaces


```cpp
VarA = MyFunction(Param1, Param2,  
                  Param3, Param4,
                  Param5);

VarB = VarB * 2;

TheVarWithLongName =
  MyObject.runThisMethodWithAVeryLongName(Param1,
                                          Param2);
```


### White spaces and white lines

* In order to write a more readable code, you are encouraged to use horizontal and vertical whitespaces, and "group" lines of code by "action".

```cpp
int a = 18;   // declarations
int i;

for (i=0; i<a; i++)  // processing
{
  printf(i*i);
}
```


* You are really encouraged to write two comment lines of dashes between methods or functions definitions, with two blank lines before and after these lines.

```cpp
Vehicle::Vehicle(const std::string& Brand,
                 const std::string& Model,
                 const std::string& Color):
  m_Brand(Brand), m_Model(Model), m_Color(Color)  
{

}


// ===========================================================
// ===========================================================


std::string Vehicle::getColor()
{
  return m_Color;
}
```


* Empty methods or functions should contains at least one blank line.


### Comments for API documentation

The API documentation should be written following the [Doxygen](https://www.doxygen.nl/) formalism and commands

* The comment block should begin by `/*` and end by `*/`
* The lines in the comment block should not be left prefixed by a `*`
* Use the `@` sign (at-sign) to start the Doxygen commands instead of the `\` sign (backslash)
* The inside text of the comment block should be indented by two spaces


```cpp
/*
  Returns an information as a string
  @param[Key the requested information key
  @param[out](in]) Info the value corresponding to the requested key
  @return true if the key exists and the conversion to string type runs successfully
*/
bool getInfoAsString(const std::string& Key, std::string& Info) const
```


### C++ Standard

Since version 2.2.0, OpenFLUID requires a C++17 compliant compiler to be built.  
So, it is highly recommended to apply the C++17, C++14 and C++11 features, such as:

* <code>nullptr</code> instead of <code>NULL</code>
* range-based for loops combined with the <code>auto</code> specifier (instead of iterators based loops for example)
* <code>enum class</code> instead of classic <code>enum</code>
* smart pointers wherever it is possible (taking into account the small overhead introduced by smart pointers)
* delegating constructors where possible
* <code>nodiscard</code> function attribute when function return is expected to be used
* <code>optional</code> for variable sometimes not set and <code>variant</code> for type-safe union
* ...


Older versions of OpenFLUID requires C++ compliant compilers

* C++14 for versions from 2.1.7 to 2.1.11 (included)
* C++11 for versions from 2.1.0 to 2.1.6 (included)
* C++98 for previous versions


## Source code tags

During the development process, tags can be used in code comments to mark specific code status or actions to perform.
They are written in capital, followed by an optional description.  

* `DIRTYCODE` : code marked as temporarily inserted (e.g. display of internal values, debugging hints, ...), must be deleted once useless and must not be commited
* `TOIMPL` : part to be implemented, must be done before the next release
* `FIXME` : marked bug, must be fixed before the next release
* `HACK` : temporary workaround, should be replaced before the next release
* `TODO` : action to perform, not critical with no due date
* `NOTE` : a simple note

Examples

```cpp
std::cout << __PRETTY_FUNCTION__  << ", " << __LINE__ << std::endl; // DIRTYCODE
```

```cpp
int doThis()
{
  std::cerr << "not implemented" << std::endl; // TOIMPL implement the code to do this, see ticket xxx
  return 0;
}
```


## Design conventions

### Object class

* a definition/implementation of an object class should be written in a single .hpp/.cpp file
* a .hpp/.cpp file should contain only a single class definition/implementation.


### Qt UI Components

* Qt UI components should be designed using QtCreator designing tool.
* Qt UI components should be integrated in the source code using the [single inheritence method with a pointer membre variable](http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html#using-a-pointer-member-variable).
* For a more explicit source code of Qt UI components, avoid using the auto-connect system for signals and slots


Example below for the use of a MyWidget.ui file created using QtCreator.

MyWidget.hpp
```cpp-qt
#include <QWidget>


namespace Ui
{
  class MyWidget;
}


class MyWidget : public QWidget
{
  Q_OBJECT

  private:

    Ui::MyWidget* ui;


  public:

    MyWidget(QWidget* Parent = 0);

    virtual ~MyWidget();
};
```


MyWidget.cpp
```cpp-qt
#include "ui_MyWidget.h"
#include "MyWidget.hpp"

MyWidget::MyWidget(QWidget* Parent):
  MyWidget(Parent,AFXDesc), ui(new Ui::MyWidget)
{
  ui->setupUi(this);
}


// ===========================================================
// ===========================================================


MyWidget::~MyWidget()
{
  delete ui;
}
```


## Other important recommendations

* Use const keyword wherever it is possible
* Prefer pass methods or functions parameters by const reference instead of value
* Use static methods when possible
* Use initialization lists in constructors wherever it is possible
* Avoid the 'using' keyword for accessing elements in namespaces
* Prefer reuse existing macros, methods, classes from the OpenFLUID API or from an external library instead of rewriting your own. For example, the OpenFLUID API provides low-level functionnalities for:
    * Filesystem operations
    * Singletons implementation
    * String manipulations : to and from numeric conversion, splitting, ...
    * Floating point comparison
    * Fortran integration in C++