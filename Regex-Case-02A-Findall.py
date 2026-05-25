
#2. re.findall() → extraer todos
#Extrae TODAS las coincidencias.

import re
import os

os.system('cls')

text = "LOT100 LOT200 LOT300 VNX001 LOT789"

result = re.findall(r"LOT\d+", text)


print(result)


'''
Símbolos importantes Regex
Regex	Significado
\d	número
\w	letra/número
.	cualquier caracter
*	cero o más
+	uno o más
^	inicio
$	final



El patrón:

r"LOT\d+"

significa:

Busca textos que empiecen con LOT
y luego tengan números.
Parte por parte
1. LOT

Literalmente busca:

LOT
2. \d

Significa:

un dígito numérico

equivale a:

0-9
Ejemplos
Texto	Match
LOT1	Sí
LOT999	Sí
LOTABC	No
3. +

Significa:

uno o más

Entonces:

\d+

significa:

uno o más números
Visualmente
LOT\d+

equivale a:

LOT + números
Ejemplos válidos
Texto	Match
LOT1	Sí
LOT12	Sí
LOT99999	Sí
Ejemplos inválidos
Texto	Match
LOT	No
LOTABC	No
ABC123	No
Ejemplo Python
import re

text = "LOT12345"

result = re.search(r"LOT\d+", text)

print(result.group())

Resultado:

LOT12345


'''

