
## Good development practice

### Use coding style guidelines

In order to produce clean code, read and apply coding style guidelines. Following these guidelines will increase the ability for others to understand and review your source code. The source code quality will be increased too.  
You can adopt the [OpenFLUID coding style](../scidev/codestyle.md).


### Raise warnings an errors

While checking possible errors or warnings, give information about these failed tests using the `OPENFLUID_RaiseWarning` and `OpenFLUID_RaiseError` methods.

```cpp
// ...

openfluid::core::SpatialUnit* SU;
openfluid::core::DoubleValue TmpValue, ResultValue;

OPENFLUID_UNITS_ORDERED_LOOP("SU",SU)
{  
  ID = SU->getID();
  OPENFLUID_GetVariable(SU,"input_var",CurrentStep,TmpValue);

  if (TmpValue > 0)
  {
    ResultValue = 1/TmpValue;
    OPENFLUID_AppendVariable(SU,"output_var",ResultValue);
  }
  else
    OPENFLUID_RaiseError("input_var is 0");

}

// ...
```

### Review code

Do not hesitate to view and review your source code to track errors, especially in tricky code parts. Use peer-reviewing if possible!

## Good documentation practices

For easier production of scientific documentation, the sim2doc tool can extract documentation directly from the source code. See also [how to buil documentation from simulators source code](../scidev/simdoc.md).

### Give scientific information

Scientific information is really important for an adapted use of the simulator you developed. You can include scientific information in your source code as C/C++ comments. It is an easy way to maintain an up-to-date documentation, according to your source code.

### Give usage information

Usage information will explain how to use the simulators, the input and output variables, the used attributes, the used parameters. A good usage information will increase the useness of the simulator and the modelling work efficiency.

## Good practices for simulator signature

The signature is the visible part of the simulator. It summarizes the simulator behaviour and should be filled with attention

### Use naming conventions

In order to avoid naming conflicts with different simulators, please refer to the naming conventions. It will also clarify the names of simulators and variables, that should be fully understandable by anyone having read the naming conventions.

### Do not forget data units

Data units can cause numeric errors, so fill the data units correctly in signatures to avoid conversions errors for a variable used by different simulators.

## Good data consistency practices

Data consistency checking can avoid numerical errors in computational codes. Developers are encouraged to check data before using it and before producing it.

### Check attributes

Attributes should be checked by simulators in order to verify if they match the correct range of values. This should be done in the checkConsistency method of the simulator.

```cpp
void ExampleFunc::checkConsistency()
{
  openfluid::core::DoubleValue Ks;
  openfluid::core::SpatialUnit* SU;

  OPENFLUID_UNITS_ORDERED_LOOP("SU",SU)
  {
    OPENFLUID_GetAttribute(SU,"ks",Ks);

    if (Ks < 0)
    {
      std::string IDStr;
      openfluid::tools::ConvertValue(ID,&IDStr);
      OPENFLUID_RaiseError("Negative ks on SU " + IDStr);
    }
  }
}
```

### Check variables before production

Produced variables should be checked before producing it, in order to avoid out of range or NaN values that can cause errors later or in other simulators.

## Good testing practices

Testing is the better way to check and validate simulators. There is no limit for testing!

### Use standard tests

Test your simulators with the most commonly used conditions, in order to check if the simulator response is correct. These conditions should be the common usage of the simulator.

### Use crash tests

Test your simulators with extreme conditions, for example by testing the lower and higher values of the possible values range. The simulator should work without crash in these conditions, or produce warnings and error if necessary.
