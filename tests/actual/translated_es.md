# Hola, el circleDiam es de 80 mm
## Este es un ejemplo de la generación de documentación.

### Enlaces entre páginas
[Mesa](#table)

### Título 1
Ahora tenemos un parámetro llamado ** boxHeight **, su ruta en el input.yml es
* testAssem> testWheelAndBox> testBox> user_params> boxHeight *.
Para mostrar el valor de esto, escribimos
```jinja2
{{testAssem.testWheelAndBox.testBox.user_params.boxHeight}}
```
Y el `código` en línea tiene` `back-ticks around` it.

### Lista
Bien, entonces hagamos una lista ahora:
1. testWheelAndBox
1. testBox
1. user_params
1. cajaAltura: 200 mm
2. boxLength: 100 mm

### Enlace
[enlace del sitio web de aguaclara](http://aguaclara.cornell.edu)

### Imagen
Aquí hay una imagen (pase el mouse para ver el texto del título):
![Universidad de Cornell](./image/cornell.png)
Solo necesita escribir el nombre de la imagen en el archivo yaml de entrada.
¡Pero, por favor, coloque directamente el archivo de imagen en la carpeta de imágenes!

### Mesa

Una mesa:

| Carta | Valor |
| --- | --- |
| A | val1 |
| B | val2 |
| C | val3 |
| D | val4 |
