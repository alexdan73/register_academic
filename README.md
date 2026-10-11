Módulo de Listas Enlazadas para Registros Académicos
Descripción
Este proyecto implementa desde cero tres tipos de listas enlazadas en Python para gestionar registros académicos:

Lista Simple: estudiantes inscritos en una asignatura.

Lista Doble: historial académico por semestre (recorrible hacia adelante y hacia atrás).

Lista Circular: rotación de grupos de prácticas (con búsqueda recursiva obligatoria).

Incluye operaciones de inserción, eliminación, búsqueda, recorrido y persistencia en formatos CSV y JSON. Todo se maneja a través de un menú de consola interactivo.

Estructura del Proyecto

    /reto3_listas
    │
    ├── src/
    │   ├── simple_node.py
    │   ├── simple_list.py
    │   ├── double_node.py
    │   ├── double_list.py
    │   ├── circular_node.py
    │   ├── circular_list.py
    │   ├── persistence_csv.py
    │   ├── persistence_json.py
    │   └── app.py                 # Menú principal
    │
    ├── data/                      # Se crea automáticamente al ejecutar
    │   ├── inscritos.csv
    │   ├── historial.json
    │   └── grupos.json
    │
    └── README.md

Requisitos
Python 3.8 o superior

No se requieren librerías externas. Solo se utiliza la biblioteca estándar (os, sys, csv, json).

1. Ejecución
   Abre una terminal y sitúate en la carpeta src (donde está app.py):

    cd ruta/al/proyecto/src

2. Ejecuta el programa:

    bash
    python app.py
3. Aparecera el menú principal

    ========== MENÚ PRINCIPAL ==========
    1. Inscritos (Lista Simple)
    2. Historial  (Lista Doble)
    3. Grupos     (Lista Circular)
    4. Reportes
    5. Salir

    Funcionalidades por Módulo
1. Inscritos (Lista Simple)
    Agregar estudiante (ID, nombres, correo).

    Eliminar por ID.

    Buscar por ID.

    Mostrar todos los inscritos.

    Exportar a data/inscritos.csv.

    Importar desde data/inscritos.csv.

2. Historial (Lista Doble)
    Agregar semestre (ordenado automáticamente por año y término).

    Buscar semestre (formato AAAA-T, ej. 2024-1).

    Recorrer hacia adelante y hacia atrás.

    Eliminar semestre.

    Exportar a data/historial.json.

    Importar desde data/historial.json.

3. Grupos (Lista Circular)
    Agregar grupo (nombre, tutor, tema).

    Eliminar grupo.

    Búsqueda recursiva por nombre de grupo.

    Rotar k posiciones (cambia el turno actual).

    Recorrer el ciclo (por defecto 2 vueltas).

    Exportar a data/grupos.json.

    Importar desde data/grupos.json.

4. Reportes
    Top 3 mejores promedios del historial académico.

    Siguiente grupo en turno (rota 1 posición y muestra el nuevo turno).

    Cantidad total de inscritos.

    Persistencia
    Lista	    Formato	    Archivo
    Inscritos	CSV	        data/inscritos.csv
    Historial	JSON	    data/historial.json
    Grupos	    JSON	    data/grupos.json

    CSV se usa para datos tabulares homogéneos (inscritos).

    JSON se usa para estructuras jerárquicas o con texto libre (historial y grupos).

    Casos de Prueba Mínimos
    Puedes verificar el correcto funcionamiento siguiendo estos pasos:

    Lista Simple
    Agregar 3 inscritos con IDs 1, 2 y 3.

    Buscar el ID 2.

    Eliminar el ID 3.

    Mostrar la lista (deben quedar IDs 1 y 2).

    Exportar CSV.

    Importar CSV (opcional: limpiar antes con la opción de importar, que reemplaza los datos).

    Volver a mostrar.

    Lista Doble
    Insertar semestres desordenados: 2024-2, 2023-1, 2024-1.

    Recorrer hacia adelante: debe mostrar 2023-1, 2024-1, 2024-2.

    Recorrer hacia atrás: orden inverso.

    Exportar JSON e importar para comprobar persistencia.

    Lista Circular
    Agregar 3 grupos: A, B, C.

    Buscar recursivamente el grupo C.

    Rotar 2 posiciones y mostrar el nuevo turno.

    Recorrer 2 vueltas para ver el ciclo completo.

    Eliminar el grupo B y comprobar que el ciclo sigue funcionando con A y C.

    Notas de Implementación
    Recursividad obligatoria: La búsqueda en la lista circular (buscar_recursivo) es recursiva.

    Nodos desde cero: Se definieron clases SimpleNode, DoubleNode y CircularNode. No se usan listas nativas para almacenar nodos.

    Complejidad: Las operaciones de inserción, búsqueda y eliminación son O(n) en promedio. La rotación es O(k). El recorrido es O(n).

    Manejo de errores: Las importaciones validan existencia y formato de archivos; los menús capturan entradas inválidas.

