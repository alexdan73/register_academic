from circular_node import CircularNode


class CircularList:

    def __init__(self):
        self.current = None
        self._size = 0

    # ---------- Inserción ----------
    def insertar(self, group):
        new_node = CircularNode(group)
        if self.current is None:
            new_node.next = new_node
            self.current = new_node
        else:
            # avanzar hasta el nodo anterior a current
            node = self.current
            while node.next is not self.current:
                node = node.next
            node.next = new_node
            new_node.next = self.current
        self._size += 1
        return new_node.value

    # ---------- Eliminación ----------
    def eliminar(self, group_name):
        if self.current is None:
            return False

        previous, node, start = self.current, self.current.next, self.current
        while True:
            if node.value.get("nombre_grupo") == group_name:
                if node.next is node:              # único nodo
                    self.current = None
                else:
                    previous.next = node.next
                    if node is self.current:
                        self.current = node.next
                self._size -= 1
                return True
            previous = node
            node = node.next
            if node is start:
                return False

    # ---------- Búsqueda recursiva (OBLIGATORIA) ----------
    def buscar_recursivo(self, value, node=None, start=None):
        if self.current is None:
            return None
        if node is None:
            node = self.current
            start = self.current
        if node.value.get("nombre_grupo") == value:
            return node.value
        if node.next is start:
            return None
        return self.buscar_recursivo(value, node.next, start)

    # ---------- Rotación ----------
    def rotar(self, k):
        if self.current is None or self._size == 0:
            return None
        for _ in range(k % self._size):
            self.current = self.current.next
        return self.current.value

    def siguiente(self):
        return self.current.value if self.current else None

    # ---------- Recorrido ----------
    def recorrer(self, n_vueltas=1):
        out = []
        if self.current is None:
            return out
        node = self.current
        for _ in range(self._size * n_vueltas):
            out.append(node.value)
            node = node.next
        return out

    # ---------- Persistencia ----------
    def to_dict(self):
        return {"grupos": self.recorrer(1)}

    def from_dict(self, data):
        self.current = None
        self._size = 0
        for g in data.get("grupos", []):
            self.insertar(g)

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