
#2. re.findall() → extraer todos
#Extrae TODAS las coincidencias.

import re
import os

os.system('cls')

#3. re.match() → validar inicio
#Valida si el texto empieza con patrón.

import re

lot = "LOT12345"

result = re.match(r"LOT\d+", lot)

print("My Result: " + str(result.group()))

print("Detailed Results: " + str(result))




#Resultado:
	#• válido porque empieza con LOT. 




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

aca la funcion es match no fnd all

'''
