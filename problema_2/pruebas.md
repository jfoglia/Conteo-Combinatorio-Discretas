# Casos de prueba - Contador de Contraseñas

## Prueba 1 - Conteo con repetición

Entradas:

¿Deseas definir grupos de caracteres? n

Ingresa la longitud de la contraseña: 4

Ingresa el tamaño del alfabeto permitido: 10

¿Está permitida la repetición? s

¿Debe contener al menos un dígito? n

¿Debe contener al menos una letra mayúscula? n

¿Debe contener al menos un símbolo especial? n

Cálculo:

Universo = 10⁴

Universo = 10000

Resultado esperado:

10000

Resultado obtenido:

10000

---

## Prueba 2 - Conteo sin repetición

Entradas:

¿Deseas definir grupos de caracteres? n

Ingresa la longitud de la contraseña: 3

Ingresa el tamaño del alfabeto permitido: 5

¿Está permitida la repetición? n

¿Debe contener al menos un dígito? n

¿Debe contener al menos una letra mayúscula? n

¿Debe contener al menos un símbolo especial? n

Cálculo:

P(5,3)

= 5! / 2!

= 5 × 4 × 3

= 60

Resultado esperado:

60

Resultado obtenido:

60

---

## Prueba 3 - Al menos un dígito

Entradas:

¿Deseas definir grupos de caracteres? n

Ingresa la longitud de la contraseña: 3

Ingresa el tamaño del alfabeto permitido: 36

¿Está permitida la repetición? s

¿Debe contener al menos un dígito? s

¿Cuántos dígitos tiene el alfabeto? 10

¿Debe contener al menos una letra mayúscula? n

¿Debe contener al menos un símbolo especial? n

Cálculo:

Universo:

36³ = 46656

Contraseñas sin dígitos:

26³ = 17576

Contraseñas válidas:

46656 − 17576

= 29080

Resultado esperado:

29080

Resultado obtenido:

29080

---

## Prueba 4 - Al menos un dígito y una mayúscula

Entradas:

¿Deseas definir grupos de caracteres? n

Ingresa la longitud de la contraseña: 3

Ingresa el tamaño del alfabeto permitido: 36

¿Está permitida la repetición? s

¿Debe contener al menos un dígito? s

¿Cuántos dígitos tiene el alfabeto? 10

¿Debe contener al menos una letra mayúscula? s

¿Cuántas mayúsculas tiene el alfabeto? 26

¿Debe contener al menos un símbolo especial? n

Cálculo:

Universo:

36³ = 46656

Sin dígitos:

26³ = 17576

Sin mayúsculas:

10³ = 1000

Sin dígitos y sin mayúsculas:

0³ = 0

Inclusión-Exclusión:

46656 - 17576 - 1000 + 0

= 28080

Resultado esperado:

28080

Resultado obtenido:

28080

---

## Prueba 5 - Dígitos, mayúsculas y símbolos

Entradas:

¿Deseas definir grupos de caracteres? n

Ingresa la longitud de la contraseña: 8

Ingresa el tamaño del alfabeto permitido: 70

¿Está permitida la repetición? s

¿Debe contener al menos un dígito? s

¿Cuántos dígitos tiene el alfabeto? 10

¿Debe contener al menos una letra mayúscula? s

¿Cuántas mayúsculas tiene el alfabeto? 26

¿Debe contener al menos un símbolo especial? s

¿Cuántos símbolos tiene el alfabeto? 8

Cálculo:

Universo:

70⁸ = 576480100000000

Sin dígitos:

60⁸ = 167961600000000

Sin mayúsculas:

44⁸ = 14048584704256

Sin símbolos:

62⁸ = 218340105584896

Sin dígitos y sin mayúsculas:

34⁸ = 1785793904896

Sin dígitos y sin símbolos:

52⁸ = 53459728531456

Sin mayúsculas y sin símbolos:

36⁸ = 2821109907456

Sin dígitos, sin mayúsculas y sin símbolos:

26⁸ = 208827064576

Aplicando inclusión-exclusión:

576480100000000
− 167961600000000
− 14048584704256
− 218340105584896

* 1785793904896
* 53459728531456
* 2821109907456
  − 208827064576

Resultado esperado:

233987976069120

Resultado obtenido:

233987976069120

