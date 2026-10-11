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
