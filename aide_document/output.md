# Hello, the circleDiam is 80 mm
## This is an example of the documentation generation.


Now we have a params called **boxHeight**, its path in the input.yml is
*testAssem>testWheelAndBox>testBox>user_params>boxHeight*.
To show the value of it, we writes
```jinja2
{{ testAssem.testWheelAndBox.testBox.user_params.boxHeight }}
```
And inline `code` has `back-ticks around` it.


Ok, so let's make a list now:
1. testWheelAndBox
  1. testBox
    1. user_params
      1. boxHeight: 200 mm
      2. boxLength: 100 mm


[aguaclara website link](http://aguaclara.cornell.edu)


Here's an image(hover to see the title text):
![Cornell University](./image/cornell.png)
You only need to write the name of the image in the input yaml file.
But please directly put the image file in the image folder!

<<<<<<< HEAD
Colons can be used to align columns.
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
=======

A table:

| Letter | Value |
| --- | --- |
| A | val1 |
| B | val2 |
| C | val3 |
| D | val4 |
>>>>>>> 7fd2074df708a69210722fd8f1932d0bef69b510
