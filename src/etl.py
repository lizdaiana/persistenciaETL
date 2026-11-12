
import pandas as pd
import sqlite3
from pathlib import Path


def ejecutar_etl():

    BASE_DIR = Path(__file__).resolve().parent.parent

    archivo_csv = BASE_DIR / "data" / "ventas_tienda.csv"
    archivo_db = BASE_DIR / "database" / "ventas.db"
    archivo_sql = BASE_DIR / "sql" / "schema.sql"

    try:
        # 1. EXTRACCION
        print("Iniciando extracción de datos...")

        df = pd.read_csv(archivo_csv)

        print(f"Registros extraídos: {len(df)}")

        # 2. TRANSFORMACION
        print("Transformando los datos...")

        df = df.drop_duplicates(subset=["id_venta"])

        df["fecha"] = pd.to_datetime(
            df["fecha"], errors="coerce"
        )

        df["cantidad"] = pd.to_numeric(
            df["cantidad"], errors="coerce"
        )

        df["precio_unitario"] = pd.to_numeric(
            df["precio_unitario"], errors="coerce"
        )

        df = df.dropna(
            subset=[
                "id_venta",
                "producto",
                "categoria",
                "cantidad",
                "precio_unitario",
                "fecha"
            ]
        )

        df["total_venta"] = (
            df["cantidad"] * df["precio_unitario"]
        ).round(2)

        df["fecha"] = df["fecha"].dt.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        df["id_venta"] = df["id_venta"].astype(int)
        df["cantidad"] = df["cantidad"].astype(int)

        print(f"Registros transformados: {len(df)}")

        # 3. CARGA Y PERSISTENCIA
        print("Conectando con SQLite...")

        archivo_db.parent.mkdir(
            parents=True, exist_ok=True
        )

        with sqlite3.connect(archivo_db) as conexion:

            with open(archivo_sql, "r", encoding="utf-8") as archivo:
                script_sql = archivo.read()

            conexion.executescript(script_sql)

            consulta = """
                INSERT OR IGNORE INTO ventas (
                    id_venta,
                    producto,
                    categoria,
                    cantidad,
                    precio_unitario,
                    fecha,
                    total_venta
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """

            registros = [
                (
                    int(fila.id_venta),
                    str(fila.producto),
                    str(fila.categoria),
                    int(fila.cantidad),
                    float(fila.precio_unitario),
                    str(fila.fecha),
                    float(fila.total_venta)
                )
                for fila in df.itertuples(index=False)
            ]

            conexion.executemany(consulta, registros)

            cargados = conexion.execute(
                "SELECT COUNT(*) FROM ventas"
            ).fetchone()[0]

        print("ETL ejecutado correctamente.")
        print(f"Registros procesados: {len(df)}")
        print(f"Total de ventas almacenadas: {cargados}")

    except FileNotFoundError as error:
        print(f"Archivo no encontrado: {error}")

    except sqlite3.Error as error:
        print(f"Error en SQLite: {error}")

    except Exception as error:
        print(f"Error durante el proceso ETL: {error}")
