import json
import os


def export_json(struct, route):
    os.makedirs(os.path.dirname(route), exist_ok=True)
    with open(route, "w", encoding="utf-8") as f:
        json.dump(struct.to_dict(), f, ensure_ascii=False, indent=2)


def import_json(struct, route):
    # valida existencia y formato JSON
    if not os.path.exists(route):
        raise FileNotFoundError(f"No se encontró el archivo: {route}")

    with open(route, encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON inválido en {route}: {e}")

    if not isinstance(data, dict):
        raise ValueError("El JSON debe ser un objeto (dict) en la raíz.")

    struct.from_dict(data)
    return struct