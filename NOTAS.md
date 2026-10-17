# Notas ChateaPro / DROPI

- API: `https://chateapro.app/api`. El token está guardado como secreto del entorno (no se escribe aquí).
- Límite de la API: ~1000 consultas por ventana. Los flujos de la cuenta comparten ese límite.
- **15 oct 2026: Johana pidió NO consultar ChateaPro (ni de noche) hasta que ella diga. Ella envía los flujos por el chat.**
  Hacer consultas despacio y por partes (máx. ~100 seguidas con pausa) y parar ante un 429.

## Búsqueda pendiente: clientes interesados en otro producto

ChateaPro es mono producto: el chat queda con el flujo del primer producto y no puede enviar otro.
Buscar clientes que pueden comprar un producto nuevo:

- Chats con estado **abierto** y último mensaje del cliente **del mismo día**.
- Que **tengan flujo de producto** (`[WhatsApp IA] Nombre del producto`).
- **Sin pedido**: sin `ID de Dropi`, `[Logistica] Order ID`, `Fecha de compra`, `Estado de la orden`,
  `[WhatsApp IA] Compra realizada` = true, ni etiquetas `Sincronizado con Dropi`, `SUBIR ORDEN`,
  `ORDEN SUBIDA POR CONFIRMAR`.
- Que pregunten por un producto **diferente** al de su flujo.

### Señal principal: el bot envió el catálogo

Cuando el cliente pregunta por otro producto, el bot le responde que revise el catálogo y envía
el enlace `https://wa.me/c/573169859773`. Buscar chats donde un mensaje saliente contenga
"catálogo" o `wa.me/c/`, y mirar qué preguntó el cliente justo antes.

## Conteo de entregas (DROPI, estado ENTREGADO, por mes de creación)

| Momento | Septiembre | Octubre |
|---|---|---|
| 10 oct 2026, ~9:05 a. m. (base) | 4.725 | 719 |
| 10 oct 2026, ~7:10 p. m. (parcial) | 4.731 | 843 |
| 10 oct 2026, 10:00 p. m. (cierre) | 4.732 | 845 |
| 11 oct 2026, 10:08 p. m. (cierre) | 4.732 | 853 |
| 12 oct 2026, 10:06 p. m. (cierre) | 4.732 | 865 |
| 13 oct 2026, 10:08 p. m. (cierre) | 4.735 | 1.020 |
| 14 oct 2026, ~10:30 p. m. (cierre; datos de Johana en DROPI por error 502) | 4.743 | 1.160 |
| 15 oct 2026, 10:08 p. m. (cierre) | 4.751 | 1.293 |
| 16 oct 2026, 10:08 p. m. (cierre) | 4.753 | 1.417 |

Método: `list_orders` con `status=ENTREGADO`, rango del mes, y búsqueda por `start` con
`result_number=1` hasta encontrar el final. Entregadas en el día = conteo de las 10 p. m. − base.

## Billetera DROPI: nombres de movimientos

Cobros por devolución (sumar todos como descuento por devoluciones):
- `SALIDA DE COBRO DE DEVOLUCIÓN POR ENTREGA NO EFECTIVA`
- `SALIDA POR COBRO DE FLETE INICIAL` (puede traer un número al final; no importa cuál)

Las variantes pueden traer el número de orden al final; agrupar por el texto antes de los dos puntos.

Abonos por entregas (sumar como ganancia de entregadas):
- `ENTRADA POR GANANCIA EN LA ORDEN COMO DROPSHIPPER`

Separar en categorías propias (no mezclar con entregas ni devoluciones):
- Descuentos por garantías
- Recargas a la Dropi Card
- Pagos por transferencia a personas (ej. Daniel, Harol, Oscar), uno por persona
- Cualquier otro movimiento: agrupar por su nombre y mostrarlo aparte

## Resultado septiembre 2026 (pedidos creados en septiembre, billetera sept + oct hasta 11 oct)

Mes del pedido por número de orden: septiembre = 87.906.119 a 91.500.000.

| Concepto | Órdenes | Valor |
|---|---|---|
| Ganancia por entregadas | 4.725 | $187.020.166 |
| Cobro flete inicial | 528 | −$13.201.236 |
| Cobro devolución entrega no efectiva | 411 | −$5.764.327 |
| Neto | | $168.054.603 |

## Cierre mensual (lo pide Johana cada mes)

1. Johana sube el historial de cartera del mes y del mes siguiente (Excel de DROPI).
2. Límites del mes por número de orden: primer pedido del mes y primer pedido del mes siguiente
   (sacarlos con `list_orders` del primer día, pocas consultas). Septiembre 2026: 87.906.119 a 91.500.000.
3. `python3 cierre_mes.py DESDE HASTA cartera_mes.xlsx cartera_mes_siguiente.xlsx`
4. Restar gastos que ella da: publicidad, nómina + ChateaPro, LLC, OpenAI.
5. Estado de los pedidos que siguen en proceso: consultar en DROPI solo los estados grandes
   (RECLAME EN OFICINA, NOVEDAD, EN REPARTO, EN TERMINAL DESTINO, NOVEDAD SOLUCIONADA), de a pocos.
   Cuidado: DROPI responde 429 si se hacen muchas consultas seguidas.

Septiembre 2026: gastos publicidad $142.500.000, nómina+ChateaPro $20.000.000, LLC $700.000,
OpenAI $2.000.000. Utilidad $2.854.603 (sin ~297 pedidos en proceso).

## Devoluciones por transportadora (pedidos de septiembre 2026, desde billetera)

Transportadora por prefijo de guía: 240=Interrapidísimo, 014/024/114=Envía, 9936/3639=Coordinadora,
WCO=Derocha/JAMV (Bogotá), V4=Veloces.

| Transportadora | Entregados | Devueltos | % dev | Neto | Neto por pedido | Cobro por devolución |
|---|---|---|---|---|---|---|
| Interrapidísimo | 2.251 | 501 | 18,2 % | $71.407.847 | $25.948 | $25.614 |
| Envía | 1.656 | 282 | 14,6 % | $65.852.266 | $33.979 | $14.057 |
| Coordinadora | 622 | 129 | 17,2 % | $22.349.602 | $29.760 | $13.956 |
| Derocha/JAMV | 159 | 24 | 13,1 % | $6.807.310 | $37.198 | $13.988 |
| Veloces | 37 | 3 | 7,5 % | $1.637.578 | $40.939 | $10.950 |

## Rutinas programadas
- 7:50 a. m. lunes y viernes: pedidos para salvar = solo Interrapidísimo en RECLAME EN OFICINA, 6+ días
  (grupos 6-8 y más de 8), Excel + push. NUNCA incluir otras transportadoras, NOVEDAD ni INTENTO DE ENTREGA.
- 8:00 a. m. lunes (corre 7:57): pedidos estancados (>10 días en tránsito), Excel + push.
- 10:00 p. m. diario: conteo de entregas.

## Publicidad Meta (octubre 2026)

- 1–14 oct: gasto $55.251.941 (~$3,95 M/día), 2.577 compras Meta, $21.440 por compra.
- Por tipo: conversaciones $24.533/compra; "varias conversiones" $17.944; interacción maximizando compras $19.477
  (atribución 7 días clic, más estricta). Johana prefiere interacción + maximizar compras para lanzar/relanzar.
- Umbrales: <$22.000 rentable; $22.000–28.000 justo; >$28.000 pierde (cada pedido deja ~$26–28 mil antes de publicidad).
- Escalar: vertical máx. +20 % cada 2–3 días; no tocar Escurridor 3 niveles ni Zapatero cubierta (las mejores).
- 15 oct: Johana relanzó 2 Tapas tráfico (campaña nueva) y apagó la vieja. Revisar con el CSV del lunes.
- 15–16 oct: Johana apagó 13 conjuntos caros (≈$303.000/día, ~6 ventas/día según Meta). Pendiente: 8 conjuntos
  al 50 % (Zapatero imágenes, Combo Cocina x2, Armario x2, Drenaje, Esc. tapa viral, Zapatero perchero imágenes)
  y 4 nuevos (VIDEO 2/3/4/5 del 10–11 oct) a revisar el domingo. Referencia: ~200 pedidos/día en ChateaPro.
