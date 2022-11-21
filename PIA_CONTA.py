from os import sep
from prettytable import PrettyTable
import os
LimpiarPantalla = lambda: os.system('cls')

#region Metodos
def separador():
    print("="*60)

def productosABC():
    global Total_Anual
    LimpiarPantalla()
    # Producto A

    print("\t\tProducto A")
    print("PRIMER SEMESTRE")
    cant_A = int(input("No. de Unidades: "))
    precio_A = int(input("Precio: "))
    Importe_A = (cant_A * precio_A)
    print(f"El importe de Prodcuto A en el primer semestre es: {Importe_A}")
    print("\n")

    print("SEGUNDO SEMESTRE")
    cant_A2 = int(input("No. de Unidades: "))
    precio_A2 = int(input("Precio: "))
    Importe_A2 = (cant_A2 * precio_A2)
    print(f"El importe de Prodcuto A en el segundo semestre es: {Importe_A2}")
    print("\n")

    print("TOTAL Producto A: ")
    Total_A = (Importe_A + Importe_A2)
    print(Total_A)
    separador()

    print("VENTAS POR SEMESTRE")
    Total_Semestre = (Importe_A)
    Total_Semestre_2 = (Importe_A2)
    Total_Anual = (Total_A)
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL ANUAL'])
    t.add_row([Total_Semestre,Total_Semestre_2,Total_Anual])
    print(t)
    input("Pulse Enter para continuar...")
    separador()

def SaldoFlujo():
    LimpiarPantalla()

    # Saldo Clientes
    print(f"\tSALDO FLUJO DE EFECTIVO")
    separador()
    print("Saldo Clientes: $50,000 ")
    print("Entrada de efectivo: ")
    print("Cobranza 2010: $150,000")
    print('Total: $24,187,500')

    # Entradas
    print("\tENTRADAS")
    primer_año= int(input("Cobro Primer Año: "))
    segundo_año= int(input("Cobro Segundo Año: "))
    entradas_total= (primer_año + segundo_año)
    print(f"Total de Entradas: {entradas_total} ")
    total_clientes2= (total_clientes - entradas_total)
    print(f"Saldo Clientes: {total_clientes2}")
    separador()
    input("Pulse Enter para continuar...")

def PresupuestoProduccion():
    LimpiarPantalla()
    print("\tPRESUPUESTO DE PRODUCCION")
    separador()

    # Produccion A PRIMER SEMESTRE
    print(f"\t\tPresupuesto de Produccion PRODUCTO A Primer Semestre")
    no_unidades_A = int(input("No. de Unidades: "))
    inventario_finalA = int(input("Inventario Final: "))
    total_unidades = (no_unidades_A + inventario_finalA)
    print(f"Total de unidades es de: {total_unidades}")
    inventario_inicialA = int(input("Inventario  incial: "))
    unidades_producir = (total_unidades - inventario_inicialA)
    print(f"Las unidades a producir en primer semestre son: {unidades_producir}")
    
    # Produccion A SEGUNDO SEMESTRE
    print(f"\t\tPresupuesto de Produccion PRODUCTO A Segundo Semestre")
    no_unidades_A2 = int(input("No. de Unidades: "))
    inventario_finalA2 = int(input("Inventario Final: "))
    print("Total de unidades es de: ")
    total_unidades2 = (no_unidades_A2 + inventario_finalA2)
    print(f"Total de unidades es de: {total_unidades2}")
    inventario_inicialA2 = int(input("Inventario  incial: "))
    unidades_producirA2 = (total_unidades2 - inventario_inicialA2)
    print(f"Las unidades a producir en segundo semestre son: {unidades_producirA2}")

    # Produccion Total A
    print(f"\t\tProduccion Total PRODUCTO A")
    no_unidades_AT = (no_unidades_A + no_unidades_A2)
    print(f"Unidades a Vender: {no_unidades_AT}")
    print(f"Inventario Final: {inventario_finalA2}")
    Total_UnidadesA= (no_unidades_AT + inventario_finalA2)
    print(f"Total de unidades de: {Total_UnidadesA}")
    inventario_inicialA = inventario_finalA
    TotalT= (Total_UnidadesA - inventario_inicialA)
    print(f"Unidades Totales de PRODUCTO A: {TotalT}")
    separador()


def PresupuestoReqMateriales():
    LimpiarPantalla()
    print("\tPRESUPUESTO REQUERIMENTOS PARA MATERIALES")

    # Producto A
    print(f"\tPRODUCTO A")
    no_unidades_A = int(input("No. de Unidades PRIMER SEMESTRE: "))
    no_unidades_A2 = int(input("No. de Unidades SEGUNDO SEMESTRE: "))

    print("--Requerimentos de los Materiales A, B y C--")
    req_A = float(input("Requermientos Primer Semestre Material A: "))
    req_A2 = float(input("Requermientos Segundo Semestre Material A: "))

    req_B = float(input("Requerimentos Primer Semestre Material B: "))
    req_B2 = float(input("Requerimentos Segundo Semestre Material B: "))

    req_C = float(input("Requerimentos Primer Semestre Material C: "))
    req_C2 = float(input("Requerimentos Segundo Semestre Material C: "))

    total_A1 = (no_unidades_A * req_A)
    total_A2 = (no_unidades_A2 * req_A2)
    total_AT = (total_A1 + total_A2)
    total_B1 = (no_unidades_A * req_B)
    total_B2 = (no_unidades_A2 * req_B2)
    total_BT = (total_B1 + total_B2)
    total_C1 = (no_unidades_A * req_C)
    total_C2 = (no_unidades_A2 * req_C2)
    total_CT = (total_C1 + total_C2)

    print("TOTAL MATERIAL A REQUERIDO")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_A1,total_A2,total_AT])
    print(t)

    print("TOTAL MATERIAL B REQUERIDO")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_B1,total_B2,total_BT])
    print(t)

    print("TOTAL MATERIAL C REQUERIDO")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_C1,total_C2,total_CT])
    print(t)
    separador()
    input("Presione Enter para continuar...")

    
def PresupuestoCompraMateriales():

    LimpiarPantalla()
    print(f"\tPRESUPUESTO COMPRA MATERIALES")

    # Material A PRIMER SEMESTRE
    print("MATERIAL A")
    separador()
    print("Primer Semestre")
    req_A = int(input("Requerimento de materiales: "))
    inv_finalA = int(input("Inventario final: "))
    total_materialesA = (req_A + inv_finalA)
    print(f"Materiales: {total_materialesA} ")
    inventario_inicialA = int(input("Inventario incial: "))
    total_materialesA_t = (total_materialesA - inventario_inicialA)
    print(f"Material a comprar: {total_materialesA_t}")
    precio_compra = int(input("Precio de compra: "))
    TotalMatA = (total_materialesA_t * precio_compra)
    print(f"Total Material A: {TotalMatA}")
    separador()

    # Material A SEGUNDO SEMESTRE
    print("Segundo Semestre")
    req_A2 = int(input("Requerimento de materiales: "))
    inv_finalA2 = int(input("Inventario final: "))
    total_materialesA2 = (req_A2 + inv_finalA2)
    print(f"Total de Materiales: {total_materialesA2} ")
    inventario_inicialA2 = int(input("Inventario incial: "))
    total_materialesA_t2 = (total_materialesA2 - inventario_inicialA2)
    print(f"Total de material a comprar: {total_materialesA_t2}")
    precio_compra = float(input("Precio de compra: "))
    TotalMatA2 = (total_materialesA_t2 * precio_compra)
    print(f"Total Material A Segundo Semestre: {TotalMatA2}")


    # Material A TOTAL
    LimpiarPantalla()
    print("\nTOTAL MATERIAL A")
    separador()
    print(f"Requerimentos de Materiales: {req_A + req_A2}")
    print(f"Inventario Final: {inv_finalA + inv_finalA2}")
    print(f"Materiales: {total_materialesA + total_materialesA_t2}")
    print(f"Inventario Inicial: {inventario_inicialA + inventario_inicialA2}")
    print(f"Materiales a comprar: {total_materialesA_t + total_materialesA_t2}")
    print(f"Material: ${TotalMatA + TotalMatA2} ")
    separador()
    input("Presione Enter para continuar...")


def SaldoProvFlujo():
    LimpiarPantalla()
    print("\tSALDOS PROVEEDORES Y FLUJOS DE SALIDA")
    separador()
    print('Saldo de proveedores 2009: $60,000')
    print('Compras 2010: $1,704,304')
    print('Total de proveedores 2010: $1,764,304')
    print('            ')
    print('--- Salidas de efectivo ---')
    print('Salida a proveedores 2009: $60,000')
    print('Pago de proveedores 2010: $1,300,000')
    print('              ')
    print('Total de pago de proveedores 2010: $1,360,000')
    print('Saldo proveedores 2009: $404,304')
    print('')

def manoObraDirecta():
    LimpiarPantalla()
    global total_horas_reqSum
    print("\tPRESUPUESTO PARA MANO DE OBRA DIRECTA")

    # Producto A PRIMER SEMESTRE
    separador()
    print("PRODUCTO A PRIMER SEMESTRE")
    unidades_p1= int(input("Unidades a producir: "))
    horas_por_unidad= int(input("Horas requeridas por unidad: "))
    total_horas_req1 = (unidades_p1 * horas_por_unidad)
    print(f"Total de horas requeridas: {total_horas_req1}")
    cuota_por_hora= int(input("Cuota por hora: "))
    importe_mano_obra_directa = total_horas_req1 * cuota_por_hora
    print(f"El importe de M.O.D es: {importe_mano_obra_directa}")

    # Producto A SEGUNDO SEMESTRE
    print("PRODUCTO A SEGUNDO SEMESTRE")
    unidades_p2 = int(input("Unidades a producir: "))
    horas_por_unidad2 = int(input("Horas requeridas por unidad: "))
    total_horas_req2 = (unidades_p2 * horas_por_unidad2)
    print(F"Total de horas requeridas: {total_horas_req2}")
    cuota_por_hora2 = float(input("Cuota por hora: "))
    importe_mano_obra_directa2 = total_horas_req2 * cuota_por_hora2
    print("El importe de M.O.D es: ", importe_mano_obra_directa2)

    # Producto A TOTAL
    unidades_totales = (unidades_p1 + unidades_p2)
    print(f"Total de unidades a producir: {unidades_totales}")
    Total_horas_unidad = (horas_por_unidad + horas_por_unidad2)
    print(f"Total de horas requeridas por unidad: {Total_horas_unidad}")
    Total_horas_req = (unidades_totales * Total_horas_unidad)
    print(f"Total de horas requeridas: {Total_horas_req}")
    Total_importemano_obra_directa = (importe_mano_obra_directa + importe_mano_obra_directa2)
    print(f"Total del importe de M.O.D: {Total_importemano_obra_directa}")
    separador()
    input("Pulse Enter para continuar...")

    
    

    LimpiarPantalla()
    separador()
    print("\tTOTAL PRESUPUESTO")
    print(f"Unidades a producir: {unidades_totales} ")
    print(f"Horas Requeridas por Unidad: {Total_horas_req}")
    total_horas_reqSum = Total_horas_req
    print(f"Horas Requeridas: {Total_horas_req}")
    print(f"Importe M.O.D: {Total_importemano_obra_directa}")

    print("\tHORAS REQUERIDAS")
    print(f"Primer semestre: {total_horas_req1}")
    print(f"Segundo semestre: {total_horas_req2}")
    print(f"Total Anual: {Total_horas_req}")

    print("\tTOTAL M.O.D")
    print(f"El total de M.O.D por el primer semestre es de: {importe_mano_obra_directa}")
    print(f"El total de M.O.D por el segundo semestre es de: {importe_mano_obra_directa2} ")
    print(f"El total de M.O.D por semestre es de: {Total_importemano_obra_directa}")
    separador()
    input("Presione Enter para continuar...")

def gastosIndirectosFabricacion():
    LimpiarPantalla()
    global total_GIF
    print("\tGASTOS INDIRECTOS DE FABRICACION")
    separador()
    print("PRIMER SEMESTRE")
    seguros_s1 = int(input("Seguros: "))
    depreciacion_s1 = int(input("Depreciacion: "))
    energeticos_s1 = int(input("Energeticos: "))
    mantenimiento_s1 = int(input("Mantenimiento: "))
    varios_s1 = int(input("Varios: "))
    totalGIF_s1 = (depreciacion_s1 + seguros_s1 + mantenimiento_s1 + energeticos_s1 + varios_s1)
    print(f"G.I.F Total Primer Semestre: {totalGIF_s1}")
    print('')

    print("SEGUNDO SEMESTRE")
    seguros_s2= int(input("Seguros: "))
    depreciacion_s2= int(input("Depreciacion: "))
    energeticos_s2= int(input("Energeticos: "))
    mantenimiento_s2= int(input("Mantenimiento: "))
    varios_s2= int(input("Varios: "))
    totalGIF_s2= (depreciacion_s2 + seguros_s2 + mantenimiento_s2 + energeticos_s2 + varios_s2)
    print(f"G.I.F Total Primer Semestre: {totalGIF_s2}")

    LimpiarPantalla()
    total_depreciacion = (depreciacion_s1 + depreciacion_s2)
    print(f"Total Depreciacion: {total_depreciacion}")

    total_seguros = (seguros_s1 + seguros_s2)
    print(f"Total Seguros: {total_seguros}")

    total_mantenimiento = (mantenimiento_s1 + mantenimiento_s2)
    print(f"Total Mantenimiento: {total_mantenimiento}")

    total_energeticos = (energeticos_s1 + energeticos_s2)
    print(f"Total Energeticos: {total_energeticos}")

    total_varios = (varios_s1 + varios_s2)
    print(f"Total Varios: {total_varios}")

    total_GIF = (total_depreciacion + total_seguros + total_mantenimiento + total_energeticos + total_varios)
    print(f"Total G.I.F: {total_GIF}")
    input("Presione Enter para continuar...")

    LimpiarPantalla()
    print("\tCOSTO POR HORA GASTOS INDIRECTOS")
    print(f"Total de G.I.F: {total_GIF}")
    print(f"El total de horas M.O.D anual es de: {total_horas_reqSum}")
    total_GIF = (total_GIF / total_horas_reqSum)
    print(f"El costo por hora de G.I.F es de: {total_GIF}")
    separador()
    input("Presione Enter para continuar...")

def PresupuestoGastosOp():
    LimpiarPantalla()
    print("\tGASTOS DE OPERACION")

    # GO Primer Semestre
    print("PRIMER SEMESTRE")
    depreciacion_s1 = int(input("Depreciacion : "))
    salarios_s1 = int(input("Salarios: "))
    comisiones_s1 = int(input("Comisiones: "))
    varios_s1 = int(input("Varios: "))
    intereses_s1 = int(input("Intereses por prestamo: "))
    print(f"Total: {depreciacion_s1 + salarios_s1 + comisiones_s1 + varios_s1 + intereses_s1}")

    # GO Segundo Semestre
    print("SEGUNDO SEMESTRE")
    depreciacion_s2 = int(input("Depreciacion : "))
    salarios_s2 = int(input("Salarios: "))
    comisiones_s2 = int(input("Comisiones: "))
    varios_s2 = int(input("Varios: "))
    intereses_s2 = int(input("Intereses por prestamo: "))
    print(f"Total: {depreciacion_s2 + salarios_s2 + comisiones_s2 + varios_s2 + intereses_s2}")
    input("Presione Enter para continuar...")


    # GO TOTAL
    print("\tTOTAL")
    print(f"Total Depreciacion: {depreciacion_s1 + depreciacion_s2}")
    print(f"Sueldos y Salarios: {salarios_s1 + salarios_s2}")
    print(f"Comisiones: {comisiones_s1 + comisiones_s2}")
    print(f"Varios: {varios_s1 + varios_s2}")
    print(f"Intereses por Préstamo: {intereses_s1 + intereses_s2}")
    print(f"Total de Gastos de Operación: {depreciacion_s1+ salarios_s1 +comisiones_s1+ varios_s1 + intereses_s1 + depreciacion_s2 + salarios_s2 + comisiones_s2 + varios_s2 + intereses_s2}")
    separador()
    input("Presione Enter para continuar...")

def costoUnitario():
    LimpiarPantalla()
    print("\tCOSTO UNITARIO PRODUCTO TERMINADO")
    
    # Producto A
    print("PRODUCTO A")
    print("Material A")
    costo_a = float(input("Costo: "))
    cantidad_a = int(input("Cantidad: "))
    costo_unitario = costo_a * cantidad_a 
    print(f"El Costo Unitario es: {costo_unitario}")

    print("Material B")
    costo_b = float(input("Costo: "))
    cantidad_b = int(input("Cantidad: "))
    costo_unitario_b = costo_b * cantidad_b 
    print(f"El Costo Unitario es: {costo_unitario_b}")

    print("Material C")
    costo_c = float(input("Costo: "))
    cantidad_c = int(input("Cantidad: "))
    costo_unitario_c = costo_c * cantidad_c 
    print(f"El Costo Unitario es: {costo_unitario_c}",)

    print("Mano de Obra")
    costo_mano = float(input("Costo"))
    cant_mano = int(input("Cantidad"))
    costo_unitario_mano = costo_mano * cant_mano 
    print(f"El Costo Unitario es: {costo_unitario_mano}")

    print("Gastos Indirectos de Fabricacion")
    costo_gastos_fab = float(input("Costo: "))
    print("Cantidad: ")
    cant_gastos = int(input())
    costo_unitario_fab = costo_gastos_fab * cant_gastos 
    print(f"Costo Unitario: {costo_unitario_fab}")

    print(f"Costo Unitario Total: ${costo_unitario+costo_unitario_b+costo_unitario_c+costo_unitario_mano+costo_unitario_fab}")
    separador()
    input("Presione Enter para continuar...")

def InventariosFinales():
    print("\tINVENTARIOS FINALES")
    print("Inventario Final de Materiales")
    print('PRIMER SEMESTRE')
    print('Material A: $112,000')
    print('Material B: $155,000')
    print('Material C: $100,000')
    print('         ')
    print('Total de costos unitarios: $367,000')
    print('         ')
    print('         ')
    print('SEGUNDO SEMESTRE')
    print('Material A: $140,000')
    print('Material B: $197,000')
    print('Material C: $127,500')
    print('         ')
    print('Total de costos unitarios: $464,500')
    print('         ')
    print('TOTAL: $831,500')


def EstadoCostoProduccionVenta():
    print("\tESTADO DE COSTOS DE PRODUCCION Y VENTA")
    saldo_inicial = int(input("Saldo Inicial de Materiales: "))
    compras_materiales = int(input("Compras de Materiales: "))
    material_disponible = compras_materiales + saldo_inicial
    print(f"Material Disponible: {material_disponible}")

    inventario_final_m = int(input("Inventario Final de Materiales: "))
    materiales_utilizados = material_disponible - inventario_final_m
    print(f"Materiales Utilizados: {materiales_utilizados}")
    mano_obra_directa = int(input("Mano de Obra Directa: "))
    gastos_fab_indirectos = int(input("Gastos de Fabricación Indirectos: "))
    print(f"Costo de Producción: {materiales_utilizados + mano_obra_directa + gastos_fab_indirectos}")
    inventario_inicial = int(input("Inventario Inicial de Productos Terminados: "))
    total_productos = materiales_utilizados + mano_obra_directa + gastos_fab_indirectos + inventario_inicial
    print(f"Total de Producción Disponible: {total_productos}")
    inventario_final = int(input(f"Inventario Final de Productos Terminados: "))
    print(f"Costo de Ventas: {total_productos-inventario_final}")
    separador()
    input("Presione Enter para continuar...")

def EstadoResultados():
    LimpiarPantalla()
    print("\tESTADO DE RESULTADOS")
    separador()
    VER1 = int(input("Ventas: " ))
    CDV1 = int(input("Costo de Ventas: "))
    UtilidadBruta = VER1-CDV1
    print(f"Utilidad Total Bruta: {UtilidadBruta}")
    GastosO = int(input("Gastos de operacion: "))
    UtilidadO= (UtilidadBruta-GastosO)
    print (f"Total de Utilidad de operacion: {UtilidadO}")
    ISR1 = int(input("ISR: "))
    PTcant_A = int(input("PTU: "))
    UtilidadN = (UtilidadO-ISR1-PTcant_A)
    print (f"Utilidad Neta: {UtilidadN}")
    separador()
    input("Presione Enter para continuar...")

def EstadoFlujoEfectivo():
    LimpiarPantalla()
    print("\tESTADO FLUJO EFECTIVO")
    separador()
    print("---Entradas---")
    cobranza_1 = int(input("Cobranza No.1: "))
    cobranza_2 = int(input("Cobranza No.2: "))
    print(f"Total Entradas: {cobranza_1 + cobranza_2}")
    separador()
    print('---Salidas---')
    proveedor_1 = int(input("Proveedores No.1: "))
    proveedor_2 = int(input("Proveedores No.2: "))
    Pmano_obra_directa= int(input("Pago de Mano de Obra Directa: "))

    gastos_in = int(input("Gastos Indirectos de Fabricación: "))
    gastos_op = int(input("Gastos de Operación: "))
    compra_a = int(input("Compra de Activo Fijo (Maquinaria): "))
    ISR1 = int(input("Pago ISR No.1: "))
    ISR2 = int(input("Pago ISR No.2: "))
    print(f"Total de Salidas: {proveedor_1 + proveedor_2 + Pmano_obra_directa + gastos_in + gastos_op + compra_a + ISR1 + ISR2}")
    separador()
    input("Presione Enter para continuar...")

def BalanceGeneral():
    LimpiarPantalla()
    separador()
    print("\tEMPRESA, S.A. de C.V.")
    print("\tBalance General")
    separador()
    print("---ACTIVOS CIRCULANTES---")
    efectivo_a = int(input("Efectivo: "))
    clientes = int(input("Clientes: "))
    deudores = int(input("Deudores Diversos: "))
    empleados = int(input("Empleados: "))
    inventario_m = int(input("Inventario de Materiales"))
    inventario_producto = int(input("Inventario de Producto Terminado"))
    activo_circulante = efectivo_a + clientes + deudores + empleados + inventario_m + inventario_producto
    print(f"Total ACTIVOS CIRCULANTES: ${activo_circulante}")
    separador()

    print("---ACTIVOS NO CIRCULANTES---")
    terreno = int(input("Terreno: "))
    equipo = int(input("Planta y equipo: "))
    depreciacion = int(input("Depreciación: "))
    activo_no_circulante = terreno + equipo + depreciacion
    print(f"Total ACTIVOS NO CIRCULANTES: ${activo_no_circulante}")
    separador()

    print(f"Total ACTIVOS: {activo_circulante + activo_no_circulante}")

    print("\n---PASIVO CORTO PLAZO---")
    proveedores = int(input("Proveedores: "))
    documentos = int(input("Documentos por Pagar: "))
    ISR = int(input("ISR por Pagar: "))
    PTU = int(input("PTU por pagar: "))
    pasivo_corto_plazo = proveedores + documentos + ISR + PTU
    print(f"Total de PASIVO CORTO PLAZO: ${pasivo_corto_plazo}")
    separador()

    print("---PASIVO LARGO PLAZO---")
    prestamos_bancarios = int(input("Préstamos Bancarios: "))
    print(f"Total de Pasivo a Largo Plazo: ${prestamos_bancarios}")
    pasivo_total = pasivo_corto_plazo + prestamos_bancarios
    print(f"Pasivo Total: {pasivo_total}")
    separador()
    
    print("\n---CAPITAL CONTABLE---")
    cap_aportado = int(input("Capital Aportado"))
    cap_ganado = int(input("Capital Ganado"))
    utilidad = int(input("Utilidad del Ejercicio"))
    total_capital = cap_aportado + cap_ganado + utilidad
    print(f"Total de Capital Contable: ${total_capital}")

    print("\n---PASIVO Y CAPITAl---")
    print(total_capital + pasivo_total)
    separador()
    input("Presione Enter para continuar...")

def main():
    print(f"\tPresupuesto Maestro")
    separador()
    productosABC()
    SaldoFlujo()
    PresupuestoProduccion()
    PresupuestoReqMateriales()
    PresupuestoCompraMateriales()
    SaldoProvFlujo()
    manoObraDirecta()
    gastosIndirectosFabricacion()
    PresupuestoGastosOp()
    costoUnitario()
    InventariosFinales()
    EstadoCostoProduccionVenta()
    EstadoResultados()
    EstadoFlujoEfectivo()
    BalanceGeneral()
#endregion

main()