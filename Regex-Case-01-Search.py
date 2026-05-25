
#1. re.search() → buscar
#Busca la primera coincidencia.

import re
import os
os.system('cls')

log = "2026-05-23 ERROR CODE 500 SPC FAILURE"

pattern = r"ERROR"

result = re.search(pattern, log)


print("My Result: " + str(result.group()))

print("Detailed Results: " + str(result))




'''

1. re.Match object

Significa:

Existe una coincidencia.

O sea:

Regex encontró algo.
2. match='ERROR'

Significa:

El texto encontrado fue:
ERROR
3. span=(11,16)

Esto indica:

Dónde apareció ERROR dentro del texto.

Tu string era:

2026-05-23 ERROR CODE 500 SPC FAILURE

Contando posiciones:

012345678901234567890123456789
2026-05-23 ERROR CODE 500 SPC FAILURE
           ^^^^^

ERROR empieza en:

posición 11

y termina en:

posición 16

Por eso:

span=(11,16)
Lo importante realmente

Normalmente NO imprimes:

print(result)

porque eso imprime el objeto completo.

Lo normal es:

print(result.group())

Resultado:

ERROR

'''