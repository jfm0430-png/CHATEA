# Notas ChateaPro / DROPI

- API: `https://chateapro.app/api`. El token está guardado como secreto del entorno (no se escribe aquí).
- Límite de la API: ~1000 consultas por ventana. Los flujos de la cuenta comparten ese límite.
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
