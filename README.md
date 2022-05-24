# Examen Final Computación Paralela y Distribuida
Repositorio de la clase Computación Paralela y Distribuida Examen Final

En la carpeta Img se podran vizualizar los resultados graficos con Python 

En la carpeta ImgC se podran vizualizar los resultados graficos con Cython

## Para su ejecución
Realizar la compilacion del setup con:
```
python3 setup.py build_ext --inplace
```
si trabaja en MAC y el setup presenta fallos cambie el contenido del setup.py por:
```python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

setup(
      ext_modules=cythonize([Extension("heat_cyt", ["heat_cyt.pyx"], include_dirs=[numpy.get_include()])])
)
```
Luego de la compilacion exitosa cambie la ruta de la variable $path a la ubicacion de su proyecto
```perl
$path = "Your path";#Ingresar su ruta - puede obetenerla ingresando el comando 'pwd' en la terminal
```
Ejecute el lanzador
```
./lanzador.pl
```
Si trabaja en MAC
```
perl lanzador.pl
```





