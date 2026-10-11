from simple_node import SimpleNode


class SimpleList:

    def __init__(self):
        self.head = None
        self._size = 0

    # ---------- Inserción ----------
    def insertar_final(self, student):
        new_node = SimpleNode(student)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
        return new_node.value

    def insertar_inicio(self, student):
        new_node = SimpleNode(student)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        return new_node.value

    # ---------- Eliminación ----------
    def eliminar(self, id_student):
        current, previous = self.head, None
        while current:
            if current.value.get("id") == id_student:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self._size -= 1
                return True
            previous, current = current, current.next
        return False

    # ---------- Búsqueda ----------
    def buscar(self, id_student):
        current = self.head
        while current:
            if current.value.get("id") == id_student:
                return current.value
            current = current.next
        return None

    # ---------- Recorrido ----------
    def recorrer(self):
        out, current = [], self.head
        while current:
            out.append(current.value)
            current = current.next
        return out

    # ---------- Persistencia ----------
    def to_dict(self):
        return {"estudiantes": self.recorrer()}

    def from_dict(self, data):
        self.head, self._size = None, 0
        for student in data.get("estudiantes", []):
            self.insertar_final(student)

    def exportar_csv(self, ruta):
        # ← NUEVO: método de conveniencia
        from persistence_csv import export_csv
        export_csv(self, ruta)

    def importar_csv(self, ruta):
        # ← NUEVO: método de conveniencia
        from persistence_csv import import_csv
        import_csv(self, ruta)

    def clear(self):
        self.head = None
        self._size = 0

    # ---------- Alias en inglés (compatibilidad) ----------
    insertion_final = insertar_final
    insertion_start = insertar_inicio
    delete = eliminar
    search = buscar
    scroll = recorrer

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next