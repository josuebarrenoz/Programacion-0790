Examen de Programación: CRUD de Inventario de Supermercado

El programa funciona a partir de main.py 
El programa crea un archivo .json a empezar en la ejecución. 

Abajo el detalle de la Prueba que resuelve main.py

Instrucciones Generales: Este examen consiste en im plementar un sistema básico de gestión de inventario para un supermercado utilizando Python. El sistema debe permitir a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los productos en el inventario. Los datos del inventario deben estar almacenados en un archivo JSON llamado inventario.json.

Requisitos del Programa

Crear Producto:
Permitir al usuario agregar un nuevo producto al inventario.
Cada producto debe tener un nombre, precio y cantidad en stock.
Verificar que no se agreguen productos duplicados (mismo nombre).

Leer/Mostrar Productos:
Mostrar la lista completa de productos disponibles en el inventario.
Mostrar la información detallada de un producto específico, solicitando su nombre.

Actualizar Producto:
Permitir al usuario actualizar la información de un producto existente (nombre, precio o cantidad).
Asegurarse de que el producto exista antes de intentar actualizarlo.

Eliminar Producto:
Permitir al usuario eliminar un producto del inventario.
Asegurarse de que el producto exista antes de intentar eliminarlo.

Implementación

El programa debe funcionar a través de un menú que permita al usuario elegir qué operación realizar. El menú debe seguir mostrándose después de completar una operación, permitiendo al usuario realizar múltiples operaciones hasta que elija salir.

Ejemplo de Estructura del Menú:
--- Gestión de Inventario ---
1. Crear producto
2. Mostrar todos los productos
3. Mostrar información de un producto
4. Actualizar producto
5. Eliminar producto
6. Salir
Elige una opción:

Tareas:
Implementa la funcionalidad para cada una de las opciones del menú.
Usa la librería json para leer y escribir en el archivo inventario.json.
Asegúrate de que los datos se manejan correctamente en todas las operaciones CRUD.
Prueba el programa con diferentes datos para asegurarte de que funciona correctamente en todos los casos.



