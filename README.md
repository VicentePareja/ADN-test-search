# Programa de Coincidencia de Genes en Tests de ADN

Este programa está diseñado para analizar un archivo de Excel que contiene distintos tests de ADN con genes asociados a cada uno. A partir de una entrada del usuario, que consiste en una lista de genes de interés, el programa busca coincidencias entre los genes ingresados y los genes evaluados en cada test. Finalmente, clasifica y muestra los 10 tests con más coincidencias.

## Estructura del Programa

El programa consta de las siguientes funciones principales:

1. **cargar_datos**: Carga el archivo de Excel especificado y devuelve un DataFrame de pandas con la información de los tests.
   
2. **contar_coincidencias**: Recorre cada fila del DataFrame, compara los genes testeados en cada test con los genes ingresados por el usuario, y cuenta el número de coincidencias para cada test.

3. **ranquear_tests**: Ordena los tests en función del número de coincidencias encontradas, en orden descendente.

4. **ejecutar**: Función principal que coordina las demás funciones. Solicita al usuario ingresar los genes de interés, carga los datos, calcula las coincidencias y muestra el top 10 de tests con más coincidencias.

## Instrucciones de Uso

1. **Instalación de Dependencias**: Ejecuta el siguiente comando para instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

2. **Preparación del Archivo de Excel**: Asegúrate de tener un archivo de Excel llamado DB ADN.xlsx con dos columnas: test y genes testeados. La columna test debe contener el nombre de cada test, y genes testeados debe contener una lista de genes separados por comas.

3. **Ejecución del Programa**: Ejecuta el archivo Python y sigue las instrucciones. El programa te pedirá ingresar una lista de genes separados por comas (ej: AAA4, BBB3).

4. **Resultados:**   El programa mostrará el top 10 de tests con más coincidencias en la consola, indicando el nombre del test y el número de coincidencias encontradas.

## Ejemplo de ejecución

Ingrese los genes separados por comas (ej: AAA4, BBB3): AAA4, BBB3

Ranking de tests por coincidencias:
test1: 3 coincidencia(s)
test2: 2 coincidencia(s)
test3: 1 coincidencia(s)

**Requisitos**
Asegúrate de tener pandas y openpyxl instalados para que el programa pueda leer el archivo de Excel. (revisar instrucciones de uso)

**Dependencias**
Python 3 y descargar las librerías correspondientes:

```bash
pip install -r requirements.txt
```
