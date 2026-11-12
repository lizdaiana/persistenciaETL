
# Proyecto: Persistencia e Integración de Scripts ETL

## Descripción

Este proyecto tiene como objetivo desarrollar un proceso ETL (Extracción, Transformación y Carga) utilizando Python, Pandas y SQLite.

Se trabaja con un archivo CSV llamado `ventas_tienda.csv`, que contiene información de ventas de una tienda, la informacion del cvs se obtuvo en la página de https://www.kaggle.com/.

El proceso busca extraer los datos, realizar una limpieza y transformación, calcular el importe total de cada venta y almacenar los resultados en una base de datos SQLite.

## Objetivos

- Extraer datos desde un archivo CSV.
- Limpiar registros duplicados y valores nulos.
- Transformar los datos utilizando Pandas.
- Calcular el total de cada venta.
- Almacenar los datos en una base de datos SQLite.
- Evitar la inserción de registros duplicados.

## Estructura del proyecto

```text
persistenciaETL/
│
├── data/
│   └── ventas_tienda.csv
│
├── database/
│   └── ventas.db
│
├── sql/
│   └── schema.sql
│
├── src/
│   └── etl.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Tecnologías utilizadas

- Python
- Pandas
- SQLite
- SQL

## Requisitos

- Python instalado.
- Visual Studio Code (opcional).
- Librería Pandas.

SQLite está incluido en la biblioteca estándar de Python, por lo que no necesita instalación adicional.

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/lizdaiana/persistenciaETL.git
```

2. Ingresar a la carpeta del proyecto:

```bash
cd persistenciaETL
```

3. Crear un entorno virtual:

```bash
python -m venv .venv
```

4. Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

5. Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Pasos para ejecutar

Ejecutar el siguiente comando desde la carpeta principal del proyecto:

```bash
python main.py
```

El programa realizará automáticamente las siguientes tareas:

1. Extracción de los datos del archivo CSV.
2. Limpieza y eliminación de duplicados.
3. Conversión y validación de los datos.
4. Cálculo del total de cada venta.
5. Creación de la tabla en SQLite.
6. Carga de los registros evitando duplicaciones.

## Base de datos

La base de datos utilizada es SQLite.

La tabla `ventas` se define mediante el archivo `sql/schema.sql`.

La tabla contiene los siguientes campos:

- id_venta
- producto
- categoria
- cantidad
- precio_unitario
- fecha
- total_venta

## Control de duplicados

Se utiliza `id_venta` como clave primaria y la instrucción SQL `INSERT OR IGNORE`.

De esta manera, si un registro ya existe en la base de datos, no se vuelve a insertar.

## Resultado obtenido

El proceso ETL se ejecutó correctamente y permitió almacenar 1.200 registros.

Al ejecutar nuevamente el proceso, la cantidad de registros almacenados permaneció en 1.200, comprobando que no se generan duplicados.


