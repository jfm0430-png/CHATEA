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
