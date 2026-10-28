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
| 17 oct 2026, 10:12 p. m. (cierre) | 4.753 | 1.419 |
| 18 oct 2026, 10:12 p. m. (cierre) | 4.756 | 1.618 |
| 19 oct 2026, 10:12 p. m. (cierre) | 4.758 | 1.808 |
| 20 oct 2026, 10:12 p. m. (cierre) | 4.761 | 1.978 |
| 21 oct 2026, 10:12 p. m. (cierre) | 4.764 | 2.163 |
| 22 oct 2026, 10:12 p. m. (cierre) | 4.765 | 2.352 |
| 23 oct 2026, 10:12 p. m. (cierre) | 4.765 | 2.571 |
| 24 oct 2026, 10:12 p. m. (cierre) | 4.765 | 2.721 |
| 25 oct 2026, 10:13 p. m. (cierre) | 4.765 | 2.733 |
| 26 oct 2026, 10:12 p. m. (cierre) | 4.766 | 2.922 |

Método: `list_orders` con `status=ENTREGADO`, rango del mes, y búsqueda por `start` con
`result_number=1` hasta encontrar el final. Entregadas en el día = conteo de las 10 p. m. − base.
Desde el 27 oct (pedido de Johana): cada reporte diario incluye también cuántas se entregaron el día anterior (última fila de cierre − penúltima) para comparar.

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
- ~9 a. m. (corre 8:48) SOLO MIÉRCOLES (pedido de Johana 19 oct): pedidos para salvar = solo Interrapidísimo en RECLAME EN OFICINA, 6+ días
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
- 16 oct (primer día tras apagar): gasto Meta $2.954.770 (antes $3.829.222), 168 compras Meta, 184 ventas reales,
  costo real $15.816 (antes $18.929). Relanzados: Combo Baño $15.540 (8), Organizador Baño $8.157 (8), 2 Tapas oct 15 $15.131 (13).
- Regla para revisar conjuntos (aprendida 17 oct): mirar ÚLTIMOS 7 DÍAS (no solo el mes) y cruzar con ventas reales
  de ChateaPro ("Ventas por anuncio"; el ID de anuncio ≈ ID de conjunto ±10). Meta ve casi todas las ventas en conjuntos
  de "compras" pero pocas en los de "conversaciones" (VIDEO 1 ZAPATERO: Meta 11, reales 21). Johana: 1 anuncio por conjunto.
- 17 oct, relanzamientos (interacción + maximizar compras, 1 conjunto, sin animación/retoques/multianunciante):
  ZAPATERO AMM AGOSTO 3 ($50k), VIDEO AMM JULIO 21 ESC 3 NIVELES ($50k), MEGACOMBO VIDEO 1 AMMM SEPT 15 ($40k).
  Revisar el martes 21 oct. Regla: copia nunca con más presupuesto que el original; si el original sube >15 %, bajar la copia.
  Pendiente lunes: +20 % a IMÁGENES 2.0 OCT 9 (Megacombo), AGOSTO 3, SEPT 24; apagar NUEVO VOZ VIRAL, 3 NIVELES VIDEO VIEJO,
  MEGACOMBO IMAGENES (viejo).

## Relanzamiento Perchero (17 oct 2026)
- Johana relanzó TODA la campaña del Perchero (la anterior estaba muy mala). Seguimiento diario por 7 días (17 al 23 oct).
- Datos que ella envía cada noche: CSV de conjuntos de Meta (gasto, compras, costo por compra) + pantallazo de ChateaPro "Ventas por anuncio" del día. No consultar ChateaPro.
- Reglas: días 1 a 3 no tocar, salvo un conjunto con ~$100k gastados y 0 o 1 ventas reales. Día 4: CPA real menor a $20k se deja; entre $20k y $28k se deja y se vigila; mayor a $30k con más de $150k gastados se apaga. Día 7: decisión final y +20% a los que estén por debajo de $20k.
- Referencias de la campaña anterior (mes): VIDEO 4 MUJER $18.840; VIDEO 1 HOMBRE copia $28.181; VIDEO 5 PERCHERO $32.043. Mejor conjunto de Perchero en general: PERCHERO AMMM SEPT 19 ($10.430, en otra campaña). Si su CPA sube más del 15% por 2 días, bajar o apagar el conjunto equivalente de la campaña nueva.
- 17 oct (sábado), Meta: gasto $3.254.630, 177 compras, CPA $18.388 (16 oct: $2.954.770, 168 compras, $17.588). Escalados día 1: Zapatero $38.862 con 3 compras ($12.954); 3 Niveles $40.065 con 2 ($20.032); Megacombo $30.901 con 1. Originales: Zapatero Cubierta Video 1 bajó de 11 a 6 compras ($25.932); Esc 3N Mayo 30 bajó de 18 a 12 ($20.840); Megacombo Agost 3 subió de 9 a 15 ($12.866). Perchero relanzado: $76.149 con 1 compra. Regla: si el 18 oct el original + su copia juntos siguen peor que el original solo del 16 (Zapatero $13.101, Esc 3N $13.520), apagar la copia.
- 17 oct ChateaPro Perchero: 8 ventas reales; 0 de la campaña relanzada ($76.149 gastados). AGOST 7 SSS 4, SEPT 19 1, AGOST 6 AMMM VIDEO 2 1. PERCHERO Z. AGOSTO 6 ≈ 6 reales ($15.500). Plan: domingo al mediodía, si la relanzada sigue en 0 ventas, apagarla completa. Lunes: +20% a AGOST 7 SSS si sigue bien.
- 18 oct, Set x9 piezas cocina ($169.900; en DROPI probablemente "Set de ollas de Acero inoxidable con man"): septiembre ganancia ~$32.900 por entregado, 25,7% de devolución, ~$18.500 netos por despachado. Semana 11 a 17 oct: Meta $497.107, 18 compras ($27.617); 14 pedidos reales, que dejan ~$260k → pierde ~$237k. Recomendado: apagar IMÁGENES SET COMPLETO X9 MAYO 8 y bajar VIDEO 1 AGOSTO 24 de $30k a $15k; apagar si en 3 días sigue por encima de $18k. Regla nueva: calcular el CPA máximo por producto con su ganancia y devolución reales, no con el promedio de $38.000.
- Corrección: el Set x9 es BATERIA ELEGANZA (producto DROPI 2086235). Septiembre: 99 pedidos, 9 cancelados, 69 entregados, 15 devueltos, 6 en oficina. Ganancia ~$32.290 por entregado, flete ~$27.900, efectividad 82%, ~$21.500 netos por despachado. Con publicidad de $2.017.853, septiembre quedó en ~−$75k. Video Agosto 24 a $16.018 deja ganancia; Imágenes Mayo 8 a $26.517 pierde. CPA máximo del producto: $21.500.
- 18 oct: tabla "CPA máximo por producto" (scratchpad cpa_maximo_por_producto.xlsx), hecha con el reporte de septiembre. Máximo = (ganancia de entregas − fletes de devolución) / (entregados + devueltos). Algunos máximos: Zapatero 6N cubierta $27.344; Zapatero 5N con perchero $30.051; PortaComida X4 $29.276; Org. cocina con tapa $37.515; Escurridor 3 niveles Gabinete $31.585; Escurridor platos 3 niveles $18.329; Bolso morral $21.532; Dispensador crema dental $24.141; Eleganza $21.637; Juego ollas 10 + tetera $14.192; Termo 500 ml $12.932; Ollas 13 pz $10.900. Objetivo = máximo − $4.200 (gastos fijos).
- Cobro por devolución, según la billetera de septiembre: Interrapidísimo cobra "FLETE INICIAL" completo (~$25.700 en promedio). Envía (~$14.000) y Coordinadora (~$13.900) cobran "DEVOLUCIÓN POR ENTREGA NO EFECTIVA", más barato. Para calcular por producto usar el cobro real de la billetera por orden; si falta, flete × factor de la transportadora medido por orden (Inter 1,00 exacto; Envía 0,74; Coordinadora 0,59; JAMV 0,79; Veloces 0,77; Derocha 0,92). La tabla de CPA máximo ya está recalculada así (los cambios fueron pequeños).
- Productos: COMBO BAÑO = 'Combo Organizador Baño Mas Esquinero' ($129.900). MEGACOMBO HOGAR X3 = 'Combo baño + Escurridor Doble' ($219.900). Escurridor 3 niveles = 'Escurridor platos 3 niveles' + 'Platero Mesa de 3 Niveles'. Gabinete escurridor = 'Escurridor 3 niveles Gabinete' + 'Escurridor cajon 2 niveles con cajon'. Set x9 = BATERIA ELEGANZA.
- 19 oct: balance de septiembre por producto (scratchpad balance_septiembre_por_producto.xlsx; mapeo en bal/mapeo.txt). Ganancia de pedidos $168,9M − Meta $142,4M = $26,4M − fijos $22,7M ≈ utilidad $3,7M. Ganan: Combo cocina +$5,6M, Zapatero 6N +$3,5M, Bolso +$3,4M, Megacombo +$3,0M, Gabinete +$2,4M, Combo lonchera+termo +$2,0M, Zapatero 9N +$1,8M. Pierden: Ollas 13 −$5,7M (ya apagada), Escurridor 1 tapa −$3,1M, Armario tela −$1,7M, Drenaje −$1,3M, Dispensador −$1,2M, Lonchera eléctrica −$1,1M, Set x6, Tetera, Ollas blancas (~−$0,6M c/u). 724 pedidos ($22M) no tienen campaña directa (combos de dispensador y esquinero, escurridor 85 cm, rack negro, org. cocina con tapa).
- Equivalencias (Johana, 19 oct): Escurridor loza 85 cm → Escurridor 2 niveles/2 tapas; Escurridor rack negro 2 niveles → Drenaje; Organizador cocina con tapa → Organizador cocina ruedas (corregido 19 oct); Armario 88130 → Armario tela. Escurridor 2 tapas = Doble Accesorios Negro + Doble Tapa 65 cm + Dos Niveles Más Tapón. Superbaño = combos dispensador + esquinero. Organizador baño = Estante 3 niveles + Estante blanco. Ruedas org cocina = Organizador cocina multifuncional. Alacena = Gabinete 80 cm (ya no se maneja). Combo lonchera + termo = Lonchera 2 niveles + Termo 500.
- Balance corregido de septiembre (balance_septiembre_completo.xlsx): con lo ya cerrado, utilidad $379k; estimada al cerrar todo, ~$3,7M. Drenaje pasa a +$1,0M; Escurridor 2 tapas a +$3,0M; Escurridor 1 tapa a −$1,1M; Armario a −$0,7M.
- Combos de armario (Armario106 + Perchero, Armario106 + Zapatero 6N, Zapatero 6N + Armario 88130) → Armario tela. Con eso el Armario queda en +$1,6M en septiembre (174 pedidos, $21.265 de publicidad por pedido).
- Agosto 2026 (solo DROPI, estados al 18 oct): 7.130 pedidos, 239 cancelados, 5.395 entregados, 1.485 devueltos, efectividad 78%. Ganancia de entregas $209.073.803; devoluciones −$28.076.962 (639 exactas); neto $180.996.841. Septiembre: neto $165,5M (+$3,3M en proceso), efectividad 81%. Excel en scratchpad agosto_dropi.xlsx.
- Corrección 19 oct: 'Organizador de cocina con tapa' es el de RUEDAS (no el escurridor 1 tapa). Septiembre: Org. cocina ruedas +$1,6M (93 pedidos, $18.858 de publicidad por pedido); Escurridor 1 tapa −$3,1M ($45.941 por pedido, aguanta $25.355).
- Regla de escalado (19 oct): en la cuenta de Johana, duplicar el mismo anuncio en otra campaña NO suma ventas; las cambia de campaña y sube el costo (Perrito: de $13.400 a $25.300 por compra; escalados del 17 oct). Escalar así: (1) el mismo anuncio, solo subiendo presupuesto +20% cada 2-3 días mientras el CPA real esté bajo el máximo del producto; (2) creativos nuevos en conjuntos nuevos de $20-30k; (3) productos, combos u ofertas nuevas. Nunca el mismo anuncio prendido en dos campañas.
- 22 oct: conjuntos de Meta del 15 al 21 oct: gasto $25.450.963, 1.345 compras Meta, CPA $18.922 (semana 9-15 oct: $27.623.338, 1.140, $24.231). −8% de gasto, +18% de compras, −22% de CPA después de apagar conjuntos. Decisiones en scratchpad decisiones_conjuntos_15-21oct.xlsx (29 para subir 20%, 7 para apagar, 13 para bajar, 16 sin producto identificado: VIDEO AMM SEPT 26/SEPT 19/OCT 4, IMAGENES WIN, VIDEO 1/2/3/6 genéricos, etc.).
- 22 oct, Megacombo: IMÁGENES viejo (sept $19.432, ahora $43.747) y VIDEO 1 SSS (sept $15.182, ahora $82.852) se cayeron desde que salieron IMÁGENES 2.0 OCT 9 y AMMM OCT 8. Plan: pausar IMÁGENES viejo. Probar SSS a maximizar compras con $15.000/día por 4 días, vigilando AMMM SEPT 15 (mismo video): si su CPA sube >15% dos días, apagar SSS. Si SSS queda por debajo de $20.000, Johana relanza las imágenes viejas también a compras.
- Campañas 16-22 oct: gasto $24.192.533, 1.319 compras Meta, CPA $18.342. Mejores: Armario tela $9.249, Porta térmica X3 $9.132, Bolso expandible $13.093, 2 Tapas relanzada OCT 11 $15.501, Zapatero cubierta $14.611, Escurridor 3N $14.163, Megacombo $17.987, Gabinete $18.180, Ruedas $18.331. Perdiendo: Combo lonchera + termo $63.729, Superbaño $34.720. Justos: Lunch Box $28.129, Lonchera eléctrica $26.976, Escurridor tapa viral Agosto 9 $24.790, Dispensador Abril 16 $22.103. Combo baño relanzada OCT 16 va bien ($20.772); los conjuntos "rojos" de combo baño eran viejos. Lanzó CLOSET 4 PUESTOS OCT 22.
- 22 oct, optimización (campañas 16-22 oct, CPA en Meta): campañas de compras $17.185 (364 compras); de conversaciones $23.294 (301); mixtas (conjuntos AMM de compras + viejos de conversaciones) $16.146 (654). Regla nueva: lo nuevo y lo relanzado, a maximizar compras. No cambiar la optimización de ganadores de conversaciones que siguen vendiendo en ChateaPro (9 Niveles, Esc 3N SEPT 12, Dispensador Mayo 5).
- Nómina (Johana, 24 oct), de lunes a sábado: Harold $120.000/día; Danna $110.000; Valeria, Ana y Camilo $100.000; Camilo además los domingos a $120.000. Más horas extras a veces. Octubre (27 días L-S + 4 domingos) ≈ $14.790.000. En la billetera de septiembre también aparecen pagos a Daniel ($3,28M) y Oscar ($1,62M): pendiente confirmar si siguen. Pendiente: valor de ChateaPro.
- Gastos fijos actualizados (Johana, 24 oct): nómina fija $14.790.000 (octubre, L-S) + Daniel y Oscar $3.000.000 + ChateaPro $1.400.000 + OpenAI $2.000.000 + LLC $700.000 = $21.890.000 al mes (≈$730.000/día) + horas extras. Usar esto en el cierre de octubre (antes se usaba $22.700.000).
