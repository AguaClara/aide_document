# Hello, the circleDiam is {{ testAssem.testCylinder.user_params.circleDiam }}
## This is an example of the documentation generation.
Now we have a params called **boxHeight**, its path in the input.yml is
*testAssem>testWheelAndBox>testBox>user_params>boxHeight*.
To show the value of it, we writes
```jinja2
{{ testAssem.testWheelAndBox.testBox.user_params.boxHeight }}
```
Ok, so let's make a list now:
1. testWheelAndBox
  1. testBox
    1. user_params
      1. boxHeight: {{ testAssem.testWheelAndBox.testBox.user_params.boxHeight }}
      2. boxLength: {{ testAssem.testWheelAndBox.testBox.user_params.boxLength }}
