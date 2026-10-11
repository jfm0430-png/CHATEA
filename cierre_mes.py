"""Cierre mensual a partir del historial de cartera de DROPI.

Uso:
    python3 cierre_mes.py DESDE HASTA archivo1.xlsx [archivo2.xlsx ...]

DESDE y HASTA son los números de orden que delimitan el mes del pedido
(primer pedido del mes y primer pedido del mes siguiente). Ejemplo septiembre 2026:
    python3 cierre_mes.py 87906119 91500000 cartera_sep.xlsx cartera_oct.xlsx
"""
import collections
import re
import sys

import openpyxl

GANANCIA = "ENTRADA POR GANANCIA EN LA ORDEN COMO DROPSHIPPER"
DEVOLUCIONES = (
    "SALIDA POR COBRO DE FLETE INICIAL",
    "SALIDA DE COBRO DE DEVOLUCIÓN POR ENTREGA NO EFECTIVA",
)
PERSONAS = ("HAROLD", "ANA MARIA", "DANIEL", "OSCAR")


def leer(archivos):
    filas = {}
    for f in archivos:
        hoja = openpyxl.load_workbook(f, read_only=True).worksheets[0]
        for r in list(hoja.iter_rows(values_only=True))[1:]:
            if r[0]:
                filas[r[0]] = r  # el ID evita contar dos veces un movimiento
    return list(filas.values())


def nombre(desc):
    d = (desc or "").split(":")[0]
    d = re.sub(r"car_\w+|BALANCEHISTORY ID.*|ID_GARANTIA.*|\bID\b.*", "", d)
    return re.sub(r"\s+", " ", d).strip(" -.")


def main():
    desde, hasta, *archivos = sys.argv[1:]
    desde, hasta = int(desde), int(hasta)
    filas = leer(archivos)
    del_mes = lambda r: r[5] and desde <= int(r[5]) < hasta

    tot = collections.defaultdict(lambda: [0, 0.0])
    for r in filas:
        desc = r[7] or ""
        for clave in (GANANCIA,) + DEVOLUCIONES:
            if desc.startswith(clave) and del_mes(r):
                tot[clave][0] += 1
                tot[clave][1] += float(r[3])

    gan = tot[GANANCIA][1]
    dev = sum(tot[c][1] for c in DEVOLUCIONES)
    print("== Pedidos del mes ==")
    print(f"Ganancia entregadas: {tot[GANANCIA][0]} ordenes  ${gan:,.0f}")
    for c in DEVOLUCIONES:
        print(f"{c}: {tot[c][0]}  -${tot[c][1]:,.0f}")
    print(f"NETO: ${gan - dev:,.0f}")

    print("\n== Todos los movimientos por nombre (fecha del movimiento) ==")
    grupos = collections.defaultdict(lambda: [0, 0.0])
    personas = collections.defaultdict(lambda: [0, 0.0])
    for r in filas:
        grupos[(r[2], nombre(r[7]))][0] += 1
        grupos[(r[2], nombre(r[7]))][1] += float(r[3] or 0)
        if "RETIRO DE SALDO" in (r[7] or ""):
            c = (r[9] or "").upper()
            p = next((x for x in PERSONAS if x in c), "SIN CONCEPTO")
            personas[p][0] += 1
            personas[p][1] += float(r[3])
    for (tipo, n), (k, v) in sorted(grupos.items(), key=lambda x: (x[0][0], -x[1][1])):
        print(f"{tipo:8} {k:5}  ${v:>14,.0f}  {n}")
    print("\n== Retiros por persona ==")
    for p, (k, v) in sorted(personas.items(), key=lambda x: -x[1][1]):
        print(f"{p:14} {k:3}  ${v:,.0f}")


if __name__ == "__main__":
    main()
