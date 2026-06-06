# Conteo Combinatorio - Matemáticas Discretas

## Autor

Julían Andrés Foglia Wilches

## Descripción

Este repositorio contiene la solución de dos problemas de conteo desarrollados para la asignatura de Matemáticas Discretas.

Los programas fueron implementados en diferentes lenguajes de programación y aplican principios fundamentales de la combinatoria como:

* Regla del producto.
* Permutaciones.
* Conteo con y sin repetición.
* Principio de complementación.
* Principio de inclusión-exclusión.

---

# Problema 1 - Permutaciones y k-Permutaciones (Java)

## 1. Descripción del problema

Se desea calcular el número de formas de ordenar r objetos distintos tomados de un conjunto de n objetos distintos.

El programa recibe dos enteros:

* n
* r

cumpliendo:

0 ≤ r ≤ n

y calcula:

P(n,r) = n! / (n-r)!

---

## 2. Principio combinatorio utilizado

### Permutaciones o k-Permutaciones

La cantidad de maneras de seleccionar y ordenar r elementos distintos tomados de un conjunto de n elementos distintos está dada por:

P(n,r) = n! / (n-r)!

---

## 3. Algoritmo

1. Solicitar los valores de n y r.
2. Validar que ambos sean no negativos.
3. Verificar que r ≤ n.
4. Calcular n!.
5. Calcular (n-r)!.
6. Aplicar la fórmula de permutaciones.
7. Mostrar el procedimiento y el resultado.
8. Comparar los resultados obtenidos mediante distintas implementaciones.

---

## 4. Código

Archivo principal:

problema2_java/src/main/java/org/example/Main.java

---

## 5. Casos de prueba

Ver archivo:

problema2_java/pruebas.md

---

## 6. Casos especiales validados

* n = 0 y r = 0.
* r = 0.
* r = n.
* Valores negativos.
* Casos donde r > n.

---

## 7. Eficiencia

### Factorial iterativo

Complejidad temporal:

O(n)

Complejidad espacial:

O(1)

### Factorial recursivo (extensión)

Complejidad temporal:

O(n)

Complejidad espacial:

O(n)

debido a la pila de llamadas recursivas.

---

# Problema 2 - Contador de Contraseñas (Python)

## 1. Descripción del problema

Se desea calcular la cantidad de contraseñas que pueden construirse bajo diferentes restricciones configurables por el usuario.

El programa permite definir:

* Longitud de la contraseña.
* Tamaño del alfabeto.
* Repetición permitida o no.
* Presencia obligatoria de dígitos.
* Presencia obligatoria de letras mayúsculas.
* Presencia obligatoria de símbolos especiales.

Adicionalmente se implementó una extensión que permite crear grupos personalizados de caracteres.

---

## 2. Principios combinatorios utilizados

### Regla del producto

Cuando se permite repetición:

|A|ⁿ

donde:

* |A| es el tamaño del alfabeto.
* n es la longitud de la contraseña.

### Permutaciones

Cuando no se permite repetición:

P(n,r) = n! / (n-r)!

### Principio de complementación

Para restricciones del tipo:

"Debe contener al menos un dígito"

se calcula:

Total − Contraseñas sin dígitos

### Principio de inclusión-exclusión

Cuando existen varias restricciones simultáneas.

---

## 3. Algoritmo

1. Leer los parámetros ingresados por el usuario.
2. Calcular el universo total de contraseñas.
3. Construir los conjuntos inválidos.
4. Aplicar inclusión-exclusión.
5. Obtener el número de contraseñas válidas.

---

## 4. Código

Archivo:

problema_2.py

---

## 5. Casos de prueba

Ver archivo:

problema1_python/pruebas.md

---

## 6. Casos especiales validados

* Longitud mayor que el tamaño del alfabeto sin repetición.
* Restricciones inconsistentes.
* Longitud insuficiente para cumplir todas las categorías obligatorias.
* Entradas inválidas.

---

## 7. Eficiencia

Si existen k restricciones, el algoritmo de inclusión-exclusión evalúa:

2ᵏ − 1

combinaciones.

En este problema:

k ≤ 3

por lo que el tiempo de ejecución es prácticamente constante.

---

# Instrucciones de ejecución

## Python

Ubicarse en la carpeta del proyecto y ejecutar:

python prueba_2.py

---

## Java

Compilar y ejecutar el proyecto Maven desde el IDE o mediante:

mvn compile

mvn exec:java

---

# Conclusiones

Los ejercicios permiten aplicar conceptos fundamentales de conteo combinatorio mediante implementaciones prácticas en Python y Java, validando distintos escenarios y casos especiales.
