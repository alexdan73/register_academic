import csv
import os

FIELDS = ["id", "nombres", "correo"]


def export_csv(simple_list, route):
    os.makedirs(os.path.dirname(route), exist_ok=True)
    with open(route, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for est in simple_list.recorrer():
            writer.writerow({k: est.get(k, "") for k in FIELDS})


def import_csv(simple_list, route):
    if not os.path.exists(route):
        raise FileNotFoundError(f"No se encontró el archivo: {route}")

    simple_list.clear()

    with open(route, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV vacío o sin encabezados.")
        missing = [c for c in FIELDS if c not in reader.fieldnames]
        if missing:
            raise ValueError(f"Faltan columnas en el CSV: {missing}")

        for i, fila in enumerate(reader, start=2):
            try:
                simple_list.insertar_final({
                    "id": int(fila["id"]),
                    "nombres": fila["nombres"],
                    "correo": fila["correo"],
                })
            except (ValueError, KeyError) as e:
                raise ValueError(f"Error en línea {i} del CSV: {e}")

    return simple_list