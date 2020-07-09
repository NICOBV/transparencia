# WEB SCRAPER
## Remuneraciones Municipalidades de Chile
### Autor: Nicolás Frías

Este es un algoritmo que va escarbando entre las páginas de *transparencia* de las comunas de una región hasta llegar a la/s tabla/s de remuneraciones de los trabajadores del municipio de dicha comuna. Luego permite exportarlas en un formato .CSV y/o cargarlas en una Base de Datos creada en SQLite. 

# Funcionamiento
 - A través de un archivo .xsl se obtienen las comunas que pertenecen a una región de Chile
 - Una vez que se tiene una lista de las comunas, el *Scraper* intenta obtener las URLs para personal a Contrata y de Planta
 - Usando una lista de *meses* y *años* proporcionada por el usuario, el *Scraper* navega por las sub páginas (tanto de Planta como de Contrata) hasta llegar a la tabla con los datos
 - En caso de que no se encuentre la tabla (el municipio no ha subido los datos para una fecha X en especifico o el sitio web reedirecciona a un archivo .PDF) se omite esta tabla (en la practica se crea un Pandas DF vacio)
 - Si el Scraper encuentra la tabla, simplemente se rescatan los datos y se anexan a un Diccionario de Datos de Python con el orden **[año][mes][comuna]**
 - Se repite este proceso por cada año y mes de cada comuna
 - Una vez que el Scraper termina de escarbar por todas las páginas del sitio web se realiza un proceso de carga de datos
 - Se crean los archivos .CSV de cada tabla rescatada (DataFrame) dentro del Diccionario de datos
 - Por ultimo se crea una Base de Datos en SQLite con el nombre de la región, se crean las tablas e insertan los datos tanto para: Comuna, Persona, Remuneracion
 - Existe un proceso intermedio en donde se determina el genero de cada persona utilizando un *modelo clasificador con machine learning*
 - Además se crea un archivo .LOG donde se agregan todos los mensajes entregados por el Scraper