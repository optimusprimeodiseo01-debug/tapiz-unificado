# Tapiz Unificado

Sistema basado en:

T(i,i) = prime(i)
H = log(T)
K = H - H^T
L = i*(H - H^T)

Incluye:
- Geometría discreta (triángulos)
- Construcción de tapiz
- Análisis espectral
- Deploy contrato (testnet-ready)
- Runner local

## Flujo

1. Generar T
2. Aplicar log → H
3. Obtener K y L
4. Calcular autovalores
5. Integrar geometría como input

## Ejecutar

```bash
pip install -r requirements.txt
python src/main.py
---

# 2) requirements.txt

```txt
numpy
sympy
web3
