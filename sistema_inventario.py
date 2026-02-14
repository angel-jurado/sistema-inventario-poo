# sistema de inventario - trabajo 2 (POO)

class Producto:
    def __init__(self, nombre, precio, cantidad):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio.")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser >= 0.")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero >= 0.")

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def actualizar_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser >= 0.")
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser un entero >= 0.")
        self.cantidad = int(nueva_cantidad)

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.nombre} | Precio: {self.precio:.2f} | Cantidad: {self.cantidad} | Total: {self.calcular_valor_total():.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")

        # si ya existe, sumamos cantidad y actualizamos precio
        existente = self.buscar_producto(producto.nombre)
        if existente is not None:
            existente.actualizar_cantidad(existente.cantidad + producto.cantidad)
            existente.actualizar_precio(producto.precio)
        else:
            self.productos.append(producto)

    def buscar_producto(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre de busqueda no puede estar vacio.")

        objetivo = nombre.strip().lower()
        for p in self.productos:
            if p.nombre.lower() == objetivo:
                return p
        return None

    def calcular_valor_inventario(self):
        total = 0.0
        for p in self.productos:
            total += p.calcular_valor_total()
        return total

    def listar_productos(self):
        if len(self.productos) == 0:
            print("El inventario esta vacio.")
            return

        print("\n--- Productos en inventario ---")
        for p in self.productos:
            print(p)


def pedir_texto_no_vacio(msg):
    while True:
        texto = input(msg).strip()
        if texto != "":
            return texto
        print("Error: no puede estar vacio.")


def pedir_float_no_negativo(msg):
    while True:
        entrada = input(msg).strip().replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Error: introduce un numero valido.")
            continue
        if valor < 0:
            print("Error: no puede ser negativo.")
            continue
        return valor


def pedir_int_no_negativo(msg):
    while True:
        entrada = input(msg).strip()
        try:
            valor = int(entrada)
        except ValueError:
            print("Error: introduce un entero valido.")
            continue
        if valor < 0:
            print("Error: no puede ser negativo.")
            continue
        return valor


def menu_principal(inventario):
    while True:
        print("\n===== MENU INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Elige una opcion (1-5): ").strip()

        if opcion == "1":
            try:
                nombre = pedir_texto_no_vacio("Nombre del producto: ")
                precio = pedir_float_no_negativo("Precio (>= 0): ")
                cantidad = pedir_int_no_negativo("Cantidad (entero >= 0): ")
                prod = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(prod)
                print("Producto agregado/actualizado correctamente.")
            except (ValueError, TypeError) as e:
                print(f"Error al agregar producto: {e}")

        elif opcion == "2":
            try:
                nombre = pedir_texto_no_vacio("Nombre a buscar: ")
                encontrado = inventario.buscar_producto(nombre)
                if encontrado is None:
                    print("Producto no encontrado.")
                else:
                    print("Producto encontrado:")
                    print(encontrado)
            except ValueError as e:
                print(f"Error en busqueda: {e}")

        elif opcion == "3":
            inventario.listar_productos()

        elif opcion == "4":
            total = inventario.calcular_valor_inventario()
            print(f"Valor total del inventario: {total:.2f}")

        elif opcion == "5":
            print("Gracias por usar el sistema de inventario.")
            break

        else:
            print("Opcion no valida. Elige un numero del 1 al 5.")


# --- programa principal ---
inv = Inventario()
menu_principal(inv)
