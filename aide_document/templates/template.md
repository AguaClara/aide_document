# Hello, the circleDiam is {{ testAssem.testCylinder.user_params.circleDiam }}
## This is an example of the documentation generation.

### Inter-page links
[Table](#table)

### Title 1
Now we have a params called **boxHeight**, its path in the input.yml is
*testAssem>testWheelAndBox>testBox>user_params>boxHeight*.
To show the value of it, we writes
```jinja2
{{ "{{ testAssem.testWheelAndBox.testBox.user_params.boxHeight }}" }}
```
And inline `code` has `back-ticks around` it.

### List
Ok, so let's make a list now:
1. testWheelAndBox
  1. testBox
    1. user_params
      1. boxHeight: {{ testAssem.testWheelAndBox.testBox.user_params.boxHeight }}
      2. boxLength: {{ testAssem.testWheelAndBox.testBox.user_params.boxLength }}

### Link
[aguaclara website link]({{officialSite}})

### Image
Here's an image(hover to see the title text):
![Cornell University](./{{imageUrl}})
You only need to write the name of the image in the input yaml file.
But please directly put the image file in the image folder!

### Table
{% set dict = table.tableContent %}
A table:

| {{table.tableColumn1}} | {{table.tableColumn2}} |
| --- | --- |
{% for dict_item in dict %}{% for key, value in dict_item.items() %}| {{key}} | {{value}} |
{% endfor %}{% endfor %}
