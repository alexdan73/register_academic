from double_node import DoubleNode


class DoubleList:

    def __init__(self):
        self.head = None
        self.queue = None   # cola = último nodo
        self._size = 0

    # ---------- Helpers ----------
    @staticmethod
    def _key(semester):
        return (semester["anio"], semester["term"])

    @staticmethod
    def _parse(semester):
        # ← CORREGIDO: robusto ante formatos inválidos
        if isinstance(semester, str):
            try:
                a, t = semester.split("-")
                return int(a), int(t)
            except (ValueError, AttributeError):
                raise ValueError(
                    f"Formato de semestre inválido: '{semester}'. Use 'AAAA-T' (ej. 2024-1)."
                )
        try:
            return int(semester["anio"]), int(semester["term"])
        except (KeyError, TypeError, ValueError):
            raise ValueError("El registro de semestre debe tener 'anio' y 'term'.")

    # ---------- Inserción ordenada ----------
    def insertar_ordenado(self, record):
        new_node = DoubleNode(record)
        if self.head is None:
            self.head = self.queue = new_node
        else:
            current = self.head
            while current and self._key(current.value) < self._key(record):
                current = current.next

            if current is None:
                # va al final
                new_node.previous = self.queue
                self.queue.next = new_node
                self.queue = new_node
            elif current.previous is None:
                # va al inicio
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node
            else:
                prev = current.previous
                prev.next = new_node
                new_node.previous = prev
                new_node.next = current
                current.previous = new_node
        self._size += 1
        return new_node.value

    # ---------- Eliminación ----------
    def eliminar(self, semester):
        try:
            a, t = self._parse(semester)
        except ValueError:
            return False
        current = self.head
        while current:
            if (current.value["anio"], current.value["term"]) == (a, t):
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.previous = current.previous
                else:
                    self.queue = current.previous
                self._size -= 1
                return True
            current = current.next
        return False

    # ---------- Búsqueda ----------
    def buscar(self, semester):
        try:
            year, term = self._parse(semester)
        except ValueError:
            return None
        current = self.head
        while current:
            if (current.value["anio"], current.value["term"]) == (year, term):
                return current.value
            current = current.next
        return None

    # ---------- Recorridos ----------
    def recorrer_adelante(self):
        out, current = [], self.head
        while current:
            out.append(current.value)
            current = current.next
        return out

    def recorrer_atras(self):
        out, current = [], self.queue
        while current:
            out.append(current.value)
            current = current.previous
        return out

    # ---------- Persistencia ----------
    def to_dict(self):
        return {"semestres": self.recorrer_adelante()}

    def from_dict(self, data):
        self.head = self.queue = None
        self._size = 0
        for s in data.get("semestres", []):
            self.insertar_ordenado(s)

    def exportar_json(self, ruta):
        # ← NUEVO
        from persistence_json import export_json
        export_json(self, ruta)

    def importar_json(self, ruta):
        # ← NUEVO
        from persistence_json import import_json
        import_json(self, ruta)

    def __len__(self):
        return self._size