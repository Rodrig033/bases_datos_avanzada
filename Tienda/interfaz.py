import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QPushButton,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QComboBox,
    QStackedWidget,
    QMessageBox,
    QHeaderView,
    QFrame,
)


class InicioWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        titulo = QLabel("Bienvenido a Tienda La Económica")
        titulo.setObjectName("titulo")

        descripcion = QLabel(
            "Sistema de gestión de productos, clientes, proveedores y ventas."
        )
        descripcion.setObjectName("subtitulo")

        layout.addWidget(titulo)
        layout.addWidget(descripcion)
        layout.addStretch()

        self.setLayout(layout)


class ProductosWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.productos = [
            ["P001", "Arroz", "Arroz blanco", 38.00, 27],
            ["P002", "Frijol", "Frijol negro", 42.00, 13],
            ["P003", "Lentejas", "Lentejas verdes", 30.00, 10],
        ]

        layout = QVBoxLayout()

        titulo = QLabel("Productos")
        titulo.setObjectName("titulo")

        layout.addWidget(titulo)

        botones = QHBoxLayout()

        boton_agregar = QPushButton("Agregar")
        boton_modificar = QPushButton("Modificar")
        boton_eliminar = QPushButton("Eliminar")

        botones.addWidget(boton_agregar)
        botones.addWidget(boton_modificar)
        botones.addWidget(boton_eliminar)
        botones.addStretch()

        layout.addLayout(botones)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(
            [
                "Código",
                "Nombre",
                "Descripción",
                "Precio",
                "Existencias",
            ]
        )

        self.tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(self.tabla)

        self.setLayout(layout)

        self.mostrar_productos()

        boton_agregar.clicked.connect(self.agregar_producto)
        boton_modificar.clicked.connect(self.modificar_producto)
        boton_eliminar.clicked.connect(self.eliminar_producto)

    def mostrar_productos(self):

        self.tabla.setRowCount(len(self.productos))

        for fila, producto in enumerate(self.productos):

            for columna, valor in enumerate(producto):

                self.tabla.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(str(valor))
                )

    def agregar_producto(self):

        dialogo = ProductoDialog(self)

        if dialogo.exec():

            producto = dialogo.obtener_producto()

            self.productos.append(producto)

            self.mostrar_productos()

    def modificar_producto(self):

        fila = self.tabla.currentRow()

        if fila < 0:
            QMessageBox.warning(
                self,
                "Modificar producto",
                "Selecciona un producto."
            )
            return

        dialogo = ProductoDialog(self, self.productos[fila])

        if dialogo.exec():

            self.productos[fila] = dialogo.obtener_producto()

            self.mostrar_productos()

    def eliminar_producto(self):

        fila = self.tabla.currentRow()

        if fila < 0:
            QMessageBox.warning(
                self,
                "Eliminar producto",
                "Selecciona un producto."
            )
            return

        respuesta = QMessageBox.question(
            self,
            "Eliminar producto",
            "¿Deseas eliminar el producto seleccionado?"
        )

        if respuesta == QMessageBox.StandardButton.Yes:

            del self.productos[fila]

            self.mostrar_productos()


class ProductoDialog(QMessageBox):

    def __init__(self, parent=None, producto=None):
        super().__init__(parent)

        self.setWindowTitle("Producto")

        self.widget = QWidget()

        layout = QFormLayout()

        self.codigo = QLineEdit()
        self.nombre = QLineEdit()
        self.descripcion = QLineEdit()

        self.precio = QDoubleSpinBox()
        self.precio.setMaximum(999999)
        self.precio.setDecimals(2)

        self.existencias = QSpinBox()
        self.existencias.setMaximum(999999)

        layout.addRow("Código:", self.codigo)
        layout.addRow("Nombre:", self.nombre)
        layout.addRow("Descripción:", self.descripcion)
        layout.addRow("Precio:", self.precio)
        layout.addRow("Existencias:", self.existencias)

        self.widget.setLayout(layout)

        self.layout().addWidget(self.widget, 1, 0, 1, 2)

        self.setStandardButtons(
            QMessageBox.StandardButton.Ok
            | QMessageBox.StandardButton.Cancel
        )

        if producto:

            self.codigo.setText(str(producto[0]))
            self.nombre.setText(str(producto[1]))
            self.descripcion.setText(str(producto[2]))
            self.precio.setValue(float(producto[3]))
            self.existencias.setValue(int(producto[4]))

    def obtener_producto(self):

        return [
            self.codigo.text(),
            self.nombre.text(),
            self.descripcion.text(),
            self.precio.value(),
            self.existencias.value(),
        ]


class CategoriasWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        titulo = QLabel("Categorías")
        titulo.setObjectName("titulo")

        layout.addWidget(titulo)

        tabla = QTableWidget()
        tabla.setColumnCount(3)
        tabla.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Descripción"]
        )

        categorias = [
            ["CAT001", "Alimentos", "Productos alimenticios"],
            ["CAT002", "Bebidas", "Bebidas y líquidos"],
            ["CAT003", "Limpieza", "Productos de limpieza"],
        ]

        tabla.setRowCount(len(categorias))

        for fila, categoria in enumerate(categorias):

            for columna, valor in enumerate(categoria):

                tabla.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(str(valor))
                )

        tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(tabla)

        self.setLayout(layout)


class ProveedoresWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        titulo = QLabel("Proveedores")
        titulo.setObjectName("titulo")

        layout.addWidget(titulo)

        tabla = QTableWidget()
        tabla.setColumnCount(5)

        tabla.setHorizontalHeaderLabels(
            [
                "ID",
                "Nombre",
                "Teléfono",
                "Correo",
                "Dirección",
            ]
        )

        proveedores = [
            [
                "PROV001",
                "Distribuidora Central",
                "2281234567",
                "central@correo.com",
                "Xalapa, Veracruz",
            ],
            [
                "PROV002",
                "Abarrotes del Sur",
                "2287654321",
                "sur@correo.com",
                "Coatepec, Veracruz",
            ],
        ]

        tabla.setRowCount(len(proveedores))

        for fila, proveedor in enumerate(proveedores):

            for columna, valor in enumerate(proveedor):

                tabla.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(str(valor))
                )

        tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(tabla)

        self.setLayout(layout)


class ClientesWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        titulo = QLabel("Clientes")
        titulo.setObjectName("titulo")

        layout.addWidget(titulo)

        tabla = QTableWidget()
        tabla.setColumnCount(4)

        tabla.setHorizontalHeaderLabels(
            [
                "ID",
                "Nombre",
                "Teléfono",
                "Correo",
            ]
        )

        clientes = [
            [
                "CLI001",
                "Rodrigo Farid",
                "2281234567",
                "farid@universidad.edu.mx",
            ],
            [
                "CLI002",
                "Ana López",
                "2289876543",
                "ana@correo.com",
            ],
        ]

        tabla.setRowCount(len(clientes))

        for fila, cliente in enumerate(clientes):

            for columna, valor in enumerate(cliente):

                tabla.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(str(valor))
                )

        tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(tabla)

        self.setLayout(layout)


class VentasWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        titulo = QLabel("Registrar venta")
        titulo.setObjectName("titulo")

        layout.addWidget(titulo)

        formulario = QFormLayout()

        self.cliente = QComboBox()
        self.cliente.addItems(
            [
                "CLI001 - Rodrigo Farid",
                "CLI002 - Ana López",
            ]
        )

        self.producto = QComboBox()
        self.producto.addItems(
            [
                "P001 - Arroz - $38.00",
                "P002 - Frijol - $42.00",
                "P003 - Lentejas - $30.00",
            ]
        )

        self.cantidad = QSpinBox()
        self.cantidad.setMinimum(1)
        self.cantidad.setMaximum(1000)

        formulario.addRow("Cliente:", self.cliente)
        formulario.addRow("Producto:", self.producto)
        formulario.addRow("Cantidad:", self.cantidad)

        layout.addLayout(formulario)

        boton_agregar = QPushButton("Agregar producto")
        layout.addWidget(boton_agregar)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)

        self.tabla.setHorizontalHeaderLabels(
            [
                "Producto",
                "Cantidad",
                "Precio unitario",
                "Subtotal",
            ]
        )

        self.tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(self.tabla)

        self.total = QLabel("Total: $0.00")
        self.total.setObjectName("total")

        layout.addWidget(self.total)

        self.setLayout(layout)

        self.detalles = []

        boton_agregar.clicked.connect(self.agregar_producto)

    def agregar_producto(self):

        productos = {
            0: ("Arroz", 38.00),
            1: ("Frijol", 42.00),
            2: ("Lentejas", 30.00),
        }

        indice = self.producto.currentIndex()

        nombre, precio = productos[indice]

        cantidad = self.cantidad.value()

        subtotal = precio * cantidad

        self.detalles.append(
            [
                nombre,
                cantidad,
                precio,
                subtotal,
            ]
        )

        self.mostrar_detalles()

    def mostrar_detalles(self):

        self.tabla.setRowCount(len(self.detalles))

        total = 0

        for fila, detalle in enumerate(self.detalles):

            for columna, valor in enumerate(detalle):

                if isinstance(valor, float):

                    texto = f"${valor:.2f}"

                else:

                    texto = str(valor)

                self.tabla.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(texto)
                )

            total += detalle[3]

        self.total.setText(
            f"Total: ${total:.2f}"
        )


class ConsultasWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        titulo = QLabel("Consultas")
        titulo.setObjectName("titulo")

        layout.addWidget(titulo)

        botones = QHBoxLayout()

        boton_todos = QPushButton("Todos los productos")
        boton_precio = QPushButton("Precio > $35")
        boton_stock = QPushButton("Stock bajo")
        boton_proveedor = QPushButton("Por proveedor")
        boton_ventas = QPushButton("Total de ventas")

        botones.addWidget(boton_todos)
        botones.addWidget(boton_precio)
        botones.addWidget(boton_stock)
        botones.addWidget(boton_proveedor)
        botones.addWidget(boton_ventas)

        layout.addLayout(botones)

        self.resultado = QLabel(
            "Selecciona una consulta."
        )

        self.resultado.setWordWrap(True)

        layout.addWidget(self.resultado)

        layout.addStretch()

        self.setLayout(layout)

        boton_todos.clicked.connect(
            lambda: self.mostrar_resultado(
                "P001 Arroz\n"
                "P002 Frijol\n"
                "P003 Lentejas"
            )
        )

        boton_precio.clicked.connect(
            lambda: self.mostrar_resultado(
                "Productos con precio mayor a $35:\n\n"
                "P001 - Arroz - $38.00\n"
                "P002 - Frijol - $42.00"
            )
        )

        boton_stock.clicked.connect(
            lambda: self.mostrar_resultado(
                "Productos con stock menor a 15:\n\n"
                "P002 - Frijol - 13\n"
                "P003 - Lentejas - 10"
            )
        )

        boton_proveedor.clicked.connect(
            lambda: self.mostrar_resultado(
                "Productos de Distribuidora Central:\n\n"
                "P001 - Arroz\n"
                "P002 - Frijol\n"
                "P003 - Lentejas"
            )
        )

        boton_ventas.clicked.connect(
            lambda: self.mostrar_resultado(
                "Total de ventas: $198.00"
            )
        )

    def mostrar_resultado(self, texto):

        self.resultado.setText(texto)


class VentanaPrincipal(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Tienda La Económica"
        )

        self.resize(1200, 700)

        contenedor = QWidget()

        layout_principal = QHBoxLayout()

        contenedor.setLayout(layout_principal)

        self.setCentralWidget(contenedor)

        # Menú lateral

        menu = QFrame()

        menu.setFixedWidth(220)

        menu_layout = QVBoxLayout()

        menu.setLayout(menu_layout)

        titulo = QLabel(
            "TIENDA\nLA ECONÓMICA"
        )

        titulo.setObjectName("menu_titulo")

        menu_layout.addWidget(titulo)

        self.boton_inicio = QPushButton("Inicio")
        self.boton_productos = QPushButton("Productos")
        self.boton_categorias = QPushButton("Categorías")
        self.boton_proveedores = QPushButton("Proveedores")
        self.boton_clientes = QPushButton("Clientes")
        self.boton_ventas = QPushButton("Ventas")
        self.boton_consultas = QPushButton("Consultas")

        botones = [
            self.boton_inicio,
            self.boton_productos,
            self.boton_categorias,
            self.boton_proveedores,
            self.boton_clientes,
            self.boton_ventas,
            self.boton_consultas,
        ]

        for boton in botones:

            boton.setCursor(Qt.CursorShape.PointingHandCursor)

            menu_layout.addWidget(boton)

        menu_layout.addStretch()

        layout_principal.addWidget(menu)

        # Área de contenido

        self.paginas = QStackedWidget()

        self.paginas.addWidget(
            InicioWidget()
        )

        self.paginas.addWidget(
            ProductosWidget()
        )

        self.paginas.addWidget(
            CategoriasWidget()
        )

        self.paginas.addWidget(
            ProveedoresWidget()
        )

        self.paginas.addWidget(
            ClientesWidget()
        )

        self.paginas.addWidget(
            VentasWidget()
        )

        self.paginas.addWidget(
            ConsultasWidget()
        )

        layout_principal.addWidget(
            self.paginas
        )

        # Navegación

        self.boton_inicio.clicked.connect(
            lambda: self.paginas.setCurrentIndex(0)
        )

        self.boton_productos.clicked.connect(
            lambda: self.paginas.setCurrentIndex(1)
        )

        self.boton_categorias.clicked.connect(
            lambda: self.paginas.setCurrentIndex(2)
        )

        self.boton_proveedores.clicked.connect(
            lambda: self.paginas.setCurrentIndex(3)
        )

        self.boton_clientes.clicked.connect(
            lambda: self.paginas.setCurrentIndex(4)
        )

        self.boton_ventas.clicked.connect(
            lambda: self.paginas.setCurrentIndex(5)
        )

        self.boton_consultas.clicked.connect(
            lambda: self.paginas.setCurrentIndex(6)
        )

        self.aplicar_estilos()

    def aplicar_estilos(self):

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #f5f6fa;
            }

            QFrame {
                background-color: #20232a;
            }

            QLabel#menu_titulo {
                color: white;
                font-size: 22px;
                font-weight: bold;
                padding: 20px;
            }

            QPushButton {
                padding: 12px;
                font-size: 14px;
                border: none;
                border-radius: 6px;
            }

            QFrame QPushButton {
                color: white;
                background-color: #2f333b;
                text-align: left;
            }

            QFrame QPushButton:hover {
                background-color: #444a54;
            }

            QLabel#titulo {
                font-size: 28px;
                font-weight: bold;
                padding-bottom: 10px;
            }

            QLabel#subtitulo {
                font-size: 16px;
            }

            QLabel#total {
                font-size: 20px;
                font-weight: bold;
            }

            QTableWidget {
                background-color: white;
                border: 1px solid #dcdde1;
                gridline-color: #dcdde1;
            }

            QHeaderView::section {
                padding: 8px;
                font-weight: bold;
            }

            QLineEdit,
            QSpinBox,
            QDoubleSpinBox,
            QComboBox {
                padding: 6px;
            }
            """
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()

    ventana.show()

    sys.exit(app.exec())