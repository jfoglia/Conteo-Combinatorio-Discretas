# Casos de prueba - Permutaciones P(n,r)

## Prueba 1

Entrada:

n = 10
r = 3

Cálculo:

P(10,3) = 10! / 7!

Resultado esperado:

720

Resultado obtenido:

720

---

## Prueba 2

Entrada:

n = 20
r = 5

Cálculo:

P(20,5) = 20! / 15!

Resultado esperado:

1860480

Resultado obtenido:

1860480

---

## Prueba 3

Entrada:

n = 5
r = 5

Cálculo:

P(5,5) = 5! / 0!

Resultado esperado:

120

Resultado obtenido:

120

---

## Prueba 4

Entrada:

n = 20
r = 0

Cálculo:

P(20,0) = 20! / 20!

Resultado esperado:

1

Resultado obtenido:

1

---

## Prueba 5

Entrada:

n = 0
r = 0

Cálculo:

P(0,0) = 0! / 0!

Resultado esperado:

1

Resultado obtenido:

1

---

## Prueba 6 (Caso inválido)

Entrada:

n = -5
r = 3

Resultado esperado:

Mensaje de error indicando que n no puede ser negativo.

Resultado obtenido:

Entrada rechazada correctamente.

---

## Prueba 7 (Caso inválido)

Entrada:

n = 3
r = 5

Resultado esperado:

Mensaje de error indicando que r no puede ser mayor que n.

Resultado obtenido:

Entrada rechazada correctamente.

