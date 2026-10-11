import os
import sys

# Permitir ejecución desde cualquier carpeta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from simple_list import SimpleList
from double_list import DoubleList
from circular_list import CircularList
from persistence_csv import export_csv, import_csv
from persistence_json import export_json, import_json

# ---------- Rutas ----------
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")
os.makedirs(DATA, exist_ok=True)

ROUTE_CSV = os.path.join(DATA, "inscritos.csv")
ROUTE_HIST = os.path.join(DATA, "historial.json")
ROUTE_GRUP = os.path.join(DATA, "grupos.json")

# ---------- Estructuras globales ----------
inscritos = SimpleList()
historial = DoubleList()
grupos = CircularList()


def ask(msg):
    return input(msg).strip()


def pause():
    input("\n[Enter para continuar]")


# ============================================================
# MÓDULO 1: Inscritos (Lista Simple)
# ============================================================
def menu_inscritos():
    while True:
        print("""
        --- INSCRITOS (Lista Simple) ---
        1. Agregar estudiante
        2. Eliminar por ID
        3. Buscar por ID
        4. Mostrar inscritos
        5. Exportar CSV
        6. Importar CSV
        0. Volver
        """)

        op = ask("Opción: ")

        if op == "1":
            try:
                inscritos.insertar_final({
                    "id": int(ask("ID: ")),
                    "nombres": ask("Nombres: "),
                    "correo": ask("Correo: "),
                })
                print("Estudiante registrado.")
            except ValueError:
                print("ID inválido.")

        elif op == "2":
            try:
                ok = inscritos.eliminar(int(ask("ID a eliminar: ")))
                print("Eliminado." if ok else "No existe.")
            except ValueError:
                print("ID inválido.")

        elif op == "3":
            try:
                r = inscritos.buscar(int(ask("ID a buscar: ")))
                print(r if r else "No encontrado.")
            except ValueError:
                print("ID inválido.")

        elif op == "4":
            lista = inscritos.recorrer()
            if not lista:
                print("(sin inscritos)")
            for e in lista:
                print(f"{e['id']:>4} | {e['nombres']:<25} | {e['correo']}")

        elif op == "5":
            try:
                inscritos.exportar_csv(ROUTE_CSV)
                print(f"Exportado a {ROUTE_CSV}")
            except Exception as e:
                print(f"Error al exportar: {e}")

        elif op == "6":
            try:
                inscritos.importar_csv(ROUTE_CSV)
                print(f"Importado desde {ROUTE_CSV}")
            except FileNotFoundError:
                print("No existe el CSV.")
            except ValueError as e:
                print(f"CSV inválido: {e}")

        elif op == "0":
            break

        pause()


# ============================================================
# MÓDULO 2: Historial (Lista Doble)
# ============================================================
def menu_historial():
    while True:
        print("""
        --- HISTORIAL ACADÉMICO (Lista Doble) ---
        1. Agregar semestre (ordenado)
        2. Buscar semestre
        3. Recorrer adelante
        4. Recorrer atrás
        5. Eliminar semestre
        6. Exportar JSON
        7. Importar JSON
        0. Volver
        """)

        op = ask("Opción: ")

        if op == "1":
            try:
                anio = int(ask("Año: "))
                term = int(ask("Término (1/2): "))

                if historial.buscar(f"{anio}-{term}"):
                    print("Ese semestre ya existe.")
                    pause()
                    continue

                materias = []
                while True:
                    cod = ask("Código materia (enter para terminar): ")
                    if not cod:
                        break
                    materias.append({
                        "cod": cod,
                        "nombre": ask("  Nombre: "),
                        "nota": float(ask("  Nota: ")),
                    })
                historial.insertar_ordenado({
                    "anio": anio,
                    "term": term,
                    "materias": materias,
                })
                print("Semestre agregado.")
            except ValueError as e:
                print(f"Datos inválidos: {e}")

        elif op == "2":
            r = historial.buscar(ask("Semestre (ej. 2024-1): "))
            print(r if r else "No encontrado.")

        elif op == "3":
            lista = historial.recorrer_adelante()
            if not lista:
                print("(sin semestres)")
            for s in lista:
                print(f"{s['anio']}-{s['term']}: " +
                      ", ".join(f"{m['cod']}({m['nota']})" for m in s["materias"]))

        elif op == "4":
            lista = historial.recorrer_atras()
            if not lista:
                print("(sin semestres)")
            for s in lista:
                print(f"{s['anio']}-{s['term']}: " +
                      ", ".join(f"{m['cod']}({m['nota']})" for m in s["materias"]))

        elif op == "5":
            ok = historial.eliminar(ask("Semestre a eliminar (ej. 2024-1): "))
            print("Eliminado." if ok else "No existe.")

        elif op == "6":
            try:
                historial.exportar_json(ROUTE_HIST)
                print(f"Exportado a {ROUTE_HIST}")
            except Exception as e:
                print(f"Error al exportar: {e}")

        elif op == "7":
            try:
                historial.importar_json(ROUTE_HIST)
                print(f"Importado desde {ROUTE_HIST}")
            except FileNotFoundError:
                print("No existe el JSON.")
            except ValueError as e:
                print(f"JSON inválido: {e}")

        elif op == "0":
            break

        pause()


# ============================================================
# MÓDULO 3: Grupos (Lista Circular)
# ============================================================
def menu_grupos():
    while True:
        print("""
        --- GRUPOS (Lista Circular) ---
        1. Agregar grupo
        2. Eliminar grupo
        3. Buscar (recursivo)
        4. Rotar k posiciones
        5. Recorrer ciclo (2 vueltas)
        6. Exportar JSON
        7. Importar JSON
        0. Volver
        """)

        op = ask("Opción: ")

        if op == "1":
            grupos.insertar({
                "nombre_grupo": ask("Nombre grupo: "),
                "tutor": ask("Tutor: "),
                "tema": ask("Tema: "),
            })
            print("Grupo agregado.")

        elif op == "2":
            ok = grupos.eliminar(ask("Grupo a eliminar: "))
            print("Eliminado." if ok else "No existe.")

        elif op == "3":
            r = grupos.buscar_recursivo(ask("Grupo a buscar: "))
            print(r if r else "No encontrado.")

        elif op == "4":
            try:
                k = int(ask("¿Cuántas posiciones rotar? "))
                r = grupos.rotar(k)
                print("En turno:", r)
            except ValueError:
                print("Número inválido.")

        elif op == "5":
            lista = grupos.recorrer(2)
            if not lista:
                print("(sin grupos)")
            for i, g in enumerate(lista, 1):
                print(f"{i:>2}. {g['nombre_grupo']} (tutor={g['tutor']}, tema={g['tema']})")

        elif op == "6":
            try:
                grupos.exportar_json(ROUTE_GRUP)
                print(f"Exportado a {ROUTE_GRUP}")
            except Exception as e:
                print(f"Error al exportar: {e}")

        elif op == "7":
            try:
                grupos.importar_json(ROUTE_GRUP)
                print(f"Importado desde {ROUTE_GRUP}")
            except FileNotFoundError:
                print("No existe el JSON.")
            except ValueError as e:
                print(f"JSON inválido: {e}")

        elif op == "0":
            break

        pause()


# ============================================================
# MÓDULO 4: Reportes
# ============================================================
def menu_reportes():
    while True:
        print("""
        --- REPORTES ---
        1. Top 3 mejores promedios
        2. Siguiente grupo en turno (rota 1)
        3. Cantidad de inscritos
        0. Volver
        """)

        op = ask("Opción: ")

        if op == "1":
            promedios = []
            for s in historial.recorrer_adelante():
                if s["materias"]:
                    prom = sum(m["nota"] for m in s["materias"]) / len(s["materias"])
                    promedios.append((f"{s['anio']}-{s['term']}", round(prom, 2)))
            promedios.sort(key=lambda x: x[1], reverse=True)
            if not promedios:
                print("(sin historial)")
            for i, (sem, p) in enumerate(promedios[:3], 1):
                print(f"  {i}. {sem} -> {p}")

        elif op == "2":
            # ← CORREGIDO: rota 1 posición y luego muestra el siguiente
            if len(grupos) == 0:
                print("(sin grupos)")
            else:
                g = grupos.rotar(1)
                print("Siguiente grupo en turno:", g)

        elif op == "3":
            print("Total inscritos:", len(inscritos))

        elif op == "0":
            break

        pause()


# ============================================================
# MENÚ PRINCIPAL
# ============================================================
def main():
    while True:
        print("""
========== MENÚ PRINCIPAL ==========
1. Inscritos (Lista Simple)
2. Historial  (Lista Doble)
3. Grupos     (Lista Circular)
4. Reportes
5. Salir
""")

        op = ask("Opción: ")

        if op == "1":
            menu_inscritos()
        elif op == "2":
            menu_historial()
        elif op == "3":
            menu_grupos()
        elif op == "4":
            menu_reportes()
        elif op == "5":
            print("Hasta pronto.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()