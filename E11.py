def procesar_inventario():
    print("--- Sistema de Despacho de Almacén ---")

    # Pedir cantidad de productos
    n = int(input("¿Cuántos productos querés registrar? "))

    productos = []
    stock = []
    precios = []
    pedidos_pendientes = []

    # Cargar datos de cada producto
    for i in range(n):
        print(f"\n-- Producto {i + 1} --")
        nombre = input("  Nombre del producto: ")
        cantidad_stock = int(input("  Stock disponible: "))
        precio = float(input("  Precio unitario: $"))
        pedido = int(input("  Cantidad pedida: "))

        productos.append(nombre)
        stock.append(cantidad_stock)
        precios.append(precio)
        pedidos_pendientes.append(pedido)

    # Procesar pedidos
    ventas_totales = 0
    print("\n--- Procesando pedidos ---")

    for i in range(len(productos)):
        nombre = productos[i]
        cantidad_pedida = pedidos_pendientes[i]
        stock_actual = stock[i]
        precio_unitario = precios[i]

        print(f"\nAnalizando pedido de: {nombre}")

        if stock_actual >= cantidad_pedida:       
            total_operacion = cantidad_pedida * precio_unitario
            ventas_totales += total_operacion
            stock[i] = stock_actual - cantidad_pedida
            print(f"  Pedido procesado. Stock restante: {stock[i]}")
        else:
            print(f"  Error: Stock insuficiente para {nombre}. Stock disponible: {stock_actual}, pedido: {cantidad_pedida}")

    print("\n---------------------------------------")
    print(f"Resumen del día. Ventas totales: ${ventas_totales:,.2f}")
    print(f"Estado final del stock: {dict(zip(productos, stock))}")

procesar_inventario()