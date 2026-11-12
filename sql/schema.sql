CREATE TABLE IF NOT EXISTS ventas (
    id_venta INTEGER PRIMARY KEY,
    producto TEXT NOT NULL,
    categoria TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    fecha TEXT NOT NULL,
    total_venta REAL NOT NULL
);
